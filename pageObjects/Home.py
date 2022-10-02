from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.Demo import Demo
from pageObjects.About import About
from pageObjects.ProductsSOC2 import ProductsSOC2
from pageObjects.SignIn import SignIn


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

    company_nav = (By.XPATH, "//li[@class='nav-item companyHeaderLink']")

    def company(self):
        self.driver.find_element(*Home.company_nav).click()

    products_nav = (By.XPATH, "//li[@class='nav-item']/a[contains(text(), 'Products')]")

    def products(self):
        a = ActionChains(self.driver)
        products = self.driver.find_element(*Home.products_nav)
        a.move_to_element(products).perform()

    soc2_nav = (By.XPATH, "//li[@class='nav-item']//a[@href='/soc-2']")

    def soc2(self):
        self.driver.find_element(*Home.soc2_nav).click()
        soc2 = ProductsSOC2(self.driver)
        return soc2

    sign_in_nav = (By.XPATH, "//div[@data-id='82c740d']//span[contains(text(),'Sign in')]")

    def sign_in(self):
        self.driver.find_element(*Home.sign_in_nav).click()
        sign_in = SignIn(self.driver)
        return sign_in

    about_nav = (By.XPATH, "//a[@href='/about']")

    def about(self):
        self.driver.find_element(*Home.about_nav).click()
        about = About(self.driver)
        return about

    careers_nav = (By.XPATH, "//a[@href='/careers']")

    def careers(self):
        return self.driver.find_element(*Home.careers_nav)

    contact_nav = (By.XPATH, "//a[@href='/contact']")

    def contact(self):
        return self.driver.find_element(*Home.contact_nav)

    security_nav = (By.XPATH, "(//a[@href='/security'])[1]")

    def security(self):
        return self.driver.find_element(*Home.security_nav)


