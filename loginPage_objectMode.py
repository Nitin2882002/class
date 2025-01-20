import time
import pytest
from selenium import webdriver
from loginPageObjectModel import login

class TestLogin:
    def test_login(self):
        print("hello")
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(5)
        driver.maximize_window()
        lp=login(driver)
        lp.setUserName("aniketnbhnabha@gmail.com")
        lp.setUserPasswrd("Nabha@123")
        time.sleep(2)
        lp.button()
        act_title=driver.title
        assert act_title=="My account - My Shop"