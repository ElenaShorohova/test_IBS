from selenium.webdriver.common.by import By


class MainLocators:
    """Класс локаторов главной страницы"""

    GET_LIST_USERS = (By.XPATH, '//*[@data-id="users"]')
    GET_SINGLE_USER = (By.XPATH, '//*[@data-id="users-single"]')
    GET_SINGLE_NOT_FOUND = (By.XPATH, '//*[@data-id="users-single-not-found"]')
    GET_LIST_RESOURCE = (By.XPATH, '//*[@data-id="unknown"]')
    GET_SINGLE_RESOURCE = (By.XPATH, '//*[@data-id="unknown-single"]')
    GET_SINGLE_RESOURCE_NOT_FOUND = (By.XPATH, '//*[@data-id="unknown-single-not-found"]')
    POST_CREATE = (By.XPATH, '//*[@data-id="post"]')
    PUT_UPDATE = (By.XPATH, '//*[@data-id="put"]')
    PATCH_UPDATE = (By.XPATH, '//*[@data-id="patch"]')
    DELETE_DELETE = (By.XPATH, '//*[@data-id="delete"]')
    POST_REGISTER_SUCCESSFUL = (By.XPATH, '//*[@data-id="register-successful"]')
    POST_REGISTER_UNSUCCESSFUL = (By.XPATH, '//*[@data-id="register-unsuccessful"]')
    POST_LOGIN_SUCCESSFUL = (By.XPATH, '//*[@data-id="login-successful"]')
    POST_LOGIN_UNSUCCESSFUL = (By.XPATH, '//*[@data-id="login-unsuccessful"]')
    GET_DELAYED_RESPONSE = (By.XPATH, '//*[@data-id="delay"]')
    RESPONSE_FRAME = (By.XPATH, '//*[@data-key="output-response"]')
    STATUS_CODE = (By.XPATH, '//*[@data-key="response-code"]')
