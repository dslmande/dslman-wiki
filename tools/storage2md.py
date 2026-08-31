#!/usr/bin/env python3
"""Confluence-Storage-XHTML -> Markdown.

Ein rekursiver Renderer ueber den XML-Baum. Kennt die HTML-Teilmenge, die
Confluence erzeugt, und die ac:/ri:-Konstrukte (Makros, Bilder, Links).
"""
import html.entities, os, re, xml.etree.ElementTree as ET
from collections import Counter

AC = "{http://atlassian.com/content}"
RI = "{http://atlassian.com/resource/identifier}"
WRAP = ('<root xmlns:ac="http://atlassian.com/content" '
        'xmlns:ri="http://atlassian.com/resource/identifier">%s</root>')

KEEP = ("amp", "lt", "gt", "quot", "apos")
ENT = re.compile(r"&([A-Za-z][A-Za-z0-9]*);")

# Makros, die in der Website-Ausgabe nichts verloren haben
DROP = {"toc", "toc-zone", "anchor", "children", "pagetree", "recently-updated",
        "contentbylabel", "livesearch", "space-details", "create-from-template",
        "detailssummary", "labels-list", "navitabs", "content-report-table",
        "blog-posts", "spacevariables", "profile", "userlister", "sectionmetrics",
        "contributors", "popular-labels", "change-history", "listlabels", "spaces",
        "space-attachments", "usage", "recently-used-labels", "pagetreesearch",
        "contributors-summary", "roadmap"}

# Makros, die nur Layout sind: Inhalt uebernehmen, Huelle verwerfen
TRANSPARENT = {"tabs-tabsgroup", "tabs-tabelement", "details", "section", "column",
               "excerpt", "panelbox", "div", "align", "auto-number-headings",
               "content-wrapper", "bootstrap-row", "bootstrap-column"}
CALLOUT = {"info": "Info", "note": "Hinweis", "warning": "Achtung", "tip": "Tipp",
           "panel": "", "success": "Erfolg", "error": "Fehler"}
IMG_EXT = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp")


def fix_entities(s):
    def sub(m):
        n = m.group(1)
        if n in KEEP:
            return m.group(0)
        cp = html.entities.name2codepoint.get(n)
        return chr(cp) if cp else " " if n == "nbsp" else m.group(0)
    return ENT.sub(sub, s)


def esc(t):
    t = t.replace("\\", "\\\\")
    for c in "*_`[]":
        t = t.replace(c, "\\" + c)
    return t.replace("<", "&lt;").replace(">", "&gt;")


def local(tag):
    return tag.rsplit("}", 1)[-1]


