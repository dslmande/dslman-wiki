/** Bilder verzögert laden – manche Seiten zeigen über hundert Fotos. */
export function rehypeMedia() {
  const visit = (node, fn) => {
    fn(node);
    for (const child of node.children ?? []) visit(child, fn);
  };
  return (tree) => {
    visit(tree, (node) => {
      if (node.tagName === 'img') {
        node.properties = { loading: 'lazy', decoding: 'async', ...node.properties };
      }
    });
  };
}
