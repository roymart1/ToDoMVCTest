from selenium.webdriver.remote.webdriver import WebDriver

class PageObjectBase:

    def __init__(self, driver : WebDriver):
        self.driver = driver