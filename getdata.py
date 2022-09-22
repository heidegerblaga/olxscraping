from bs4 import BeautifulSoup
from requests import get
from models import (Base, session,
                    Crawler, engine)




def getdata(link):
     url = link
     page = get(url)
     bs = BeautifulSoup(page.content, 'html.parser')
     price = bs.find(class_="css-okktvh-Text eu5v0x0")
     tabel = bs.find_all('li',class_="css-ox1ptj")
     content = []
     for i in range(0,len(tabel)-1):
          content.append(tabel[i].find(class_="css-xl6fe0-Text").get_text().split(':'))
     print(content)
     content[1][1]

     id = bs.find(class_="css-9xy3gn-Text eu5v0x0").get_text().split(':')

     area=int(content[3][1].split(' ')[1])
     plotarea = int(content[4][1].split(' ')[1])

     print(area)

     #session.add(Crawler(property=content[0],price=price,metrprice=content[1][1],market=content[2][1]),area=area,plotarea=plotarea,building=content[5][1],offerid=id)

     session.commit()


