"""Модуль главной страницы"""
from selenium.webdriver.remote.webdriver import WebDriver

from web.pages.base import BasePage


class MainPage(BasePage):
    """Класс главной страницы"""
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url='https://reqres.in/')
