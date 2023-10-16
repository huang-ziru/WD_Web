# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from common.baseFun import BaseFun
from pages.Administration import AdministrationPage


def test_print_picture(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Select Permissions
    browser.find_element(By.XPATH, "//div[text()='Printing']").click()
    time.sleep(3)
    # 3.Choose picture
    Customer_name = browser.find_element(By.XPATH, "//input[@class='TextBox_String_Style']")
    Customer_name.clear()
    random_str = BaseFun(browser).Random_Str(5)
    name = "test name "+random_str
    Customer_name.send_keys(name)
    Customer_name.send_keys(Keys.ENTER)
    time.sleep(5)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 4.Check picture upload success
    browser.find_element(By.XPATH, "//a[text()='Refresh']").click()
    time.sleep(5)
    Customer_name_new = browser.find_element(By.XPATH, "//input[@class='TextBox_String_Style']").get_attribute('value')
    assert Customer_name_new == name


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41378.py"])
