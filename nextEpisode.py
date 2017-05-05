from urllib2 import *
from bs4 import BeautifulSoup as bs

def tvShowURL(tvShow):
    """
    Takes name of TV show as input and returns a formatted string
    which can be directly plugged into a URL
    """
    tvShow = tvShow.lower()
    tvShow = tvShow.replace(' ', '-')
    return tvShow

tvShow = raw_input("Enter TV show name: ")
tvShow = tvShowURL(tvShow)

url = "http://next-episode.net/" + tvShow
try:
    request = Request(url)
    response = urlopen(request)
    page = response.read()
    soup = bs(page, 'html.parser')

    previousEpisode = soup.find('div', {'id': 'previous_episode'}).text
    previousEpisode = previousEpisode.replace('Summary:Episode Summary', '')\
                      .replace('\t', '').replace('\n\n', '\n')
    previousEpisode = previousEpisode.strip()

    nextEpisode = soup.find('div', {'id': 'next_episode'}).text
    nextEpisode = nextEpisode.replace('Summary:Episode Summary', '')\
                  .replace('\t', '').replace('\n\n', '\n')
    nextEpisode = nextEpisode.strip()

    print previousEpisode
    print
    print nextEpisode

except HTTPError:
    print "Sorry, we could not find the TV series you were looking for! :("
