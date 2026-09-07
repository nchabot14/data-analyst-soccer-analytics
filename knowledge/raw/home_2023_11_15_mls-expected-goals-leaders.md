---
source_url: https://www.americansocceranalysis.com/home/2023/11/15/mls-expected-goals-leaders
scraped_at: 2026-09-07T14:32:43.712368+00:00
source: americansocceranalysis.com
---

American Soccer Analysis — American Soccer Analysis

[![American Soccer Analysis](https://images.squarespace-cdn.com/content/v1/5352fb7ce4b0bf79997bfc81/1435180609079-51SLX979FJ44N8A4R9PG/banner-03.png?format=1500w)](https://www.americansocceranalysis.com/)

![ASAlogo.png](https://images.squarespace-cdn.com/content/v1/5352fb7ce4b0bf79997bfc81/1583345552222-KI88BLW48F32BESTQZXI/ASAlogo.png)

[![American Soccer Analysis](https://images.squarespace-cdn.com/content/v1/5352fb7ce4b0bf79997bfc81/1435180609079-51SLX979FJ44N8A4R9PG/banner-03.png?format=1500w)](https://www.americansocceranalysis.com/)

# American Soccer Analysis

[![American Soccer Analysis](https://images.squarespace-cdn.com/content/v1/5352fb7ce4b0bf79997bfc81/1435180609079-51SLX979FJ44N8A4R9PG/banner-03.png?format=1500w)](https://www.americansocceranalysis.com/)

No results found

[![Replication Project-ish: Projecting MLS Performance based on  MLS Next Pro Data](https://images.squarespace-cdn.com/content/v1/5352fb7ce4b0bf79997bfc81/1787460581956-IWVNPERKCDN08XUFSJG9/backtest_wheel_frankie_westfield.png)](https://www.americansocceranalysis.com/home/2026/8/22/replication-project-ish-projecting-mls-performance-based-on-mls-next-pro-data)

[By Kieran Doyle](https://bsky.app/profile/kierdoyle.bsky.social)

In 2022, Daniel Dinsdale and Joe Gallagher of Stats Perform (the artist formerly known as Opta) released an [arXiv of a paper titled “ _Transfer Portal: Accurately Forecasting the Impact of a Player Transfer in Soccer”._](https://arxiv.org/abs/2201.11533) The paper is a worthwhile read, but the idea can sort of be summed up as the three approaches.

1. Identify how the player is currently doing on a per 90’ basis, for the metrics you care about.

2. Identify how their team and league fits into the global hierarchy, in relation to other teams and leagues.

3. For players with insufficient data, weight the average of their small data sample and some prior for the league/age/position etc.


Then take all those things, stick it in some neural networks, and try to predict the impact if that player moved from team A to team B. And it works! It’s a pretty good predictor of how players do when they move clubs, reducing mean squared error by 50% compared to assuming their performance translated over one-to-one. This is a cool result, and league translation/transfer projection is an extremely difficult task.

Where my brain went when I read this paper six years ago was, wow, this would be a great approach to trying to figure out how good young players might be. Three months after this, MLS Next Pro started its inaugural season, in March of 2022. While Opta’s work on this was based on some 26,000 samples and 2600 transfers, after four seasons of MLS Next Pro we certainly don’t have 2600 players graduating to their first team, but we might have enough to try.

[Read More](https://www.americansocceranalysis.com/home/2026/8/22/replication-project-ish-projecting-mls-performance-based-on-mls-next-pro-data)

[![Scream and Shout: an xClaim Model for Goalkeeper Cross Collection](https://images.squarespace-cdn.com/content/v1/5352fb7ce4b0bf79997bfc81/1785390163930-J0YZ9705RRYJJR777CLH/xclaim_cross_type_clusters_v3.png)](https://www.americansocceranalysis.com/home/2026/7/29/scream-and-shout-an-xclaim-model-for-goalkeeper-cross-collection)

[By Kieran Doyle](https://bsky.app/profile/kierdoyle.bsky.social)

Ever since we built [goals added (g+)](https://www.americansocceranalysis.com/what-are-goals-added) oh so many years ago, I’ve largely been unhappy with how we’ve treated goalkeepers here at ASA. ASA, the masterful puppeteer in the shadows crafting the rise of [Matt Turner and Djordje Petrovic](https://www.americansocceranalysis.com/home/2023/8/28/thomas-bayes-meet-djordje-petrovic) to the Premier League, letting them down! And so, my fellow analytics practitioners, ask not what your goalkeeper can do for you, but what you can do for your goalkeeper.

ASA and the analytics community at large has gotten to a pretty good place with goalkeeper shotstopping, at least with event only data. You scale the saves they make by the quality of chances they face, you accept that’s a pretty noisy metric season to season, it tracks directly to goals, it’s sort of easy. We have done a somewhat less good job looking at how the other parts of being a goalkeeper impact the game. Goals added does an okay job, assigning the value of their sweeping to the situations they interrupt. But it’s an imperfect picture, the whole point of sweeping is that you are preventing a much more dangerous situation from occurring further down the road, but where you are now is not actually that dangerous on its own. The ball playing side is similar, goalkeepers are so far from goal that aside from long kicks up the field, virtually all the passing they do is meaningless in the eye of a possession value model.

Today, though, we start with cross claiming. If you take the entire MLS dataset we have at ASA, the most productive cross claiming season by g+ is about +0.5 g+ across the entire season. Half a goal. Intercepting a cross in the 6 yard box off the head of a striker itself is worth half a goal! It’s wrong, and I won’t stand for this goalkeeper cross claiming erasure #GKUnion.

[Read More](https://www.americansocceranalysis.com/home/2026/7/29/scream-and-shout-an-xclaim-model-for-goalkeeper-cross-collection)

[By David Almona](https://bsky.app/profile/almondanalysis.bsky.social)

At the end of a season in soccer, the Golden Glove is awarded to the goalkeeper that has kept the most clean sheets. It seems intuitive, as being the last line of defense, their job is mainly to stop any shots that make it past the defense from entering the goal. However, a clean sheet is when the _team_ prevents their opponent from scoring, not just the goalkeeper; it’s a team effort.

[Read More](https://www.americansocceranalysis.com/home/2026/7/28/a-new-goalkeeper-metric-clean-sheets-earned-cse)

## How scoring in the Men's World Cup compares to domestic leagues

By [Jamon Moore](https://bsky.app/profile/jamonm.bsky.social)

During the pandemic, when [Carlon Carpenter](https://bsky.app/profile/carloncarpenter.bsky.social) and I researched the impact of certain types of soccer passes, we were blown away by how important they were to goal scoring. We wrote 10 articles about them throughout 2021, called the “ [Where Goals Come From](https://www.americansocceranalysis.com/?offset=1614099600614&tag=Where+Goals+Come+From)” series. Even from those 10 articles, we never imagined the reach they would have in clubs across the world.

Now, we examine the world’s premier competition and compare it to our original and ongoing research on how shots are created and goals are scored in domestic league competitions.

[Read More](https://www.americansocceranalysis.com/home/2026/7/18/where-goals-come-from-fifa-mens-world-cup-edition)

[By Kieran Doyle](https://bsky.app/profile/kierdoyle.bsky.social)

MLS is back on Thursday, as we return from the World Cup break into a season finely poised to be one of the most fun we’ve had in quite some time. At the same time, our friends [John Muller](https://bsky.app/profile/johnspacemuller.com) and [Mike Imburgio](https://bsky.app/profile/mimburgio.bsky.social) have launched their new app, [Futi](https://bsky.app/profile/futi.live). I’m sure they agonized over every word of their tagline, so I’ll copy it here:

_The new app that makes football make sense. Follow your favorite teams and players with real-time scores, shareable data visuals and pro analytics made simple._

While ideologically we believe it’s called soccer, the app definitely does what it says on the tin. As such, I thought it’d be fun to dig in and see what Futi tells me to keep an eye on as we welcome MLS Saturday night’s back into our hearts. If you like what you see here (every image in here will be right out of the iOS app), head to [futi.live](https://futi.live/) and check it out for yourself.

[Read More](https://www.americansocceranalysis.com/home/2026/7/11/mls-is-back-futi-style)

[By Theresa Pham](https://www.linkedin.com/in/theresap90/)

Expected Threat (xT) is a model that estimates the value of a pass or carry based on its likelihood of leading to a shot and the danger associated with that shot. Unlike [Karun Singh’s original xT framework](https://karun.in/blog/expected-threat.html), which relies entirely on historical transition probabilities, this version incorporates a logistic expected goals (xG) component to better capture shot quality. This analysis is inspired by [similar work conducted by Chloe Sainsbury in 2025](https://beyondthetouchline.substack.com/p/who-is-the-most-dangerous-passer).

[Read More](https://www.americansocceranalysis.com/home/2026/7/7/a-2026-nwsl-midseason-analysis-from-the-lens-of-expected-threat)

## Towards a manual for the most common restart

[By Ben Bellman](https://bsky.app/profile/beninquiring.bsky.social)

Whether you love long attacking throw-ins or hate them, there is no denying that they’ve become both a key feature and flashpoint in men’ssoccer in the past year. John Muller likely sparked a renaissance of the tactic (and a soon-to-be Arsenal title) with his [2023 article for The Athletic](https://www.nytimes.com/athletic/4297050/2023/03/11/get-it-launched-explaining-why-long-throw-ins-into-the-box-are-undervalued/), and Joe Lowery and I [borrowed his method for Backheeled](https://www.backheeled.com/how-some-mls-teams-are-using-long-throw-ins-to-play-smarter-soccer/) when Minnesota United started longthrowmaxxing in 2025 ( _Editor’s note: Minnesota work with Mike Imburgio through ASA’s firewalled consulting arm_). But while each game has about 40 throw-ins on average, only about 10 of those throws happen close enough to reach the box. But apart from Formerly Called Twitter jokes about consultant [Thomas Grønnemark](https://www.sloansportsconference.com/people/thomas-gronnemark), there hasn’t been much commentary about all the other ones in popular media or public analytics circles. The only exceptions I’m aware of are Eliot McKinley’s 2018 [two-part](https://www.americansocceranalysis.com/home/2018/11/27/game-of-throw-ins) [opus](https://www.americansocceranalysis.com/home/2018/12/4/a-feast-for-throws) on this very website, and some [recent academic work](https://shura.shu.ac.uk/35132/1/Stone-AnalysisOfThrowInsStrategy%28AM%29.pdf) on the top 5 European leagues that, if you like in-text citations and interpreting regressions, is an excellent spoiler for the rest of this article.

[Read More](https://www.americansocceranalysis.com/home/2026/4/15/throw-in-it-back)

_Our 2026 NWSL Season Previews have started and today we hit the Washington Spirit and NJ/NY Gotham. If you want to support this coverage of the league,_ [_you can head to our Patreon_](https://www.patreon.com/americansocceranalysis) _. For $5 a month you can get access to a lot of the data visualization tools we use to make these previews._

_If you’re more of an audio person, our friends at Expected Own Goals spoke to Riss Willett of Shea Butter FC to talk Spirit, and Jenna Tonelli of Sports Illustrated on Gotham,_ [_available wherever you get your pods_](https://open.spotify.com/show/30ThmaUENe9hTGo00YLFyl?si=b77d14aa019c4a22) _. If you want to support them,_ [_you can head to their Patreon_](https://www.patreon.com/xOwnGoals) _._

[Read More](https://www.americansocceranalysis.com/home/2026/3/10/2026-nwsl-previews-washington-spirit-gotham-fc)

_Our 2026 NWSL Season Previews have started and today we hit Portland and KC.. If you want to support this coverage of the league,_ [_you can head to our Patreon_](https://www.patreon.com/americansocceranalysis) _. For $5 a month you can get access to a lot of the data visualization tools we use to make these previews._

_If you’re more of an audio person, our friends at Expected Own Goals spoke to Phuoc Nguyen from Stumptown Footy to talk Portland, and Cindy Lara from the KC Sports Journal on the Current,_ [_available wherever you get your pods_](https://open.spotify.com/show/30ThmaUENe9hTGo00YLFyl?si=b77d14aa019c4a22) _. If you want to support them,_ [_you can head to their Patreon_](https://www.patreon.com/xOwnGoals) _._

[Read More](https://www.americansocceranalysis.com/home/2026/3/10/2026-nwsl-previews-portland-thorns-kc-current)

_Our 2026 NWSL Season Previews have started and today we hit Seattle and Orlando. If you want to support this coverage of the league,_ [_you can head to our Patreon_](https://www.patreon.com/americansocceranalysis) _. For $5 a month you can get access to a lot of the data visualization tools we use to make these previews._

_If you’re more of an audio person, our friends at Expected Own Goals spoke to Kari Anderson from Yahoo about the Reign, and Abigail Segel from The XI and Defector about Orlando,_ [_available wherever you get your pods_](https://open.spotify.com/show/30ThmaUENe9hTGo00YLFyl?si=b77d14aa019c4a22) _. If you want to support them,_ [_you can head to their Patreon_](https://www.patreon.com/xOwnGoals) _._

[Read More](https://www.americansocceranalysis.com/home/2026/3/9/2026-nwsl-previews-seattle-reign-orlando-pride)

0items

$0