c = {"data":{"records": {
    "matchWin": 1,
    "matchLoss": 1,
    "matchDraw": 0,
    "matchBye": 0,
    "gameWin": 3,
    "gameLoss": 5,
    "gameTie": 0,
    "gamePointsFor": 0,
    "gamePointsAgainst": 0,
    "comparisons": [
        {
            "key": "MATCH_DIFFERENTIAL",
            "value": 0
        },
        {
            "key": "MATCH_GAME_DIFFERENTIAL",
            "value": -2
        },
        {
            "key": "GAME_HEAD_TO_HEAD_DIFFERENTIAL",
            "value": None
        },
        {
            "key": "MATCH_HEAD_TO_HEAD_DIFFERENTIAL",
            "value": None
        },
        {
            "key": "ADVANTAGE",
            "value": 0
        }
    ]
}
}
}


from OWLPy import models

competitor = models.Records(**c["data"]["records"])