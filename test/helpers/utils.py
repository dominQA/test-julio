import json
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Utils:

    def __init__(self):
        self.driver = None

    @staticmethod
    def open_url_json(route):
        """
        Open the json that is in the route passed by parameter.
        :param route:
        :return url:
        """
        url_json = "../settings/files/data.json"
        with open(url_json) as file:
            data = json.load(file)
        url = data['paths_and_urls'][route]
        return url

    @staticmethod
    def save_report(data):
        """
        Saves a txt report when executing the api exercise.
        :param data:
        :return:
        """
        url_api_txt = "../../../settings/files/reports_api/report.txt"
        with open(url_api_txt, 'a') as file:
            file.write(data + "\n")

    def click_button(self, name):
        """
        Clicks on a button with the name passed by parameter.
        :param name:
        :return:
        """
        btn__search = self.driver.find_element(By.XPATH, f"//*[text()='{name}']")
        btn__search.click()
        time.sleep(1)

    @staticmethod
    def scroll_until_present(self, xpath):
        """
        Scrolls until the element is present in the web. xpath locator is passed by parameter.
        :param xpath:
        :param self:
        :return element:
        """
        element = None
        max_scrolls = 5
        scroll_height = self.driver.execute_script("return window.innerHeight")
        for i in range(max_scrolls):
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_height)
            time.sleep(2)
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                break
            except NoSuchElementException:
                pass
        return element
