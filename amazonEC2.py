import TheTvDbEpisode
import nextEpisode
import sys
import json
from datetime import datetime

sendMessage = "Here are the series airing today (ET).\n"
episodeToday = False
myFavouries = TheTvDbEpisode.getMyFavorites()
token = TheTvDbEpisode.authenticate()
todaysDate = datetime.now().date()

for series in myFavouries:
    seriesName = TheTvDbEpisode.getSeriesName(series)
    seriesNameFormatted = nextEpisode.tvShowURL(seriesName)
    latestEpisodes = nextEpisode.previousNext(seriesNameFormatted)
    later = latestEpisodes["nextEpisode"]
    nextAirDate = later["airDate"]
    if nextAirDate:
        nextAirDateFormatted = datetime.strptime(nextAirDate[0], '%a %b %d, %Y').date()
        if nextAirDateFormatted == todaysDate:
            episodeToday = True
            sendMessage += str(seriesName) + ": " + str(later["countDown"][0]) + '\n'

if episodeToday:
    TheTvDbEpisode.sendSMS(sendMessage)
else:
    TheTvDbEpisode.sendSMS("No series airing today")
