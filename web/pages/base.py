"""Модуль базовой страницы и методы для работы с ней."""
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Класс базовой страницы для работы с элементами"""
    url: str

    def __init__(self, driver: WebDriver, url: str):
        """

        Args:
            driver: WebDriver.
        """
        self.driver = driver
        self.url = url

    def driver(self) -> WebDriver:
        """Получить драйвер"""
        return self.driver

    def open_url(self):
        """Открыть страницу по url"""
        self.driver.get(self.url)

    def find_element(self, locator: tuple, timeout: int = 20) -> WebElement:
        """Ожидание элемента в DOM страницы.

        Args:
            locator: локатор
            timeout: Количество секунд до тайм-аута ожидания
        """
        try:
            element = WebDriverWait(driver=self.driver, timeout=timeout).until(
                method=EC.presence_of_element_located(locator=locator)
            )
            return element
        except TimeoutException as e:
            raise e

    def click_by_element(self, locator: tuple) -> None:
        """Кликнуть по элементу.

        Args:
            locator: локатор
        """
        self.find_element(locator=locator).click()

    def wait_text_to_be_present_in_element(self, locator: tuple, text: str) -> WebElement:
        """Ожидание элемента с текстом в DOM страницы.

        Args:
            locator: локатор
            text: Текст элемента
        """
        try:
            element = WebDriverWait(driver=self.driver, timeout=10).until(
                method=EC.text_to_be_present_in_element(locator=locator, text_=text)
            )
            return element
        except TimeoutException as e:
            raise e
