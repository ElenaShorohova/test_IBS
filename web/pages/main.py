from web.pages.base import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url='https://reqres.in/')
        
