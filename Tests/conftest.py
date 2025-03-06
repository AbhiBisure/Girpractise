import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",default="chrome")
    parser.addoption("--env", default="dev") #action is not mandetory

@pytest.fixture( scope="function" )
def setup(request):
    browser_name = request.config.getoption( "browser_name" )
    if browser_name == "chrome" :
        driver = webdriver.Chrome()
    elif browser_name == "firefox" :
        driver = webdriver.Firefox()

    environment = request.config.getoption("--env")
    if environment == 'dev':
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    elif environment == 'QA':
        driver.get("https://getawaygogo.com")
        print("getaway gogo is opened")

    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.close()



