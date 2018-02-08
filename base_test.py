from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
# content is coming from content  symphony
# https://symphony.integ.amazon.com/creatives/56e9361d-7488-44da-a887-1d587c0b817c

#Tests
#testQPETag(ASIN_TO_CONTENT)
class BaseTest(unittest.TestCase):

    def openPage(self, url):
        SERVICE_ARGS = ['--ignore-ssl-errors=true', '--ssl-protocol=any']
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        # emulate userAgent as OPF will return empty webpage for "bots"
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
            "(KHTML, like Gecko) Chrome/15.0.87"
        )
        driver = webdriver.PhantomJS(service_args=SERVICE_ARGS, desired_capabilities=dcap)
        driver.set_window_size(1024, 768)  # optional
        driver.get(url)
        if len(driver.find_elements_by_tag_name("body")[0].find_elements_by_tag_name("div")) == 0:
            raise AssertionError("The body of the page has no divs ")
        return driver

    #Method of the parent class, that will be called before run test
    def setUp(self):
        self.driver = self.openPage(self.url)

    def tearDown(self):
        # self.driver.save_screenshot("screen.png")
        self.driver.quit()
