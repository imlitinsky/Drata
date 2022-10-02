from selenium.webdriver.common.by import By


class SignIn:

    def __init__(self, driver):
        self.driver = driver

    drata_nav = (By.XPATH, "//a[@href='https://drata.com']")

    def go_home(self):
        self.driver.find_element(*SignIn.drata_nav).click()

    h_sign_in = (By.XPATH, "//h2[contains(text(),'Sign in')]")

    def check_sign_in_header(self):
        return self.driver.find_element(*SignIn.h_sign_in)

    l_sign_in_with_email = (By.XPATH, "//span[contains(text(),'Sign in with email')]")

    def check_sign_in_with_email(self):
        return self.driver.find_element(*SignIn.l_sign_in_with_email)

