import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener

class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        filename = driver.current_url.replace('https://tr-pre-prod.amazon.com/', '').replace('/', '_')
        screenshot_name = self.test_name + '_' + filename + '.png'
        driver.get_screenshot_as_file(screenshot_name)
        print("Screenshot saved as '%s'" % screenshot_name)

class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        SERVICE_ARGS = ['--ignore-ssl-errors=true', '--ssl-protocol=any']
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        # emulate userAgent as OPF will return empty webpage for "bots"
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
            "(KHTML, like Gecko) Chrome/15.0.87"
        )
        driver = webdriver.PhantomJS(service_args=SERVICE_ARGS, desired_capabilities=dcap)
        self.error_listener = ScreenshotListener()
        self.driver = EventFiringWebDriver(driver, self.error_listener)
        self.driver.set_window_size(1024, 768)  # optional
        self.url = "https://tr-pre-prod.amazon.com/dp/B01BTZFM0W"

    def addWeblab(self, weblab):
        self.driver.add_cookie({
            'name': 'experiment',
            'value': weblab,
            'domain': '.amazon.com',
            'path': '/'
        })

    #Method of the parent class, that will be called before run test
    def setUp(self):
        self.error_listener.test_name = self._testMethodName
        self.driver.get(self.url)
        if len(self.driver.find_elements_by_tag_name("body")[0].find_elements_by_tag_name("div")) == 0:
            raise AssertionError("The body of the page has no divs ")
        else:
            self.body = self.driver.find_elements_by_tag_name("body")[0]

    def tearDown(self):
        # self.driver.save_screenshot("screen.png")
        self.driver.quit()
