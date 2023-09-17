import json

from requests import Response
from selenium.webdriver.remote.webdriver import WebDriver

from api.status_codes import StatusCodes
from scheme.schema_user import ListUsersResponse
from tests.web.locators import MainLocators
from web.pages.main import MainPage


class TestGetListUsersWeb:

    def test_get_list_users_web(self, driver: WebDriver, get_list_users: Response):
        main_page = MainPage(driver)
        main_page.open_url()
        main_page.click_by_element(MainLocators.GET_LIST_USERS)
        main_page.wait_text_to_be_present_in_element(locator=MainLocators.RESPONSE_FRAME, text='{')
        web_text = main_page.find_element(MainLocators.RESPONSE_FRAME).text
        web_text_status_code = main_page.find_element(MainLocators.STATUS_CODE).text
        api_text = get_list_users.json()
        assert web_text_status_code == '200', \
            f'Статус код {web_text_status_code} не совпадает с ожидаемым - {StatusCodes.STATUS_200}'
        assert ListUsersResponse(**json.loads(web_text)) == ListUsersResponse(**api_text)
