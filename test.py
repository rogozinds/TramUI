from bs4 import BeautifulSoup
import PyQt5
import requests
import sys
from PyQt5 import QtWidgets

ASIN="B00AR9HWZ0"
DOMPATH = "FOO"
URL = "https://rogozin.integ.amazon.com/dp/B00AR9HWZ0"
#URL ="https://google.com"
def checkFeatures(asin, domPath):
    url = URL+asin
    #connect to url
    #the certificate is not specified
    #path="/Users/rogozin/PycharmProjects/test/mysite.pem"
    site = requests.get(URL, verify=False)
    dom = BeautifulSoup(site.text,"html.parser")
    body = dom.find("body")

    elem = body.find(None,{"id":"qpeTitleTag_feature_div"})
    elem2 = body.select("#qpeTitleTag_feature_div")
    if(elem==None):
        return "No Element"
    else:
        return elem.text

foo = checkFeatures(ASIN,DOMPATH)
print(foo)