import nflgame
from pprint import pprint
import operator
import urllib2
from BeautifulSoup import BeautifulSoup
import urllib

games = nflgame.games(2014, week=11)
players = nflgame.combine(games)

print "playerid,first_name,last_name,team,position,profile_url,profile_photo,uniform_number,weight,passing_yds,rushing_yds,receiving_yds,receiving_rec,passing_tds,rushing_tds,receiving_tds"

for p in players:
    if p.player.position == "WR" or p.player.position == "RB" or p.player.position == "QB" or p.player.position == "TE":
        html = urllib2.urlopen(p.player.profile_url).read()
        parsed_html = BeautifulSoup(html)
        profile_photo = parsed_html.body.find('div', attrs={'class':'player-photo'}).find('img')['src']
        urllib.urlretrieve(profile_photo, "src/images/players/" + p.playerid + ".png")
        print str(p.playerid) + "," + str(p.player.first_name) + "," + str(p.player.last_name) + "," + str(p.team) + "," + str(p.player.position) + "," + str(p.player.profile_url) + "," + profile_photo + "," + str(p.player.uniform_number) + "," + str(p.player.weight) + "," + str(p.passing_yds) + "," + str(p.rushing_yds) + "," + str(p.receiving_yds) + "," + str(p.receiving_rec) + "," + str(p.passing_tds) + "," + str(p.rushing_tds) + "," + str(p.receiving_tds)
