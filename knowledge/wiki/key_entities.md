# Key Entities

This page lists the major entities (teams, players, sources, governing structures) that appear across the scraped corpus, grouped by type. Each entity has a short summary drawn only from what the source files contain, and a "Mentioned in" list of the filenames where it is named.

## Teams

### Inter Miami CF
The most-cited team across the corpus and the **2025 MLS Cup champion**. Defeated the Vancouver Whitecaps in the 2025 final under first-season head coach **Javier Mascherano**, with a roster including 2022 World Cup champions **Lionel Messi**, **Sergio Busquets**, and **Rodrigo De Paul**. In the 2026 season, the team sits 3rd in the Eastern Conference (19 points from 11 matches as of the scrape) with Messi as top scorer (8 goals). Goalkeeper of record: Dayne St. Clair.
**Mentioned in:** `competitions_mls-cup-playoffs.md`, `en_comps_22_Major-League-Soccer-Stats.md`, `en_players_d70ce98e_Lionel-Messi.md`, `news.md`, `home.md` (homepage 2026 MLS preview list)

### Vancouver Whitecaps FC
The 2025 MLS Cup runner-up, defeated by Inter Miami in the final ("Ref Cam! Inter Miami down Vancouver Whitecaps in MLS Cup"). Referenced as a Western Conference opponent in 2026 Eastern Conference match-result links.
**Mentioned in:** `competitions_mls-cup-playoffs.md`, `en_comps_22_Major-League-Soccer-Stats.md` (via match links)

### Nashville SC
The 2026 Eastern Conference leader through the scrape window — 23 points from 10 matches (7-2-1, +15 GD, 2.30 PPG). Top scorer: Sam Surridge (9 goals). Goalkeeper: Brian Schwake. Average attendance 26,677.
**Mentioned in:** `en_comps_22_Major-League-Soccer-Stats.md`

### New England Revolution
2nd place in the 2026 Eastern Conference (19 pts from 10 matches). Co-leading scorers: Carles Gil and Peyton Miller (3 each). Goalkeeper: Matt Turner.
**Mentioned in:** `en_comps_22_Major-League-Soccer-Stats.md`

### Los Angeles FC (LAFC)
Cited as the home of the 2026 league-wide leaders in **assists** (Son Heung-min, 7) and **clean sheets** (Hugo Lloris, 8). Featured in news headline "LAFC shock San Diego late to boost CCC momentum" — a CONCACAF Champions Cup match.
**Mentioned in:** `en_comps_22_Major-League-Soccer-Stats.md`, `en_comps_22_stats_Major-League-Soccer-Stats.md`, `en_comps_22_shooting_Major-League-Soccer-Stats.md`, `en_comps_22_passing_Major-League-Soccer-Stats.md`, `en_comps_22_defense_Major-League-Soccer-Stats.md`, `en_comps_22_possession_Major-League-Soccer-Stats.md`, `en_comps_22_misc_Major-League-Soccer-Stats.md`, `news.md`

### FC Dallas
Home of co-leading league scorer Petar Musa (10 goals through the scrape window). Featured in news for "Petar Musa makes World Cup statement in FC Dallas win."
**Mentioned in:** all seven `en_comps_22_*` files (top-scorer banner), `news.md`

### Chicago Fire
4th place in 2026 Eastern Conference (17 pts), and home of co-leading league scorer **Hugo Cuypers** (10 goals). Goalkeeper: Chris Brady.
**Mentioned in:** all seven `en_comps_22_*` files, `en_comps_22_Major-League-Soccer-Stats.md`

