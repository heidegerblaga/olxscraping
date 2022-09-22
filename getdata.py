from bs4 import BeautifulSoup
from requests import get
from models import (Base, session,
                    Crawler, engine)




def cleardata(data):

     clean = []


     clean.append(float(data[0].split('zł')[0].strip().replace(' ','')))
     clean.append(int(data[1][1].strip()))
     clean.append(data[2][0].strip())
     clean.append(float(data[3][1].split('zł')[0].strip()))
     clean.append(data[4][1].strip())
     clean.append(float(data[5][1].split('m²')[0].strip().replace(' ','').replace(',','.')))
     clean.append(float(data[6][1].split('m²')[0].strip().replace(' ','').replace(',','.')))
     clean.append(data[7][1].strip())


     return clean



def getdata(link,location):
     url = link
     page = get(url)
     bs = BeautifulSoup(page.content, 'html.parser')


     price = bs.find(class_="css-okktvh-Text eu5v0x0").get_text()
     id = bs.find(class_="css-9xy3gn-Text eu5v0x0").get_text().split(':')



     content = []
     content.append(price)
     content.append(id)

     tabel = bs.find_all('li', class_="css-ox1ptj")

     for i in range(0,len(tabel)-1):
          content.append(tabel[i].find(class_="css-xl6fe0-Text").get_text().split(':'))


     data=cleardata(content)




     session.add(Crawler(property=data[2],location=location,price=data[0],metrprice=data[3],market=data[4],area=data[5],plotarea=data[6],building=data[7],offerid=data[1]))
     session.commit()


