from bs4 import BeautifulSoup
from requests import get
from getdata import getdata


url = 'https://www.olx.pl/d/nieruchomosci/domy/sprzedaz/'
page = get(url)
bs = BeautifulSoup(page.content,'html.parser')



for offer in bs.find_all('div' ,class_="css-19ucd76"):
  footer = offer.find(class_="css-1bbgabe", href=True)
  print('______________________')
  if (footer != None):
    if (('olx' not in (footer['href']))and('otodom' not in (footer['href']))):
       new = 'https://www.olx.pl' + footer['href']
       print(new)
       getdata(new)
    else:
      print(footer['href'])
      #getdata(footer['href'])
  print('[end]______________________')








  if (footer != None):
    location =  footer.get_text().split("-")[0]
    #print(location)


 #  print("\n")

  # price = offer.find('p',class_='css-wpfvmn-Text eu5v0x0').get_text().strip().split('do negocjacji')[0]
   #title = offer.find('h6', class_="css-v3vynn-Text eu5v0x0").get_text()
   #lc.append(location)
   #pr.append(price)
   #tl.append(title)

   #print("%s - %s "%(location,price))














