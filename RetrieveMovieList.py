import urllib2
from BeautifulSoup import BeautifulSoup
import datetime

def findDate():
    """Finds the current month for use in building the URL. Uses system time."""
    
    thisMonth = datetime.datetime.now().strftime("%m")

    if thisMonth == 1:
        thisMonth = "january"
    elif thisMonth == 2:
        thisMonth = "february"
    elif thisMonth == 3:
        thisMonth = "march"
    elif thisMonth == 4:
        thisMonth = "april"
    elif thisMonth == 10:
        thisMonth = "october"
    elif thisMonth == 11:
        thisMonth = "november"
    elif thisMonth == 12:
        thisMonth = "december"
    else:
        thisMonth = "break"
        
    return thisMonth

def scraper(month):
    """Gets the movie list, formats it, and returns it as a tuple. More work needs to be done for special cases."""

    page = urllib2.urlopen("http://temple.edu/mcpb/thereel/" + month + ".html")
    soup = BeautifulSoup(page)
    movie1 = str(soup.find('div', id="rightbodyevents").findAll('p')[0])
    movie1 = movie1[4:-4].split('<br />')
    movie1[0] = movie1[0].strip()
    movie1[1] = movie1[1].strip()
    print movie1
    
    movie2 = str(soup.find('div', id="movie3").findAll('p')[0])
    movie2 = movie2[4:-4].split('<br />')
    movie2[0] = movie2[0].strip()
    movie2[1] = movie2[1].strip()
    print movie2
    
    movie3 = str(soup.find('div', id="movie2").findAll('p')[0])
    movie3 = movie3[4:-4].split('<br />')
    movie3[0] = movie3[0].strip()
    movie3[1] = movie3[1].strip()
    print movie3
    
    movie4 = str(soup.find('div', id="movie4").findAll('p')[0])
    movie4 = movie4[4:-4].split('<br />')
    movie4[0] = movie4[0].strip()
    movie4[1] = movie4[1].strip()
    print movie4
    
    a = (movie1, movie2, movie3, movie4) #THIS IS WHERE I REACHED ENLIGHTENMENT
    
    return a

month = findDate()

month = "april" #For debugging purposes



