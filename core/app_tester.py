import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from core.ctx import CTX
from page_objects.todo_main_page import TodoMainPage


class AppTester:

    def __init__(self):
        pass

    def init_driver(self, url):
        """
        Initialize the required web driver used for testing

        :param url: initial navigation url
        :type url: str
        :type url: str
        :return: the webdriver to be use for the test
        :rtype: WebDriver
        """
        driver = webdriver.Chrome()
        CTX.driver =  driver
        driver.get(url)
        return driver


if __name__ == '__main__':
    app = AppTester()
    drv = app.init_driver("http://todomvc.com/examples/react/#/")
    main_window = TodoMainPage(drv)
    main_window.validate_main_title()

    time.sleep(10)
    drv.quit()
