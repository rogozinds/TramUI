from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import base_test
# content is coming from content  symphony
# https://symphony.integ.amazon.com/creatives/56e9361d-7488-44da-a887-1d587c0b817c
DP_URL = 'https://tr-development.amazon.com/dp/'
ASIN_TO_CONTENT = {"B0014WJYOG": "Amazon'a özel cep telefonu fırsatlarını buradan keşfedin.",
                   "B0107NR9L2": "Amazon'a özel cep telefonu fırsatlarını buradan keşfedin3."
                   }


def openPage(url):
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
    if len(driver.find_elements_by_tag_name("body")[0].find_elements_by_tag_name("div"))==0:
        raise AssertionError("The body of the page has no divs ")
    return driver


def constructURL(base, asin):
    return base + asin


def testQPETag(asinToContent):
    for asin, expectedContent in asinToContent.items():
        driver = openPage(constructURL(DP_URL, asin))
        body =  driver.find_elements_by_tag_name("body")[0]
        qpeTitleElem = body.find_element_by_id("qpeTitleTag_feature_div")
        actual = qpeTitleElem.get_property("text")
        if actual != expectedContent:
            print(f"ASIN {asin} has wrong qpeTitle Value. exp {expectedContent}, actual {asinToContent} ")
            driver.save_screenshot(asin + ".png")
    print("Done! If this the only output everything is OK!")


#Tests
#testQPETag(ASIN_TO_CONTENT)
class QpeTest(base_test.BaseTest):
        # base_test.BaseTest.url = "https://tr-pre-prod.amazon.com/dp/B01BTZFM0W"


    def runTest(self):
        self.assertEqual('foo'.upper(), 'FObaO')


suite = unittest.TestLoader().loadTestsFromTestCase(QpeTest)
unittest.TextTestRunner(verbosity=2).run(suite)