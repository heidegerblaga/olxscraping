from bs4 import BeautifulSoup
from requests import get


url = 'https://www.olx.pl/nieruchomosci/'

page = get(url)

bs = BeautifulSoup(page.content,'html.parser')


for offer in bs.find_all('div' ,class_='css-19ucd76'):



  footer = offer.find("p", class_="css-p6wsjo-Text eu5v0x0")
  if (footer != None):
   location =  footer.get_text().split("-")[0]
   print(location)
   print("\n")


 #print(location)





