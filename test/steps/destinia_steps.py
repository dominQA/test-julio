from selenium import webdriver
from behave import *
from selenium.webdriver.chrome.options import Options
from src.POM.Pages.web_exercise.po_destinia_result import DestiniaResult
from src.POM.Pages.web_exercise.po_destinia import DestiniaHome
from src.POM.Pages.web_exercise.po_hotel import Hotel
from test.helpers.utils import Utils


@step("access the web application '{url_name}'")
def step_access_web_application(context, url_name):
    """
    This step accesses the web application url passed by parameter.
    Example:
        Given access the web application 'url_destinia'
    :param url_name:
    :param context:
    :return:
    """
    options = Options()
    # options.add_argument("--headless")
    context.driver = webdriver.Chrome(Utils.open_url_json("path_chrome_driver"), options=options)
    context.driver.maximize_window()
    context.driver.get(Utils.open_url_json(url_name))


@step("fill in the search fields")
def step_fill_search_fields(self):
    """
    This step fills the search fields to perform the corresponding search.
    Example:
        When fill in the search fields
    :return:
    """
    self.destinia_home_page = DestiniaHome(self.driver)
    self.destinia_home_page.search_accomodation(self.driver, "Madrid")


@step("click on '{button_name}' button")
def step_click_button_by_name(self, button_name):
    """
    This step clicks on a button which has the text passed by parameter.
    Example:
        And click on 'Buscar' button
    :param self:
    :param button_name:
    :return:
    """
    Utils.click_button(self, button_name)


@step("filter results and choose the cheapest hotel")
def step_filter_results_choose_cheapest(self):
    """
    This step filters the results by the cheapest hotels, selecting the first result.
    Example:
        And filter results and choose the cheapest hotel
    :return:
    """
    po_result = DestiniaResult(self.driver)
    po_result.get_economic_results()


@step("verify the accommodation description")
def step_verify_accommodation_description(self):
    """
    This step verifies the hotel description and takes a screenshot.
    Example:
        Then verify the accommodation description
    :return:
    """
    po_hotel = Hotel(self.driver)
    po_hotel.search_description()
