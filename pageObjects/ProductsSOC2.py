from selenium.webdriver.common.by import By


class ProductsSOC2:

    def __init__(self, driver):
        self.driver = driver

    drata_nav = (By.XPATH, "//div[@data-id='af082b9']//a[@href='https://drata.com']")

    def go_home(self):
        self.driver.find_element(*ProductsSOC2.drata_nav).click()

    h_soc2_comp = (By.XPATH, "//h1[contains(text(), 'SOC 2')]")

    def check_h_soc2_comp(self):
        return self.driver.find_element(*ProductsSOC2.h_soc2_comp)
