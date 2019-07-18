import requests
from OWLPy import models

# Competitor Tests
competitor_dict = requests.get("https://api.overwatchleague.com/matches/20301").json()["competitors"][0]
competitor = models.Competitor(**competitor_dict)
assert competitor.id == 4409, "The Competitor of this game should be Seoul Dynasty"
print ("all Competitor tests completed sucessfully")

# Team Tests
team_dict = requests.get("https://api.overwatchleague.com/team/7694").json()
team = models.Team(**team_dict)
assert team.id == 7694, "The Team should have the id 7694 (Paris Eternal) but was {}".format(team.id)
print ("all Team tests completed sucessfully")

# Player Tests
player_dict = requests.get("https://api.overwatchleague.com/players/3380").json()["data"]["player"]
player = models.Player(**player_dict)
assert (player.id) == 3380, "Player ID should be the same as the requested player"
assert (player.formatedName()) == "T. Kettunen (A.K.A Taimou)"


print ("all Player tests completed sucessfully")