class Converter:
    """Konvertiert eine Seite. `ctx` liefert Link- und Anhangsaufloesung."""

    def __init__(self, ctx=None):
        self.ctx = ctx or {}
        self.unknown = Counter()

    # ---------- oeffentlich ----------
    def convert(self, storage):
        try:
            root = ET.fromstring(WRAP % fix_entities(storage or ""))
        except ET.ParseError:
            # Letzte Rettung: Tags entfernen, Text behalten
            return re.sub(r"<[^>]+>", " ", fix_entities(storage or "")).strip(), self.unknown
        md = self.kids(root)
        md = re.sub(r"[ \t]+\n", "\n", md)
        md = re.sub(r"\n{3,}", "\n\n", md)
        return md.strip() + "\n", self.unknown

    # ---------- Bausteine ----------
    def kids(self, el):
        out = []
        if el.text:
            out.append(esc(el.text))
        for c in el:
            out.append(self.node(c))
            if c.tail:
                out.append(esc(c.tail))
        return "".join(out)

    def raw_text(self, el):
        """Text ohne Markdown-Escaping (fuer Codebloecke, Titel, Alt-Texte)."""
        return "".join(el.itertext())

    def block(self, s):
        s = s.strip("\n")
        return "\n\n" + s + "\n\n" if s.strip() else ""

    def node(self, el):
        t = local(el.tag)
        fn = getattr(self, "t_" + t.replace("-", "_"), None)
        if fn:
            return fn(el)
        if el.tag.startswith(AC):
            return self.ac(el, t)
        if el.tag.startswith(RI):
            return ""
        return self.kids(el)  # unbekanntes HTML transparent durchreichen

    # ---------- HTML-Bloecke ----------
    def t_p(self, el):
        return self.block(self.kids(el))

    def t_div(self, el):
        return self.block(self.kids(el))

    def t_section(self, el):
        return self.block(self.kids(el))

    def t_hr(self, el):
        return self.block("---")

    def t_br(self, el):
        return "  \n"

    def _h(self, el, n):
        txt = " ".join(self.kids(el).split())
        if not txt:
            return ""
        if getattr(self, "in_cell", False):      # in Tabellenzellen gibt es keine Ueberschriften
            return "\n**" + txt.strip("*") + "**\n"
        return self.block("#" * n + " " + txt)

    for _i in range(1, 7):
        exec("def t_h%d(self, el): return self._h(el, %d)" % (_i, _i))

    def t_blockquote(self, el):
        body = self.kids(el).strip()
        q = "\n".join("> " + l if l.strip() else ">" for l in body.split("\n"))
        return self.block(re.sub(r"(?:\n>[ \t]*(?=\n))+", "\n>", q).strip())

    def t_pre(self, el):
        return self.block("```\n" + self.raw_text(el).strip("\n") + "\n```")

    # ---------- Listen ----------
    def t_ul(self, el, depth=0):
        return self._list(el, depth, ordered=False)

    def t_ol(self, el, depth=0):
        return self._list(el, depth, ordered=True)

    def _list(self, el, depth, ordered):
        items, n = [], 0
        for li in el:
            if local(li.tag) != "li":
                continue
            n += 1
            marker = ("%d. " % n) if ordered else "- "
            items.append(self._li(li, depth, marker))
        return self.block("\n".join(i for i in items if i.strip()))

    def _li(self, li, depth, marker):
        pad = "  " * depth
        inner, subs = [], []
        if li.text:
            inner.append(esc(li.text))
        for c in li:
            if local(c.tag) in ("ul", "ol"):
                subs.append(self._list(c, depth + 1, local(c.tag) == "ol").strip("\n"))
            else:
                inner.append(self.node(c))
            if c.tail:
                inner.append(esc(c.tail))
        body = re.sub(r"\n{2,}", "\n", "".join(inner)).strip()
        lines = body.split("\n")
        out = pad + marker + (lines[0] if lines else "")
        for l in lines[1:]:
            out += "\n" + pad + "  " + l
        for s in subs:
            out += "\n" + s
        return out

    # ---------- Tabellen ----------
    def t_table(self, el):
        rows = []
        for tr in el.iter():
            if local(tr.tag) != "tr":
                continue
            cells, head = [], False
            for td in tr:
                lt = local(td.tag)
                if lt not in ("td", "th"):
                    continue
                head = head or lt == "th"
                self.in_cell = True
                txt = re.sub(r"\s*\n\s*", "<br>", self.kids(td).strip())
                self.in_cell = False
                txt = re.sub(r"^(?:<br>)+|(?:<br>)+$", "", re.sub(r"(<br>)+", "<br>", txt))
                cells.append(txt.replace("|", "\\|").strip() or " ")
            if cells:
                rows.append((head, cells))
        if not rows:
            return ""
        width = max(len(c) for _, c in rows)
        out = []
        for i, (head, cells) in enumerate(rows):
            cells = cells + [" "] * (width - len(cells))
            out.append("| " + " | ".join(cells) + " |")
            if i == 0:
                out.append("|" + "---|" * width)
        if not rows[0][0]:                       # keine Kopfzeile: leere Kopfzeile einziehen
            out.insert(0, "|" + "---|" * width)
            out.insert(0, "|" + "   |" * width)
            out.pop(3)
        return self.block("\n".join(out))

    # ---------- Inline ----------
    def _wrap(self, el, mark):
        inner = self.kids(el).strip()
        if not inner:
            return ""
        return mark + inner + mark

    def t_strong(self, el):
        return self._wrap(el, "**")

    t_b = t_strong

    def t_em(self, el):
        return self._wrap(el, "*")

    t_i = t_em

    def t_code(self, el):
        return "`" + self.raw_text(el).strip() + "`"

    def t_del(self, el):
        return self._wrap(el, "~~")

    t_s = t_strike = t_del

    def t_u(self, el):
        return self.kids(el)

    def t_span(self, el):
        return self.kids(el)

    def t_sup(self, el):
        return "<sup>" + self.kids(el) + "</sup>"

    def t_sub(self, el):
        return "<sub>" + self.kids(el) + "</sub>"

    def t_time(self, el):
        return el.get("datetime", "")

    def t_a(self, el):
        href = el.get("href", "")
        text = self.kids(el).strip() or esc(href)
        return "[%s](%s)" % (text, self.ctx_url(href)) if href else text

    def t_img(self, el):
        return "![%s](%s)" % (el.get("alt", ""), self.ctx_url(el.get("src", "")))

    def ctx_url(self, url):
        fn = self.ctx.get("url")
        return fn(url) if fn else url

    # ---------- Confluence: Bilder, Links, Layout ----------
    def t_image(self, el):
        att = el.find(RI + "attachment")
        url = el.find(RI + "url")
        alt = el.get(AC + "alt") or ""
        if att is not None:
            fn = att.get(RI + "filename", "")
            return "\n\n![%s](%s)\n\n" % (alt or fn, self.asset(fn))
        if url is not None:
            return "\n\n![%s](%s)\n\n" % (alt, url.get(RI + "value", ""))
        return ""

    def t_link(self, el):
        body = el.find(AC + "link-body")
        if body is None:
            body = el.find(AC + "plain-text-link-body")
        text = (self.kids(body).strip() if body is not None else "")
        anchor = el.get(AC + "anchor") or ""

        page = el.find(RI + "page")
        if page is None:
            page = el.find(RI + "blog-post")
        if page is not None:
            title = page.get(RI + "content-title", "")
            skey = page.get(RI + "space-key")
            href = self.page_link(title, skey)
            if anchor:
                href += "#" + slug_anchor(anchor)
            return "[%s](%s)" % (text or esc(title), href)

        att = el.find(RI + "attachment")
        if att is not None:
            fn = att.get(RI + "filename", "")
            return "[%s](%s)" % (text or esc(fn), self.asset(fn))

        user = el.find(RI + "user")
        if user is not None:
            return text or "@Autor"
        if anchor:
            return "[%s](#%s)" % (text or anchor, slug_anchor(anchor))
        return text

    def t_layout(self, el):
        return self.kids(el)

    t_layout_section = t_layout_cell = t_adf_extension = t_adf_node = t_layout
    t_inline_comment_marker = t_layout

    def t_adf_fallback(self, el):
        return ""

    def t_placeholder(self, el):
        return ""

    def t_parameter(self, el):
        return ""

    def t_rich_text_body(self, el):
        return self.kids(el)

    def t_plain_text_body(self, el):
        return self.raw_text(el)

    def t_emoticon(self, el):
        return EMOJI.get(el.get(AC + "name", ""), el.get(AC + "emoji-fallback", "")) or ""

    # ---------- Aufgabenlisten ----------
    def t_task_list(self, el):
        out = []
        for task in el.findall(AC + "task"):
            st = task.find(AC + "task-status")
            done = (st is not None and (st.text or "").strip() == "complete")
            body = task.find(AC + "task-body")
            txt = re.sub(r"\s*\n\s*", " ", self.kids(body).strip()) if body is not None else ""
            out.append("- [%s] %s" % ("x" if done else " ", txt))
        return self.block("\n".join(out))

    # ---------- Makros ----------
    def params(self, el):
        """ac:parameter-Elemente als dict name -> Element."""
        return {p.get(AC + "name", ""): p for p in el.findall(AC + "parameter")}

    def ptext(self, ps, name, default=""):
        p = ps.get(name)
        return (self.raw_text(p).strip() if p is not None else default)

    def pfile(self, ps, *names):
        """Dateiname aus einem Parameter, der eine ri:attachment-Referenz haelt."""
        for n in names:
            p = ps.get(n)
            if p is None:
                continue
            att = p.find(RI + "attachment")
            if att is not None:
                return att.get(RI + "filename", "")
            url = p.find(RI + "url")
            if url is not None:
                return url.get(RI + "value", "")
            txt = self.raw_text(p).strip()
            if txt:
                return txt
        return ""

    def t_structured_macro(self, el):
        name = (el.get(AC + "name") or "").lower()
        ps = self.params(el)
        body = el.find(AC + "rich-text-body")

        if name in DROP:
            return ""

        if name in ("code", "noformat", "codeblock"):
            lang = self.ptext(ps, "language")
            txt = self.raw_text(el.find(AC + "plain-text-body")) if el.find(AC + "plain-text-body") is not None else ""
            return self.block("```%s\n%s\n```" % (lang, txt.strip("\n")))

        if name in CALLOUT:
            label = self.ptext(ps, "title") or CALLOUT[name]
            inner = self.kids(body).strip() if body is not None else ""
            head = ("**%s**\n\n" % esc(label)) if label else ""
            quoted = "\n".join("> " + l if l.strip() else ">" for l in (head + inner).split("\n"))
            quoted = re.sub(r"(?:\n>[ \t]*(?=\n))+", "\n>", quoted).strip()
            return self.block(quoted)

        if name == "expand":
            title = self.ptext(ps, "title") or "Mehr anzeigen"
            inner = self.kids(body).strip() if body is not None else ""
            return self.block("<details>\n<summary>%s</summary>\n\n%s\n\n</details>" % (title, inner))

        if name == "status":
            return "`%s`" % (self.ptext(ps, "title") or "")

        if name in ("view-file", "viewpdf", "viewdoc", "viewxls", "viewppt", "multimedia", "widget"):
            fn = self.pfile(ps, "name", "filename", "url")
            if not fn:
                return ""
            if fn.startswith("http"):
                return self.block("[%s](%s)" % (esc(fn), fn))
            link = self.asset(fn)
            if fn.lower().endswith(IMG_EXT):
                return self.block("![%s](%s)" % (esc(fn), link))
            return self.block("[%s](%s)" % (esc(fn), link))

        if name == "drawio":
            fn = self.ptext(ps, "diagramName")
            for cand in (fn + ".png", fn):
                if cand and self.has_asset(cand):
                    return self.block("![%s](%s)" % (esc(fn), self.asset(cand)))
            return self.block('*(Diagramm "%s" aus Confluence - nicht als Datei exportierbar)*' % fn)

        if name in ("gallery",):
            return self.block(self.gallery())

        if name == "attachments":
            return self.block(self.attachment_list())

        if name in TRANSPARENT:
            inner = self.kids(body).strip() if body is not None else ""
            title = self.ptext(ps, "title") or self.ptext(ps, "name")
            if name == "tabs-tabelement" and title:
                inner = "**%s**\n\n%s" % (esc(title), inner)
            return self.block(inner) if inner else ""

        if name in ("gliffy", "drawio-diagram"):
            nm = self.ptext(ps, "name") or self.ptext(ps, "diagramName")
            for cand in (nm + ".png", nm):
                if cand and self.has_asset(cand):
                    return self.block("![%s](%s)" % (esc(nm), self.asset(cand)))
            return self.block("*(Diagramm \"%s\" – lag nur im Confluence-Editor vor)*" % nm)

        if name == "html-macro":
            b = el.find(AC + "plain-text-body")
            return self.block(self.raw_text(b).strip()) if b is not None else ""

        if name in ("excerpt-include", "include"):
            p = ps.get("")
            title = self.raw_text(p).strip() if p is not None else self.ptext(ps, "name")
            pg = p.find(RI + "page") if p is not None else None
            if pg is not None:
                title = pg.get(RI + "content-title", title)
                return self.block("→ siehe [%s](%s)" % (esc(title), self.page_link(title, pg.get(RI + "space-key"))))
            return self.block("→ siehe %s" % esc(title))

        if name in ("iframe", "html", "html-bobswift"):
            src = self.ptext(ps, "src") or self.ptext(ps, "url")
            if src:
                return self.block("[%s](%s)" % (esc(src), src))
            return self.block(self.raw_text(el.find(AC + "plain-text-body")).strip()
                              if el.find(AC + "plain-text-body") is not None else "")

        # Unbekannt: Inhalt retten, Makro protokollieren
        self.unknown[name] += 1
        inner = self.kids(body).strip() if body is not None else ""
        return self.block("<!-- confluence-macro: %s -->\n%s" % (name, inner) if inner
                          else "<!-- confluence-macro: %s -->" % name)

    def ac(self, el, tag):
        return self.kids(el)

    # ---------- Kontext-Bruecken ----------
    def asset(self, filename):
        fn = self.ctx.get("asset")
        return fn(filename) if fn else filename

    def has_asset(self, filename):
        fn = self.ctx.get("has_asset")
        return fn(filename) if fn else False

    def page_link(self, title, space_key):
        fn = self.ctx.get("page")
        return fn(title, space_key) if fn else "#"

    def gallery(self):
        fn = self.ctx.get("gallery")
        return fn() if fn else ""

    def attachment_list(self):
        fn = self.ctx.get("attachment_list")
        return fn() if fn else ""


def slug_anchor(t):
    return re.sub(r"[^a-z0-9]+", "-", (t or "").lower()).strip("-")


EMOJI = {"tick": "✅", "cross": "❌", "check": "✅", "warning": "⚠️", "information": "ℹ️",
         "question": "❓", "thumbs-up": "👍", "thumbs-down": "👎", "star": "⭐",
         "light-on": "💡", "light-off": "💡", "red-star": "⭐", "yellow-star": "⭐",
         "green-star": "⭐", "blue-star": "⭐", "plus": "➕", "minus": "➖", "smile": "🙂",
         "sad": "🙁", "cheeky": "😜", "laugh": "😄", "wink": "😉", "heart": "❤️"}
