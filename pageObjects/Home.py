from selenium.webdriver.common.by import By
from pageObjects.Demo import Demo
from pageObjects.About import About


class Home:

    def __init__(self, driver):
        self.driver = driver

    drata_nav = (By.XPATH, "//div[@data-id='af082b9']//a[@href='https://drata.com']")

    def go_home(self):
        self.driver.find_element(*Home.drata_nav).click()
        #return self.driver.find_element(*Home.drata_nav)

    start_nav = (By.XPATH, "//div[@data-id='5ab7cad']//span[contains(text(),'get started')]")

    def get_started(self):
        self.driver.find_element(*Home.start_nav).click()
        demo = Demo(self.driver)
        return demo
        #return self.driver.find_element(*Home.start_nav)

    company_nav = (By.XPATH, "//li[@class='nav-item companyHeaderLink']")

    def company(self):
        self.driver.find_element(*Home.company_nav).click()
        #return self.driver.find_element(*Home.company_nav)

    about_nav = (By.XPATH, "//a[@href='/about']")

    def about(self):
        self.driver.find_element(*Home.about_nav).click()
        about = About(self.driver)
        return about
        #return self.driver.find_element(*Home.about_nav)

    careers_nav = (By.XPATH, "//a[@href='/careers']")

    def careers(self):
        return self.driver.find_element(*Home.careers_nav)

    contact_nav = (By.XPATH, "//a[@href='/contact']")

    def contact(self):
        return self.driver.find_element(*Home.contact_nav)

    security_nav = (By.XPATH, "(//a[@href='/security'])[1]")

    def security(self):
        return self.driver.find_element(*Home.security_nav)


