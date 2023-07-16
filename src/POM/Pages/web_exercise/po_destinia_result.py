import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class DestiniaResult:

    def __init__(self, driver):
        self.driver = driver
        self.lnk__economic = None
        self.lnk__first_result = None
        self.economic_xpath = "//a[text()='Más  económicos']"

    def get_economic_results(self):
        """
        Order the web results by the cheapest first.
        :return:
        """
        try:
            self.lnk__economic = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.economic_xpath)))
            time.sleep(8)
            self.lnk__economic.click()
        except Exception:
            print("* Web element could not be found.")
        time.sleep(5)
        self.lnk__first_result = self.driver.find_element(By.XPATH, "(//a[@class='dst-select-hotel'])[1]")
        self.lnk__first_result.click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_windows = self.driver.window_handles
        self.driver.switch_to.window(new_windows[1])
        time.sleep(2)
