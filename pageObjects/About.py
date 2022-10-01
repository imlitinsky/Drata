from selenium.webdriver.common.by import By


class About:

    def __init__(self, driver):
        self.driver = driver

    drata_nav = (By.XPATH, "//div[@data-id='c3e4b4f']//a[@href='https://drata.com']")

    def go_home(self):
        self.driver.find_element(*About.drata_nav).click()
        #return self.driver.find_element(*About.drata_nav)

    about_drata = (By.XPATH, "//h2[contains(text(),'About Drata')]")

    def check_about_drata(self):
        return self.driver.find_element(*About.about_drata)
