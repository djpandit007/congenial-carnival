import requests
import json
from pprint import pprint

APIURL = "https://api.thetvdb.com"

def getCredentials():
    # Returns dictionary with credentials
    try:
        credentials = open("credentials.txt", "r")
        apiKey = credentials.readline().strip()
        assert len(apiKey) == 16, "Invalid API Key"
        userName = credentials.readline().strip()
        assert len(userName) == 11, "Invalid username"
        userKey = credentials.readline().strip()
        assert len(userKey) == 16, "Invalid user key"
        credentials.close()
        return {"apikey": apiKey, "username": userName, "userkey": userKey}
    except IOError:
        print "The file with API key not found!"

def isError(responseObj):
    # Returns True if there is an error, False otherwise
    if responseObj.ok and responseObj.status_code == 200:
        return False
    elif responseObj.status_code == 401:
        print "Authentication failure"
        return True
    else:
        print "There has been an unexpected error"
        return True

def authenticate():
    """
    Authenticates credentials are returns JWT token as unicode
    Returns None if there is an error
    """
    data = getCredentials()
    response = requests.post(APIURL + "/login", json=data)
    if isError(response):
        return None
    else:
        token = json.loads(response.content)["token"]
    return token

def getMyFavorites():
    """
    Returns the IDs of my favorite series
    Returns None if error
    """
    token = authenticate()
    authorization = {"Authorization" : "Bearer " + token}
    userFav = requests.get(APIURL + "/user/favorites", headers=authorization)
    if isError(userFav):
        return None
    else:
        favorites = json.loads(userFav.content)["data"]["favorites"]
        print "Fetched my favorite series successfully"
    return favorites

def seriesInfo(seriesName):
    """
    Returns response object for 'seriesName'
    Returns None if error
    """
    token = authenticate()
    authorization = {"Authorization": "Bearer " + token}
    series = requests.get(APIURL + "/search/series", headers=authorization, params={"name": seriesName})
    if isError(series):
        return None
    return series

def getEpisodeOverview(seriesId, seasonNum, episodeNum):
    """
    Returns the overview of a particular episode of a season
    Returns None if error
    """
    token = authenticate()
    authorization = {"Authorization" : "Bearer " + token}
    episodeOverview = requests.get(APIURL + "/series/" + str(seriesId) + "/episodes/query", headers=authorization, params={"id": seriesId, "airedSeason": seasonNum, "airedEpisode" :episodeNum})
    if isError(episodeOverview):
        return None
    return json.loads(episodeOverview.content)["data"][0]["overview"]

def getSeriesName(seriesId):
    """
    Returns the name of the series, given its ID
    Returns None if error
    """
    token = authenticate()
    authorization = {"Authorization": "Bearer " + token}
    seriesName = requests.get(APIURL + "/series/" + str(seriesId), headers=authorization)
    if isError(seriesName):
        return None
    return json.loads(seriesName.content)["data"]["seriesName"]
