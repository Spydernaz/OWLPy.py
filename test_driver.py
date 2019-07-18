from OWLPy import Driver

# Initialise the Driver
d = Driver()


print("Testing Player Functions")
# Test: Player should be of type Player
from OWLPy.models import Player
player = d.get_player_by_id(id=3987)
assert str(type(player)) == "<class 'OWLPy.models.objects.Player'>"

from OWLPy.models import Player
player = d.get_player_by_name(name="SoOn")
assert str(type(player)) == "<class 'OWLPy.models.objects.Player'>"

# # Test: Graceful Error if player is not found
# player = d.get_player_by_id(id=6657789)
# assert str(type(player)) == "<class 'OWLPy.errors.customerrors.PlayerNotFound'>"

player = d.get_player_by_name(name="SooooooooN")
assert str(type(player)) == "<class 'OWLPy.errors.customerrors.PlayerNotFound'>"


# TEST: Get SoOn by player ID 3987
player = d.get_player_by_id(id=3987)
assert player.id == 3987, "The player ID should be 3987 but was {}".format(player.id)

# TEST: Player Soon should have a function formatted name
player = d.get_player_by_id(id=3987)
assert (player.formatedName()) == "T. Tarlier (A.K.A SoOn)", "The first player should have been T. Tarlier (A.K.A SoOn) but was {}".format(player.formatedName())


print("All tests passed")