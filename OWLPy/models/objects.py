import requests

class Account(object):
    """Overwatch League teams and players each have their social media accounts for interacting with fans. Each Account object has an account ID, an account type, and an account URL."""
    def __init__(self, id, type, url):
        self.id = id
        self.type = type
        self.url = url
    
    def _getlatestpost():
        pass

class Blog(object):
    def __init__(self, blodId, created, updated, publish, title, author, \
                locale, keywords, summary, commentKey, status, thumbnail, \
                defaultCommunity, defaultUrl, commentsEnabled, pollAttached, \
                localizationPublish, siteCategory):
        """A Blog is where articles pertaining to Overwatch League are located. Each Blog covers topics including player news, match summaries, team updates, and more."""
        self.blogId = blogId
        self.created = created
        self.updated = updated
        self.publish = publish
        self.title = title
        self.author = author
        self.locale = locale
        self.keywords = keywords
        self.summary = summary,
        self.commentKey = commentKey,
        self.status = status,
        self.thumbnail = thumbnail,
        self.defaultCommunity = defaultCommunity
        self.defaultUrl = defaultUrl
        self.commentsEnabled = commentsEnabled
        self.pollAttached = pollAttached
        self.localizationPublish = localizationPublish
        self.siteCategory = siteCategory
    

class Bracket(object):
    pass

class Colors(object):
    def __init__(self, primary, secondary, tertiary):
        self.primary = primary
        self.secondary = secondary
        self.tertiary = tertiary

class Competitor(object):
    def __init__(self, id, availableLanguages, homeLocation, addressCountry, \
                game, handle, name, abbreviatedName, \
                primaryColor, secondaryColor, logo, icon, secondaryPhoto, \
                players, attributes, attributesVersion, type, \
                website=None, placement=None, advantage=None, ranking=None, schedule=None, aboutUrl=None, \
                description=None, accounts=None, location=None):
        """Model for a competitor/team and associated information"""
        self.id = id
        self.availableLanguages = availableLanguages
        self.handle = handle
        self.name = name
        self.abbreviatedName = abbreviatedName
        self.logo = logo
        # self.hasFallback = hasFallback
        self.location = location
        self.players = []
        for p in players:
            #self.players.append(d.get_player(p["player"]["id"]))
            #self.players.append(Player(**p))
            pass
        self.accounts = []
        if accounts is not None:
            for a in accounts:
                pass
                #self.accounts.append(Account(**a))
        self.website = website
        self.placement = placement
        self.advantage = advantage
        #self.records = Records(records)
    pass


class Team(Competitor):
    def __init__(self, id, availableLanguages, homeLocation, addressCountry, \
                game, handle, name, abbreviatedName, \
                primaryColor, secondaryColor, logo, icon, secondaryPhoto, \
                players, attributes, attributesVersion, type, \
                website=None, placement=None, advantage=None, ranking=None, schedule=None, aboutUrl=None, \
                description=None, accounts=None, location=None):
        """Model for a competitor/team and associated information"""
        # d = Driver()
        self.id = id
        self.availableLanguages = availableLanguages
        self.handle = handle
        self.name = name
        self.abbreviatedName = abbreviatedName
        self.logo = logo
        # self.hasFallback = hasFallback
        self.location = location
        self.players = []
        for p in players:
            # self.players.append(d.get_player(p["id"]))
            #self.players.append(Player(**p))
            pass
        self.accounts = []
        if accounts is not None:
            for a in accounts:
                pass
                #self.accounts.append(Account(**a))
        self.website = website
        self.placement = placement
        self.advantage = advantage
        #self.records = Records(records)
    pass

class Game(object):
    pass

class Gamemode(object):
    pass

class Livematch(object):
    pass

class Logo(object):
    pass

class Match(object):
    pass

class Nextmatch(object):
    pass

class Player(object):
    def __init__(self, id, availableLanguages, handle, name, homeLocation, accounts, \
                game, attributes, attributesVersion, familyName, givenName, \
                nationality, headshot, type, teams):
        """A Player is a member of a competing Overwatch League team"""
        self.id = id
        self.availableLanguages = availableLanguages
        self.handle = handle
        self.name = name
        self.homeLocation = homeLocation
        self.accounts = accounts
        self.game = game
        self.attributes = attributes
        self.attributesVersion = attributesVersion
        self.familyName = familyName
        self.givenName = givenName
        self.nationality = nationality
        self.headshot = headshot
        self.teams = teams
        self.type = type
    
    def formatedName(self):
        return("{}. {} (A.K.A {})".format(self.givenName[0], self.familyName, self.name))


class Records(object):
    def __init__(self, matchWin, matchLoss, matchDraw, matchBye, \
                gameWin, gameLoss, gameTie, gamePointsFor, gamePointsAgainst, \
                comparisons):
        """Records maintain information about a Team's statistics"""
        self.matchWin = matchWin
        self.matchLoss = matchLoss
        self.matchDraw = matchDraw
        self.matchBye = matchBye
        self.gameWin = gameWin
        self.gameLoss = gameLoss
        self.gameTie = gameTie
        self.gamePointsFor = gamePointsFor
        self.gamePointsAgainst = gamePointsAgainst
        self.comparisons = comparisons
        

class VOD(object):
    pass
