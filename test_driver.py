from OWLPy import Driver

# Initialise the Driver
d = Driver()


print("Testing Player Functions")
# Test: Player should be of type Player
from OWLPy import Player
player = d.get_player_by_id(id=3987)
assert str(type(player)) == "<class 'OWLPy.objects.Player'>"


from OWLPy import Player
player = d.get_player_by_name(name="cruise")
assert str(type(player)) == "<class 'OWLPy.objects.Player'>"
assert player.name == "Kruise", "Failed, got {} instead of Kruise".format(player.name)

from OWLPy import Player
player = d.get_player_by_name(name="soon")
assert str(type(player)) == "<class 'OWLPy.objects.Player'>"
assert player.name == "SoOn"

# SoOn should play for the Paris Eternal
from OWLPy import Player
player = d.get_player_by_name(name="soon")
assert str(type(player)) == "<class 'OWLPy.objects.Player'>"
assert player.get_team().name == "Paris Eternal"

# # Test: Graceful Error if player is not found
# player = d.get_player_by_id(id=6657789)
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.PlayerNotFound'>"

# player = d.get_player_by_name(name="SooooooooN")
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.PlayerNotFound'>"


# TEST: Get SoOn by player ID 3987
player = d.get_player_by_id(id=3987)
assert player.id == 3987, "The player ID should be 3987 but was {}".format(player.id)

# TEST: Player Soon should have a function formatted name
player = d.get_player_by_id(id=3987)
assert (player.formatted_name()) == "T. Tarlier (A.K.A SoOn)", "The first player should have been T. Tarlier (A.K.A SoOn) but was {}".format(player.formatted_name())


print("All Player Tests passed")

print("Testing Team Functions")
# Test: Team should be of type Team
from OWLPy import Team
team = d.get_team_by_id(id=4523)
assert str(type(team)) == "<class 'OWLPy.objects.Team'>"

# Exact match
from OWLPy import Team
team = d.get_team_by_name(name="Paris")
assert str(type(team)) == "<class 'OWLPy.objects.Team'>"
assert team.name == "Paris Eternal"

# Partial match works 
from OWLPy import Team
team = d.get_team_by_name(name="Gladiators")
assert str(type(team)) == "<class 'OWLPy.objects.Team'>"
assert team.name == "Los Angeles Gladiators"

# Fuzzy match works 
from OWLPy import Team
team = d.get_team_by_name(name="san fransico shock")
assert str(type(team)) == "<class 'OWLPy.objects.Team'>"
assert team.name == "San Francisco Shock"

# # Test: Graceful Error if player is not found
# player = d.get_player_by_id(id=6657789)
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.PlayerNotFound'>"

# player = d.get_team_by_name(name="Sydney Sharks")
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.TeamNotFound'>"


# TEST: Get SoOn by player ID 3987
# team = d.get_team_by_id(id=4523)
# assert player.id == 3987, "The player ID should be 3987 but was {}".format(player.id)

# TEST: Player Soon should have a function formatted name
# team = d.get_team_by_id(id=4523)
# player = team.players[0]
# assert len(player.formatted_name()) >= 11, "Players formatted name should be".format(player.formatted_name())

print("All Team Tests passed")


print("Testing Match Functions")
# Test: Player should be of type Player
from OWLPy import Match
match = d.get_match_by_id(id=20301)
assert str(type(match)) == "<class 'OWLPy.objects.Match'>"


# from OWLPy import Match
# team = d.get_team_by_name(name="Dallas Fuel")
# assert str(type(team)) == "<class 'OWLPy.objects.Team'>"

# # Test: Graceful Error if player is not found
# player = d.get_player_by_id(id=6657789)
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.PlayerNotFound'>"

# player = d.get_team_by_name(name="Sydney Sharks")
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.TeamNotFound'>"


# # TEST: Get SoOn by player ID 3987
# team = d.get_team_by_id(id=4523)
# assert player.id == 3987, "The player ID should be 3987 but was {}".format(player.id)

# # TEST: Player Soon should have a function formatted name
# team = d.get_team_by_id(id=4523)
# player = team.players[0]
# assert len(player.formattedName()) >= 11, "Players formatted name should be".format(player.formattedName())

print("All Match Tests passed")