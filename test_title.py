from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import base_test

#Tests
class TitleTest(base_test.BaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = self.base_url + "/dp/B01BTZFM0W"
        self.addWeblab('DP_PINFO_TITLE_REARCH_111070:T1')

    # def test_no_title(self):
    #     actual = self.body.find_element_by_id("title_feature_div").text
    #     expectedContent = ""
    #     asin = "B01BTZFM0W"
    #     self.assertEqual(actual,expectedContent, "ASIN {asin} has wrong qpeTitle Value. exp {expectedContent}, actual {actual} ".format(asin=asin, expectedContent=expectedContent, actual=actual))

    def test_title(self):
        actual = self.body.find_element_by_id("title_feature_div").text
        expectedContent = "Samsung Galaxy S7 akıllı telefon, 5,1 inç (12,9 cm) dokunmatik ekran, 32 GB dahili hafıza, Android OS, siyah., 32 GB, Siyah"
        asin = "B01BTZFM0W"
        self.assertEqual(actual, expectedContent, "ASIN {asin} has wrong qpeTitle Value. exp {expectedContent}, actual {actual} ".format(asin=asin, expectedContent=expectedContent, actual=actual))

suite = unittest.TestLoader().loadTestsFromTestCase(TitleTest)
unittest.TextTestRunner(verbosity=2).run(suite)
