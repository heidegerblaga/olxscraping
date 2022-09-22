from bs4 import BeautifulSoup
from requests import get
from getdata import getdata
from nextpage import nextpage

def getlinks(link):
    url = link
    page = get(url)
    bs = BeautifulSoup(page.content,'html.parser')



    for offer in bs.find_all('div' ,class_="css-19ucd76"):
      footer = offer.find(class_="css-1bbgabe", href=True)
      if (footer != None):
        if (('olx' not in (footer['href']))and('otodom' not in (footer['href']))):
         new = 'https://www.olx.pl' + footer['href']
         getdata(new)


    getlinks(nextpage(link))



 #  print("\n")















