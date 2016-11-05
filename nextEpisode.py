import urllib2
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
request = urllib2.Request(url)
response = urllib2.urlopen(request)
page = response.read()
soup = bs(page, 'html.parser')

previousEpisode = soup.find('div', {'id': 'previous_episode'})

nextEpisode = soup.find('div', {'id': 'next_episode'})


print previousEpisode.text.strip()
print
print nextEpisode.text.strip()
