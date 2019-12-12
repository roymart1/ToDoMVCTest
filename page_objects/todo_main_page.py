from page_objects.page_object_base import PageObjectBase


class TodoMainPage(PageObjectBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.__page_title_rid = ".0.0.0"

    def validate_main_title(self):
        we_title = self.driver.find_element_by_xpath(f".//h1[@data-reactid='{self.__page_title_rid}']")
        print("The title is --> " + we_title.text)




