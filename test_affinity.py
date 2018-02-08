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

    #Test content of the QPE Title Tag
    def test_qpe_title_tag(self):
        qpeTitleElem = self.body.find_element_by_id("qpeTitleTag_feature_div")
        actual = qpeTitleElem.text
        expectedContent = "Amazon'a özel cep telefonu fırsatlarını buradan keşfedin."
        asin = "B01BTZFM0W"
        self.assertEqual(actual,expectedContent, f"ASIN {asin} has wrong qpeTitle Value. exp {expectedContent}, actual {actual} ")

    #Test features bullets has 5 or more items
    def test_feature_bullets_is_not_empty(self):
        elem = self.body.find_element_by_id("featurebullets_feature_div")
        contentList = elem.find_elements_by_css_selector("li")
        expectedNElements= 5;
        self.assertGreaterEqual(len(contentList),expectedNElements, f"The feature bullets should have at least {expectedNElements} items")


    # test image block has non empty images
    def test_image_block_alt_images_are_not_empty(self):
        elem = self.body.find_element_by_id("imageBlock_feature_div")
        contentList = elem.find_elements_by_id("altImages")

        self.assertGreater(len(contentList),0, "altImages size should be more  than 0")
        images = contentList[0].find_elements_by_css_selector("img");
        self.assertGreater(len(images), 0, "There should be more than 0 images in altImages.")
        expectedWidth = 10
        #for some reason first element has 0x0 size, excluding it.
        for image in images[1:len(images)]:
            width = image.size['width'];
            self.assertGreaterEqual(width, expectedWidth, f"Image size should be bigger than {expectedWidth}")

suite = unittest.TestLoader().loadTestsFromTestCase(QpeTest)
unittest.TextTestRunner(verbosity=2).run(suite)
