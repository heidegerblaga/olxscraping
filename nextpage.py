from bs4 import BeautifulSoup
from requests import get
from getdata import getdata


def nextpage(link):
    url = link
    page = get(url)
    bs = BeautifulSoup(page.content, 'html.parser')
    pagination = bs.find(class_="css-4mw0p4")
    tabel = pagination.find('ul').find_all('a')
    button='https://www.olx.pl'+tabel[4]['href']

    return button
