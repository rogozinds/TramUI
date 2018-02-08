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

#Tests
#testQPETag(ASIN_TO_CONTENT)
class QpeTest(base_test.BaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = "https://tr-pre-prod.amazon.com/dp/B01BTZFM0W"

    def runTest(self):
        body = self.driver.find_elements_by_tag_name("body")[0]
        qpeTitleElem = body.find_element_by_id("qpeTitleTag_feature_div")
        actual = qpeTitleElem.text
        expectedContent = "foo"
        asin = "B01BTZFM0W"
        self.assertEqual(actual,expectedContent, f"ASIN {asin} has wrong qpeTitle Value. exp {expectedContent}, actual {actual} ")


suite = unittest.TestLoader().loadTestsFromTestCase(QpeTest)
unittest.TextTestRunner(verbosity=2).run(suite)