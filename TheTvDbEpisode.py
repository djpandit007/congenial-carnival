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

def authenticate():
    # Authenticates credentials are returns JWT token
    data = getCredentials()
    response = requests.post(APIURL + "/login", json=data)
    if response.status_code == 401:
        print "Authentication failure. The program will now quit"
        sys.exit()
    elif response.ok and response.status_code == 200:
        token = json.loads(response.content)["token"]
        print "JWT Token Generated successfully"
    else:
        print "There has been an unexpected error. The program will now quit"
        sys.exit() 
    return token


authenticate()
