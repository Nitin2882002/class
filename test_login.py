import time
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestClass:
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("login")
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.ID,"email").send_keys("aniketnbhnabha@gmail.com")
        driver.find_element(By.ID, "passwd").send_keys("Nabha@123")
        time.sleep(3)
        driver.find_element(By.ID, "SubmitLogin").click()
        try:
          text=driver.find_element(By.XPATH,'//*[@id="center_column"]/h1').text
          assert text=='MY ACCOUNT'
        except:
          driver.close()
          assert False



@allure.severity(allure.severity_level.MINOR)
@allure.feature("Display LOGO")
def test_login(self, setup):
        self.driver = setup
        logo=self.driver.find_element(By.XPATH,'//*[@id="header_logo"]/a/img').is_displayed
        self.driver.close()
        assert logo == True

 # pytest -v -s --alluredir="allure report\Reports" allure report\basics.py