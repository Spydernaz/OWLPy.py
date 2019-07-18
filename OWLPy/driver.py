import requests
import OWLPy.models
import OWLPy.errors

class Driver(object):
    """An Object for controlling API functions"""
    def __init__(self):
        self.baseurl = "https://api.overwatchleague.com/"
    
    def test(self, route=None):
        return requests.get("{}/{}".format(self.baseurl, route))
    
    def get_player_by_id(self, id): 
        r = requests.get("{}/player/{}".format(self.baseurl, id)).json()["data"]["player"]
        return OWLPy.models.Player(**r)

    def get_player_by_name(self, name): 
        r = requests.get("{}/players".format(self.baseurl)).json()["content"]
        for p in r:
            if p["name"] == name:
                return OWLPy.models.Player(**p)
        raise OWLPy.errors.PlayerNotFound()