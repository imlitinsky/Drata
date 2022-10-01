from selenium.webdriver.common.by import By


class Demo:

    def __init__(self, driver):
        self.driver = driver

    schedule_demo = (By.XPATH, "//h1[contains(text(), 'Schedule a Demo')]")

    def check_schedule_demo(self):
        return self.driver.find_element(*Demo.schedule_demo)

    first_name = (By.XPATH, "//input[@name='firstname']")

    def check_first_name(self):
        return self.driver.find_element(*Demo.first_name)
