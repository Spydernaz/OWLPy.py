import requests
from OWLPy import models

competitor_dict = requests.get("https://api.overwatchleague.com/matches/20301").json()["competitors"][0]

competitor = models.Competitor(**competitor_dict)

assert competitor.id == 4409, "The Competitor of this game should be Seoul Dynasty"


team_dict = requests.get("https://api.overwatchleague.com/team/7694").json()
print(team_dict["players"][0].keys())

team = models.Team(**team_dict)

assert team.id == 7694, "The Team should have the id 7694 (Paris Eternal) but was {}".format(team.id)
assert (team.players[0].formattedName()) == "T. Tarlier (A.K.A SoOn)", "The first player should have been T. Tarlier (A.K.A SoOn) but was {}".format(team.players[0].formattedName())

print ("all tests completed sucessfully")