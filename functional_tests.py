from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_get_to_blog_and_verify_content(self):
        # Melissa has heard about a cool new blog. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention Ryan Renno
        self.assertIn('Ryan Renno', self.browser.title)
        #She notices the page title and header mention Ryan Renno
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Ryan Renno', header_text)        
        self.fail('Finish the test!')

        # She likes what she sees and leaves the site

if __name__ == '__main__':
    unittest.main(warnings='ignore') 
