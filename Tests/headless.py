import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",default="chrome")
    parser.addoption("--env", default="dev") #action is not mandetory
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")  # Custom option for headless mode

@pytest.fixture(scope="function")
def setup2(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")  ################################### Get the --headless option
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()   #####################################
        if headless:
            chrome_options.add_argument("headless")  ################################### Enable headless mode if --headless is passed
        driver = webdriver.Chrome(options=chrome_options) ###################################

    yield driver

"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)
"""