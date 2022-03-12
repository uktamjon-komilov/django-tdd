from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path="C:\Program Files (x86)\chromedriver.exe"
        )
    
    def tearDown(self) -> None:
        self.browser.close()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Madina has heard about a cool new online to-do app. She goes
        # to check its home page
        self.browser.get("http://localhost:8000")
        
        # She notices the page title and header mention 'to-do lists'
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")


if __name__ == "__main__":
    unittest.main(warnings="ignore")