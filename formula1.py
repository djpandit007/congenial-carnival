import urllib2
from bs4 import BeautifulSoup as bs

calendarURL = "https://www.formula1.com/en/championship/races/2016.html"
raceURL = "https://www.formula1.com/en/results.html/2016/races.html"
driversURL = "https://www.formula1.com/en/championship/results/2016-driver-standings.html"
constructorsURL = "https://www.formula1.com/en/championship/results/2016-constructor-standings.html"

request = urllib2.Request(calendarURL)
response = urllib2.urlopen(request)
page = response.read()
calendarSoup = bs(page, 'html.parser')

request = urllib2.Request(raceURL)
response = urllib2.urlopen(request)
page = response.read()
raceSoup = bs(page, 'html.parser')

request = urllib2.Request(driversURL)
response = urllib2.urlopen(request)
page = response.read()
driverSoup = bs(page, 'html.parser')

request = urllib2.Request(constructorsURL)
response = urllib2.urlopen(request)
page = response.read()
constructorSoup = bs(page, 'html.parser')
