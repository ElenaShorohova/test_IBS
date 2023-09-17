from selenium.webdriver.remote.webdriver import WebDriver

from api.status_codes import StatusCodes
from tests.web.locators import MainLocators
from web.pages.main import MainPage


class TestResourceNotFoundWeb:

    def test_resource_not_found_web(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_url()
        main_page.click_by_element(MainLocators.GET_SINGLE_RESOURCE_NOT_FOUND)
        main_page.wait_text_to_be_present_in_element(locator=MainLocators.RESPONSE_FRAME, text='{')
        web_text = main_page.find_element(MainLocators.RESPONSE_FRAME).text
        web_text_status_code = main_page.find_element(MainLocators.STATUS_CODE).text
        assert web_text_status_code == '404', \
            f'Статус код {web_text_status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_404}'
        assert web_text == '{}'
