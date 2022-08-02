from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time


s = HTMLSession()

url = "https://www.olx.pl/nieruchomosci/"





r = s.get(url)
soup = BeautifulSoup(r.content,'html.parser')

for offer in soup.find_all('div',class_='offer-wrapper'):
    footer = offer.find ('td', class_='bottom-cell')
    location = footer.find('small', class_='breadcrumb').get_text().strip().split(',')[0]
    print(location)

#print(getdata(url))




