import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.HomePageObject import HomePageObject
from datapages.HomePageData import HomePageData

@pytest.fixture(params = HomePageData.Home_page_data)
def getdata(request):
    return request.param

def test_one(setup, getdata):
    driver = setup
    homepage = HomePageObject(driver)
    title = homepage.get_title()
    print(title)
    homepage.search_veggie(getdata["search_by_text"])
    print (getdata["veggie_name"])
    homepage.add_product(getdata["veggie_name"])
    time.sleep(3)

@pytest.mark.ab
def test_two_three(setup2):
    driver=setup2
    print("i'm test no.2")












"""
def test(setup):
    driver=setup
    homepage = HomePageObject(driver)
    homepage.search_veggie("ber")
    products = driver.find_elements(By.XPATH, "//div[@class= 'product']")
    for product in products:
        names = product.find_element(By.XPATH, ".//h4[@class= 'product-name']").text
        name = names.split('-')[0].strip()
        print(name)
        if name == "Strawberry":
            product.find_element(By.XPATH, "./div[3]/button").click()

        time.sleep(3)"""

