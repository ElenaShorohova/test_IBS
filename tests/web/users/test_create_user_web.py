import json

from selenium.webdriver.remote.webdriver import WebDriver

from api.status_codes import StatusCodes
from scheme.schema_user import CreateUserResponse
from tests.web.locators import MainLocators
from web.pages.main import MainPage


class TestCreateUserWeb:

    def test_create_user_web(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_url()
        main_page.click_by_element(MainLocators.POST_CREATE)
        main_page.wait_text_to_be_present_in_element(locator=MainLocators.RESPONSE_FRAME, text='{')
        web_text = main_page.find_element(MainLocators.RESPONSE_FRAME).text
        web_text_status_code = main_page.find_element(MainLocators.STATUS_CODE).text
        CreateUserResponse.model_validate(json.loads(web_text))
        assert web_text_status_code == '201', \
            f'Статус код {web_text_status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_201}'
