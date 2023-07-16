import random
from datetime import datetime, timedelta
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.helpers.utils import Utils


def select_date(self):
    """
    Select arrival and departure date.
    """
    date_execution = datetime.now().date()
    date_arrival = date_execution + timedelta(days=4)
    date_departure = date_arrival + timedelta(days=3)
    time.sleep(1)
    self.input__arrival_date.click()
    time.sleep(1)
    day_arrival = str(date_arrival.day)
    select_arrival = self.driver.find_element(By.XPATH, f"//span[@class='flatpickr-day ' and text()='{day_arrival}']")
    select_arrival.click()
    time.sleep(1)

    day_departure = str(date_departure.day)
    select_departure = self.driver.find_element(By.XPATH, f"//span[@class='flatpickr-day ' and text()='{day_departure}']")
    select_departure.click()
    time.sleep(1)


def select_children(self):
    """
    Select number of children (under 18 years old) older than 2 years old.
    """
    self.btn__occupation.click()
    btn__more_children = self.driver.find_element(By.XPATH, self.btn__more_children_xpath)
    time.sleep(1)
    btn__more_children.click()
    time.sleep(1)

    num_random = random.randint(3, 17)
    select__elmt = self.driver.find_element(By.XPATH, "//select[contains(@class,'searchAddAge__select')]")
    select = Select(select__elmt)
    select.select_by_value(str(num_random))
    time.sleep(1)
    Utils.click_button(self, "Hecho")


class DestiniaHome:

    def __init__(self, driver):
        self.driver = driver
        self.btn__cookies_xpath = "//button[contains(text(),'Aceptar')]"
        self.txt__search_city = self.driver.find_element(By.XPATH,
                                                         "(//input[contains(@placeholder,'Ciudad, zona, hotel')])[1]")
        self.input__arrival_date = self.driver.find_element(By.XPATH, "(//label[text()='Entrada']/parent::div)[1]")
        self.txt__departure_date = self.driver.find_element(By.XPATH,
                                                            "(//label[text()='Salida']/following-sibling::input[contains(@placeholder,'Elegir fecha')])[1]")
        self.btn__occupation = self.driver.find_element(By.XPATH,
                                                        "(//label[text()='Ocupación']/following-sibling::button)[1]")
        self.btn__more_children_xpath = "(//button[contains(@class,'searchCounter__btn--plus')])[2]"

    def search_accomodation(self, driver, city_name):
        """
        Searchs the city passed by parameter.
        :param city_name:
        :param driver:
        :return:
        """
        try:
            btn_accept_cookies = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.btn__cookies_xpath)))
            btn_accept_cookies.click()
        except TimeoutException as ex:
            print("* Web element could not be found. Error message --> " + ex.msg)
        self.txt__search_city.clear()
        self.txt__search_city.send_keys(city_name)
        time.sleep(1)
        self.txt__search_city.send_keys(Keys.DOWN)
        self.txt__search_city.send_keys(Keys.ENTER)
        time.sleep(1)
        select_date(self)
        select_children(self)
