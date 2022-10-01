import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Test set up

@pytest.fixture(scope="class")
def set_up(request):
    dc = DesiredCapabilities.CHROME
    dc['goog:loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=dc)
    driver.implicitly_wait(10)

    driver.get("https://drata.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


