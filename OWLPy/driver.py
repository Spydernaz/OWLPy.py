import requests
from fuzzywuzzy import fuzz
from OWLPy.objects import Player, Team, Match
from OWLPy.errors import *

class Driver(object):
    """An Object for controlling API functions"""
    def __init__(self):
        self.baseurl = "https://api.overwatchleague.com/"
    
    # Acquire Players
    def get_player_by_id(self, id): 
        r = requests.get("{}/player/{}".format(self.baseurl, id)).json()["data"]["player"]
        return Player(**r)

    def get_player_by_name(self, name): 
        r = requests.get("{}/players".format(self.baseurl)).json()["content"]
        player = None
        score = 0
        id = None
        for p in r:
            predict = fuzz.token_set_ratio(p["name"].lower(),name.lower())
            if p["name"].lower() == name.lower():
                player = self.get_player_by_id(p["id"])
                return player
            elif (predict > score):
                id = p["id"]
                score = predict
        if score > 80:
            return self.get_player_by_id(id)

        raise PlayerNotFound()


    # Acquire Teams
    def get_team_by_id(self, id):
        r = requests.get("{}/v2/teams/{}".format(self.baseurl, id)).json()["data"]
        return Team(**r)

    def get_team_by_name(self, name):
        r = requests.get("{}/v2/teams".format(self.baseurl)).json()["data"]
        team = None
        score = 0
        id = None
        for t in r:
            predict = fuzz.token_set_ratio(t["name"].lower(),name.lower())
            if t["name"].lower() == name.lower():
                team = self.get_team_by_id(t["id"])
                return team
            elif (predict > score):
                id = t["id"]
                score = predict
        if score > 80:
            return self.get_team_by_id(id)

        raise TeamNotFound()

    
    # Acquire Players
    def get_match_by_id(self, id): 
        r = requests.get("{}/match/{}".format(self.baseurl, id)).json()
        return Match(**r)

    def get_match_by_name(self, name): 
        r = requests.get("{}/players".format(self.baseurl)).json()["content"]
        for m in r:
            if m["name"] == name:
                return Match(**m)
        raise MatchNotFound()

    def get_next_match():
        """gets the next match to be played by any team"""
        pass

    def get_schedule(self, team):
        """gets the schedule for a team"""
        pass

    def get_next_round(self):
        """shows all games to be played in the next round, if you mid round it will return the current round"""
        pass
