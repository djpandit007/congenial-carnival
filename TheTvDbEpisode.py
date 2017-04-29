import requests
import json
import sys
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
        print "Fetched API Key"
        return {"apikey": apiKey, "username": userName, "userkey": userKey}
    except IOError:
        print "The file with API key not found!"

def isError(responseObj):
    # Returns True if there is an error, False otherwise
    if responseObj.ok and responseObj.status_code == 200:
        return False
    elif responseObj.status_code == 401:
        print "Authentication failure. The program will now quit"
        return True
    else:
        print "There has been an unexpected error. The program will now quit"
        return True

def authenticate():
    # Authenticates credentials are returns JWT token as unicode
    data = getCredentials()
    response = requests.post(APIURL + "/login", json=data)
    if isError(response):
        sys.exit()
    else:
        token = json.loads(response.content)["token"]
        print "JWT Token Generated successfully"
    return token

def getMyFavorites():
    # Returns the IDs of my favorite series
    token = authenticate()
    authorization = {"Authorization" : "Bearer " + token}
    userFav = requests.get(APIURL + "/user/favorites", headers=authorization)
    if isError(userFav):
        sys.exit()
    else:
        favorites = json.loads(userFav.content)["data"]["favorites"]
        print "Fetched my favorite series successfully"
    return favorites
