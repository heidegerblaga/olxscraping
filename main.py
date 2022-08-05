from bs4 import BeautifulSoup
from requests import get


url = 'https://www.olx.pl/d/nieruchomosci/domy/sprzedaz/'

page = get(url)

bs = BeautifulSoup(page.content,'html.parser')

lc = []

for offer in bs.find_all('div' ,class_='css-19ucd76'):

  footer = offer.find("p", class_="css-p6wsjo-Text eu5v0x0")

  if (footer != None):
   location =  footer.get_text().split("-")[0]
   lc.append(location)

   print("\n")

   price = offer.find('p',class_='css-wpfvmn-Text eu5v0x0').get_text().strip().split('do negocjacji')[0]
   title = offer.find('h6', class_="css-v3vynn-Text eu5v0x0").get_text()

   print(title)
   print("%s - %s "%(location,price))














