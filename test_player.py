import requests
from OWLPy import models
player_dict = requests.get("https://api.overwatchleague.com/players/3380").json()["data"]["player"]


player = models.Player(**player_dict)


assert (player.id) == 3380, "Player ID should be the same as the requested player"
assert (player.formatedName()) == "T. Kettunen (A.K.A Taimou)"


print ("all tests completed sucessfully")