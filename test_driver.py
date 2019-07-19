from OWLPy import Driver

# Initialise the Driver
d = Driver()


print("Testing Player Functions")
# Test: Player should be of type Player
from OWLPy import Player
player = d.get_player_by_id(id=3987)
assert str(type(player)) == "<class 'OWLPy.objects.Player'>"


from OWLPy import Player
player = d.get_player_by_name(name="SoOn")
assert str(type(player)) == "<class 'OWLPy.objects.Player'>"

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
assert (player.formattedName()) == "T. Tarlier (A.K.A SoOn)", "The first player should have been T. Tarlier (A.K.A SoOn) but was {}".format(player.formattedName())


print("All Player Tests passed")

print("Testing Team Functions")
# Test: Player should be of type Player
from OWLPy import Team
team = d.get_team_by_id(id=4523)
assert str(type(team)) == "<class 'OWLPy.objects.Team'>"


from OWLPy import Team
team = d.get_team_by_name(name="Dallas Fuel")
assert str(type(team)) == "<class 'OWLPy.objects.Team'>"

# # Test: Graceful Error if player is not found
# player = d.get_player_by_id(id=6657789)
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.PlayerNotFound'>"

# player = d.get_team_by_name(name="Sydney Sharks")
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.TeamNotFound'>"


# TEST: Get SoOn by player ID 3987
team = d.get_team_by_id(id=4523)
assert player.id == 3987, "The player ID should be 3987 but was {}".format(player.id)

# TEST: Player Soon should have a function formatted name
team = d.get_team_by_id(id=4523)
player = team.players[0]
assert len(player.formattedName()) >= 11, "Players formatted name should be".format(player.formattedName())

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