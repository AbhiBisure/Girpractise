from selenium.webdriver.common.by import By
from utils.utilities import BrowserUtils

class HomePageObject(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.title = (By.CLASS_NAME,"brand")
        self.search =(By.XPATH,"// input[ @ type = 'search']")
        self.products=(By.XPATH, "//div[@class= 'product']")
        self.product_name=(By.XPATH, ".//h4[@class= 'product-name']")
        self.cart_button = (By.XPATH, "./div[3]/button")

    def get_title(self):
        utilities = BrowserUtils(self.driver)
        utilities.wait_for_element("// input[ @ type = 'search']")
        element =self.driver.find_element(*self.title)
        return element.text

    def search_veggie(self,text):
        self.driver.find_element(*self.search).send_keys(text)

    def add_product(self,veggie):
        products = self.driver.find_elements(*self.products)

        for product in products:
            names= product.find_element(*self.product_name).text
            name = names.split('-')[0].strip()
            print(name)
            if name == veggie:
                product.find_element(*self.cart_button).click()


