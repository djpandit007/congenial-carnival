def getAPIKey():
    # Returns the secret API Key as string
    try:
        apiFile = open("API Key.txt", "r")
        apiKey = apiFile.readline()
        assert apiKey != "", "Invalid API Key"
        apiFile.close()
        print "Fetched API Key"
        return apiKey
    except IOError:
        print "The file with API key not found!"

getAPIKey()