### Other Eastern Conference clubs (2026 season standings)
FC Cincinnati (5th, 15 pts; top scorer Kévin Denkey, 6); Charlotte FC (6th, 14 pts; top scorer Pep Biel, 5); Toronto FC (7th, 14 pts); New York City FC (8th, 12 pts; top scorer Nicolás Ezequiel Fernández, 8); Columbus Crew (9th, 12 pts); D.C. United (10th, 12 pts; top scorer Tai Baribo, 6); New York Red Bulls (11th, 12 pts); Atlanta United (12th, 10 pts; top scorer Aleksei Miranchuk, 5); Orlando City (13th, 10 pts; top scorer Martín Ojeda, 7); CF Montréal (14th, 9 pts); Philadelphia Union (15th, 6 pts).
**Mentioned in:** `en_comps_22_Major-League-Soccer-Stats.md`, `news.md` (Orlando City's Florida Derby comeback over Inter Miami), `competitions_mls-cup-playoffs.md` (general 2026 MLS preview list)

### Western Conference teams (referenced but not enumerated in a table)
The following teams appear as opponents in 2026 Eastern Conference match-result links or in news/transfer headlines, confirming their existence in the league: Real Salt Lake, Colorado Rapids, LA Galaxy, Minnesota United, FC Dallas, Sporting Kansas City, San Jose Earthquakes, St. Louis CITY SC, San Diego FC, Austin FC, Houston Dynamo, LAFC, Vancouver Whitecaps. A complete Western Conference table was not captured in the scrape.
**Mentioned in:** `en_comps_22_Major-League-Soccer-Stats.md`, `news.md`, `standings.md` (referenced in highlight clips like "Austin FC vs. St. Louis CITY SC")

## Players

### Lionel Messi
The only player with a fully-scraped FBref profile. Full name **Lionel Andrés Messi Cuccittini**, position FW-MF (AM-WM), left-footed, 170 cm / 72 kg, born June 24, 1987 in Rosario, Argentina. National team: Argentina. Current club: **Inter Miami**, with reported wages of **$12,000,000 annual** (contract expires December 2028, per Capology). Honors include 8× Ballon d'Or, 4× The Best FIFA Men's Player, 9× La Liga Best Player, 2× UEFA Men's Player of the Year, 13× Domestic League Champion, 4× Champions League Champion, 2022 World Cup Champion, 17× FIFA FIFPro World XI. 2026 partial-season stats: 10 MP / 900 min / 8 goals / 1 assist in MLS, plus 2 MP / 180 min / 1 goal in CONCACAF Champions Cup. Inter Miami's top scorer in 2026.
**Mentioned in:** `en_players_d70ce98e_Lionel-Messi.md`, `en_comps_22_Major-League-Soccer-Stats.md`, `competitions_mls-cup-playoffs.md`

### Sergio Busquets
Named in the 2025 MLS Cup playoff coverage as one of Inter Miami's "World Cup champions" alongside Messi and De Paul. **No detailed profile is available** — the FBref scrape of his player page returned an HTTP 500 error (`en_players_00e7e57b_Sergio-Busquets.md` contains only the error message body).
**Mentioned in:** `competitions_mls-cup-playoffs.md`; failed scrape captured in `en_players_00e7e57b_Sergio-Busquets.md`

### Rodrigo De Paul
Named in the same Inter Miami "World Cup champions" headline as Messi and Busquets. **No further detail in the corpus** — De Paul does not have a scraped FBref profile.
**Mentioned in:** `competitions_mls-cup-playoffs.md`

### Jordi Alba
Implicitly part of the Inter Miami squad (referenced by the original scrape target list), but **the scraped file `en_players_8b04d6c1_Jordi-Alba.md` actually contains Pierre-Emile Højbjerg's profile** (Marseille / Denmark international) — the 8-char FBref player ID in the URL was wrong. The corpus therefore contains no actual data on Jordi Alba.
**Mentioned in:** filename only — content does not match.

### Petar Musa
Co-leader for most goals in the 2026 MLS season (10) at FC Dallas. Featured in news for a hat trick noted as a "World Cup statement."
**Mentioned in:** all seven `en_comps_22_*` files (top-scorer banner), `news.md`

### Hugo Cuypers
Co-leader for most goals in the 2026 MLS season (10) at Chicago Fire.
**Mentioned in:** all seven `en_comps_22_*` files

### Son Heung-min
2026 MLS assist leader (7) at Los Angeles FC. South Korean international.
**Mentioned in:** all seven `en_comps_22_*` files

### Hugo Lloris
2026 MLS clean-sheet leader (8) as goalkeeper at Los Angeles FC.
**Mentioned in:** all seven `en_comps_22_*` files

### Other named MLS players (visible as 2026 squad top scorers or in news/transfers)
Sam Surridge (Nashville SC), Carles Gil (NE Revolution), Peyton Miller (NE Revolution), Kévin Denkey (FC Cincinnati), Pep Biel (Charlotte FC), Dániel Sallói (Toronto FC), Nicolás Ezequiel Fernández (NYCFC), Wessam Abou Ali (Columbus Crew), Tai Baribo (D.C. United), Julian Hall (NY Red Bulls), Aleksei Miranchuk (Atlanta United), Martín Ojeda (Orlando City), Prince Owusu (CF Montréal), Danley Jean-Jacques and Milan Iloski (Philadelphia Union), plus goalkeepers Brian Schwake, Matt Turner, Dayne St. Clair, Chris Brady, Roman Celentano, Kristijan Kahlina, Luka Gavran, Matt Freese, Patrick Schulte, Sean Johnson, Ethan Horvath, Lucas Hoyos, Maxime Crépeau, Thomas Gillier, Andre Blake. Recent transfer-tracker subjects: Noel Caliskan (Real Salt Lake), Arnau Farnós (NYCFC), Dylan Chambost (Columbus Crew), Aron John (Charlotte FC homegrown), Mattheo Dimareli (Houston Dynamo homegrown), Rodolfo Aloko (Charlotte FC). Other MLS Cup goal-scorer references: M. Uzuni and C. Ramírez (vs. STL highlights).
**Mentioned in:** `en_comps_22_Major-League-Soccer-Stats.md`, `news.md`, `standings.md`

### Pierre-Emile Højbjerg (mistakenly under "Jordi-Alba" filename)
Although not relevant to MLS recruitment, his profile is in the corpus due to the wrong-ID scrape. Pierre-Emile Højbjerg is a 30-year-old Danish midfielder (CM-DM, right-footed, 185 cm / 81 kg, born August 5, 1995 in Copenhagen) currently at **Marseille** (Ligue 1, France) on €122,308/week wages until June 2028. Honors: 2× Bundesliga Champion, 2022 Danish Male Footballer of the Year. 2025-2026 stats: 30 Ligue 1 matches (3 goals, 4 assists). Marseille is shown 7th in Ligue 1 with a 16-5-11 record.
**Mentioned in:** `en_players_8b04d6c1_Jordi-Alba.md` (incorrectly named)

## Analysts and sources

### FBref (`fbref.com`)
The Sports Reference family's football-statistics site. Provides MLS coverage at competition `id=22` with a 2026 season landing page plus seven dedicated category sub-pages (Standard, Shooting, Passing, Defense, Possession, Miscellaneous; Goalkeeping and Playing Time also linked). Each player has a stable 8-character ID and a multi-tab profile (overview, match logs, goal logs, all-competition rollups, comparison tools). Wage data is integrated via Capology. The site offers a paid tier called Stathead.
**Mentioned in:** all 10 fbref.com files (the seven competition pages plus three player files)

### MLS Soccer (`mlssoccer.com`)
The league's official site. Covers the league office, organization (Executives, Official Partners), official rule documents (Roster Rules & Regulations, Competition Guidelines, Fan Code of Conduct), and editorial output (news, transfer tracker, MLS Cup Playoffs landing). Distributes content via a partnership with Apple TV ("Come Kick It! Watch MLS on Apple TV").
**Mentioned in:** `about.md`, `news.md`, `standings.md`, `competitions_mls-cup-playoffs.md`

### American Soccer Analysis / ASA (`americansocceranalysis.com`)
An independent soccer-analytics publication. From the scraped homepage we can see: bylined contributing writers include **Ben Bellman**, **Joe Lowery**, and **Eliot McKinley**; the publication runs a **Patreon at $5/month** for access to "data visualization tools we use to make these previews"; **Mike Imburgio** runs a "firewalled consulting arm" of ASA that works with MLS clubs (Minnesota United is the example given); and ASA partners with the **Expected Own Goals** podcast for audio versions of its coverage. ASA produces season previews for both MLS and NWSL, plus thematic analytical pieces on tactics (e.g., long throw-ins) and rules (roster rules, expected goals, academy system).
**Mentioned in:** all four `americansocceranalysis.com` files (`home.md` plus three article slugs that returned the same homepage)

## Governing structures and rules

The corpus references the *names* of several MLS-specific roster mechanisms but does not contain their substantive descriptions (because the relevant ASA articles did not scrape successfully and the official rule documents at mlssoccer.com were not in the target list). The following are attested to as topics that exist in MLS:

- **Roster Rules & Regulations** — listed as a top-level navigation item on `mlssoccer.com/about/` (source: `about.md`); rule details not in this corpus.
- **Competition Guidelines** — also a top-level mlssoccer.com nav item (source: `about.md`).
- **Homegrown Players** — attested by news headlines explicitly tagged "homegrown" (Aron John for Charlotte FC, Mattheo Dimareli for Houston Dynamo — source: `news.md`); the formal definition of the homegrown rule is not in the corpus.
- **The MLS Draft** (specifically the 2026 MLS Draft) — linked from FBref's 2026 MLS overview (source: `en_comps_22_Major-League-Soccer-Stats.md`); the draft mechanics are not detailed.
- **Salary / wages** — not formally explained, but Capology integration on FBref provides per-player wage figures (source: `en_players_d70ce98e_Lionel-Messi.md`).
- **MLS Cup Playoffs** — confirmed as the post-regular-season tournament (sources: `competitions_mls-cup-playoffs.md`, `en_comps_22_Major-League-Soccer-Stats.md`); detailed bracket structure not captured.
- **CONCACAF Champions Cup (CCC)** — referenced as a separate competition that MLS clubs play in (sources: `news.md` "LAFC shock San Diego late to boost CCC momentum"; `en_players_d70ce98e_Lionel-Messi.md` lists "CCC" as one of Messi's 2026 stat categories).
- **Designated Player rule, GAM/TAM (allocation money), U22 Initiative** — these terms are referenced indirectly via ASA URL slugs (`breaking-down-mls-roster-rules`) and were the topics the user expected the wiki to cover, **but the article bodies were not captured**. The corpus cannot answer detailed questions about how these mechanisms work.
