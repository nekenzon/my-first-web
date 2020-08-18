from selenium import webdriver
import unittest

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_get_to_the_url_correct(self):

        #functional testing
        self.browser.get('http://localhost:8000/cv')

        #Title testing
        self.assertIn('QIHONGLIANG BLOG', self.browser.title)

        #head element testing
        head = self.browser.find_element_by_tag_name('td').text
        self.assertEqual('Objective Job',head)





if __name__ == '__main__':
    unittest.main(warnings='ignore')
