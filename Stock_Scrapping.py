import requests
import bs4

def getStockValue(keyword):
    res= requests.get("https://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/index.html")
    soup=bs4.BeautifulSoup(res.text,'lxml')
    searchArray=soup.find_all(string=keyword)
    tr=searchArray[0].find_parents('tr')
    tdArray=tr[0].select('td')
    return tdArray[1].find_all(text=True)[0]

lastPrice=getStockValue('Axis Bank')
print(lastPrice)