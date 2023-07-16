import time
from test.helpers.utils import Utils


class Hotel:

    def __init__(self, driver):
        self.driver = driver
        self.txt__hotel_description_XPATH = "//div[@id='hotel_description']"
        self.txt__hotel_description = None

    def search_description(self):
        """
        Search for the hotel description in the web page.
        :return:
        """
        self.txt__hotel_description = Utils.scroll_until_present(self, self.txt__hotel_description_XPATH)
        self.txt__hotel_description.screenshot(Utils.open_url_json("path_save_screenshot"))
        print("Taking screenshot of the hotel description... \nScreenshot saved in 'settings > files > output'.")
        time.sleep(3)
