import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from locators.locator import login
from locators.locator import logout
from locators.locator import dashbaord

class loginpage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('login.url')
        # from webdriver_manager.core import driver
        self.driver.find_element(By.ID,'login.username_boxid').send_keys('Admin')
        self.driver.find_element(By.ID,'login.password_boxid').send_keys('admin123')
        self.driver.find_element(By.ID,'login.login_clickbox').click()
        time.sleep(2)

        time.sleep(5)
    def test_login(self):
        #from webdriver_manager.core import driver
        value=self.driver.find_element(By.ID,'login.welcome').text
        result='Welcome German'
        self.assertNotEqual(result,value,'congratulation')
        time.sleep(4)
    def test_logout(self):
        self.driver.find_element(By.XPATH,'logout.forlogout').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'logout.logoutposition').click()

    def test_forgetpass(self):
        # from webdriver_manager.core import driver
        self.driver.find_element(By.XPATH,'login.email_forget').click()
       #self.driver.find_element(By.ID,'securityAuthentication_userName').send_keys('anit@mail.com')
        cancel=self.driver.find_element(By.ID,'login.cancel_boxid')
        print(cancel.is_selected())
        print(cancel.is_enabled())
        time.sleep(4)

    def test_dashboard(self):
        time.sleep(2)
        # from webdriver_manager.core import driver
        self.driver.find_element(By.XPATH,'assigneleave_box').click()
        self.driver.find_element(By.ID,'employeename_boxid').send_keys('anit upreti')
        self.driver.find_element(By.XPATH,'leavetype_box').click()
        self.driver.find_element(By.ID,'assignleave_txtComment').send_keys('this is an emergency case')
        self.driver.find_element(By.ID,'assignBtn').click()
        time.sleep(4)
   #assignleave_txtComment
    def tearDown(self) -> None:
        self.driver.close()
