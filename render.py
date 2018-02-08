import sys
import PyQt5
import requests
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Render(QtWebEngineWidgets.QWebEnginePage):
    def __init__(self, url):
        self.app = QtWidgets.QApplication(sys.argv)
        QtWebEngineWidgets.QWebEnginePage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.load(QUrl(url))
        self.toPlainText(self._lambda)
        self.toHtml(self._lambda)
        self.app.exec_()

    def _lambda(self, res):
        self.frame = res
    def _loadFinished(self, result):
      #  self.frame = self.mainFrame()
      self.toPlainText(self._lambda)
      self.app.quit()


url = 'http://www.theuselessweb.com/'
#This does the magic.Loads everything
r = Render(url)
#result is a QString.
result = r.frame
print(result)