from selenium.webdriver.remote.webdriver import WebDriver

from api.status_codes import StatusCodes
from tests.web.locators import MainLocators
from web.pages.main import MainPage


class TestDeleteUserWeb:

    def test_delete_user_web(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_url()
        main_page.click_by_element(MainLocators.DELETE_DELETE)
        main_page.wait_text_to_be_present_in_element(locator=MainLocators.STATUS_CODE, text='204')
        web_text = main_page.find_element(MainLocators.STATUS_CODE).text
        assert web_text == '204', f'Статус код {web_text} не совпадает с ожидаемым - {StatusCodes.STATUS_204}'
