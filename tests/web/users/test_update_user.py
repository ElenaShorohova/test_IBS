import json

from selenium.webdriver.remote.webdriver import WebDriver

from api.status_codes import StatusCodes
from scheme.schema_user import UpdateUserResponse
from tests.web.locators import MainLocators
from web.pages.main import MainPage


class TestUpdateUserWeb:

    def test_full_update_user_web(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_url()
        main_page.click_by_element(MainLocators.PUT_UPDATE)
        main_page.wait_text_to_be_present_in_element(locator=MainLocators.RESPONSE_FRAME, text='{')
        web_text = main_page.find_element(MainLocators.RESPONSE_FRAME).text
        web_text_status_code = main_page.find_element(MainLocators.STATUS_CODE).text
        UpdateUserResponse.model_validate(json.loads(web_text))
        assert web_text_status_code == '200', \
            f'Статус код {web_text_status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'

    def test_update_user_web(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_url()
        main_page.click_by_element(MainLocators.PATCH_UPDATE)
        main_page.wait_text_to_be_present_in_element(locator=MainLocators.RESPONSE_FRAME, text='{')
        web_text = main_page.find_element(MainLocators.RESPONSE_FRAME).text
        web_text_status_code = main_page.find_element(MainLocators.STATUS_CODE).text
        UpdateUserResponse.model_validate(json.loads(web_text))
        assert web_text_status_code == '200', \
            f'Статус код {web_text_status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
