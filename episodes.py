import TheTvDbEpisode
import nextEpisode
import sys
import json

choice = ''
crendentialsValid = False

print "Enter 1 to show next episodes of all favourite series."
print "Enter 2 to show next episode of a specific series."
while choice != "1" and choice != "2":
    choice = raw_input("Enter your choice: ")

if choice == "1":
    # Print info for all favourite series
    pass
elif choice == "2":
    # Print info for specific series
    seriesName = raw_input("Enter the name of the TV Series: ")
    seriesNameFormatted = nextEpisode.tvShowURL(seriesName)
    token = TheTvDbEpisode.authenticate()
    crendentialsValid = True
    details = TheTvDbEpisode.seriesInfo(seriesName)
    if not details:
        print "No series called " + seriesName + " found. The program will now quit."
        sys.exit()
    detailsData = json.loads(details.content)["data"][0]
    print "%s : %s. It first aired on %s on %s. Overview: %s" % (detailsData["seriesName"], detailsData["status"], detailsData["network"], detailsData["firstAired"], detailsData["overview"])
    seriesId = detailsData["id"]
    latestEpisodes = nextEpisode.previousNext(seriesNameFormatted)
    previous = latestEpisodes["previousEpisode"]
    later = latestEpisodes["nextEpisode"]
    previousOverview = TheTvDbEpisode.getEpisodeOverview(seriesId, previous["season"], previous["episode"])
    latestOverview = TheTvDbEpisode.getEpisodeOverview(seriesId, later["season"], later["episode"])
    print
    print previous["text"]
    print "Summary: " + previousOverview
    print
    print later["text"]
    print "Summary: " + latestOverview
