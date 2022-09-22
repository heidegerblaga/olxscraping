from bs4 import BeautifulSoup
from requests import get
from getdata import getdata
from nextpage import nextpage

def getlinks(link):
    url = link
    page = get(url)
    bs = BeautifulSoup(page.content,'html.parser')


    i=-1
    for offer in bs.find_all('div' ,class_="css-19ucd76"):
      footer = offer.find(class_="css-1bbgabe", href=True)
      if (footer != None):
        if (('olx' not in (footer['href']))and('otodom' not in (footer['href']))):
         new = 'https://www.olx.pl' + footer['href']
         i+=1
         getdata(new,bs.find_all(class_="css-p6wsjo-Text eu5v0x0")[i].get_text().split('-')[0].strip())



    getlinks(nextpage(link))



 #  print("\n")















