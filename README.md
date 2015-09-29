# lolatmyteam
League of Legends Perl-CGI Application [02.2015]

**ATTENTION**
As of September 2X, 2015, the Riot API has removed the MatchHistory API that I used to build this application, therefore running my code will result in only a partially correct output. I plan on revising the website, however will not be able to upload it to Matrix until December 2015 when I can re-claim my Matrix account

Web application tool used to display ranked player statistics. Using this application, you can get an understanding of a certain player's strengths and weaknesses.

The input into this webpage is the player's summoner name. The only condition for the input is that the player must have played at least one ranked game this season, otherwise it will not return any data. Additionally, because the page is so new and fragile, I'm not sure how it will handle if the player has played <10 ranked games and not been given a tier/division rank.

If using the multi search page, please do not hit the search button more than once. Additionally, the program will take about 20 seconds to load the data because of the amount of data being requested to the Riot API servers. I will be applying for a new development key once this webpage is refined, in hopes of receiving a higher data transfer limit.

Currently hosted on the Seneca matrix SGE cluster.

Links:

http://matrix.senecac.on.ca/~apmacdonald/lolatmyteam.cgi
http://matrix.senecac.on.ca/~apmacdonald/lolatmyteam_multi.cgi

To test (if you do not play League of Legends, or do not meet the input requirements), use my summoner name: Norifurikake.
