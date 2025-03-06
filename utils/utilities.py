import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver
        
    def wait_for_element(self,locator):
        wait = WebDriverWait(self.driver,3)
        print("test*******************************")
        return wait.until(EC.presence_of_element_located((By.XPATH,locator)))









    """def setup_logger(name):
        logger = logging.getLogger(name)
        filehandler=logging.filehandler("logfile.log")
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger"""


