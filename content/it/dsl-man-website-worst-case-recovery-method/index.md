---
title: "DSL-man website worst case recovery method"
space: "IT"
space_key: "IT"
type: page
created: "2020-01-08T20:24:36"
updated: "2020-01-08T20:24:59"
confluence_id: "884768"
confluence_url: "https://diysynth.wiki.dsl-man.de/wiki/spaces/IT/pages/884768"
---

# DSL-man website worst case recovery method

## **not funny but important !!**

everyone must die, sometimes earlier sometimes later, in case of an casual vacancy of me is the responsible root server owner: **Bernd Dau from Germany (Koenigslutter)**

he have access on the rootserver.

it's not needed to be a confluence skilled admin to bring back Admin permissions to another person or make an backup or get all data to install a new system.

few solutions to get Confluence Admin permissions or get receive all data to 

**A:** **hack the database entry (easy for most sys-admins)**

1. you need an user account or must know a user (lets say UserA) and you must know the password of UserA.

2. shutdown the confluence application (tomcat\_directory/inst/bin/stop-confluence.sh)

3. copy in the database the password hash from the UserA to the user from me (username: LED-man)

4. start the confluence (tomcat\_directory/inst/bin/start-confluence.sh)

**B. contact Checkmate (from Germany) or Martin Jan Koehler (from Austria) - both have Confluence Admin permissions** (in planning)     (they don't have rootserver access)

they can export every Space to a zip file - then they need to install a new confluence and import the space exports, the exports contain all content & attachments)

(my System use 15 spaces (DSO, TTSH, SOLOMAN and more) 

that's how I backup my system atm.

**C. contact a IT-Consulting company which is Atlassian Partner - they know some other tricks**

**D. standard way for migration or server movement:** export the database (sql) and export the (home and inst) directory - copy this on the new server.

but you also need the Confluence Admins to get Admin access in the webapplication.

**good to know:**

1.the global export function do NOT work, because the system is too big

2.some pages are hidden for users (ttsh, cloney )they are restricted by groups - only Confluence Admins can change it.

**worst case: system is down  - you can't read this page 😉**
