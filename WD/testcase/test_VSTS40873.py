# coding = utf-8
import configparser
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun
from pages.Administration import AdministrationPage


def test_no_permission(browser):
    # add corp\qaone to Production Execution User in AFW
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Select Permissions
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(3)
    # 3.Grant no permission for "Production Execution User"
    select = Select(browser.find_element(By.XPATH, "//select[@class='gwt-ListBox']"))
    select.select_by_value("Production Execution User")
    time.sleep(3)
    inputs = browser.find_elements(By.XPATH, "//input[@type ='checkbox']")
    for input in inputs:
        if input.is_selected():
            input.click()
            time.sleep(1)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    time.sleep(3)
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
        # Check apply successfully
        text = "Apply Permission Successful"
        assert text in BaseFun(browser).get_AlterMessage()
    # 4.Logout and login user, set a method
    browser.find_element(By.XPATH, "//div[text()='Logoff']").click()
    config = configparser.ConfigParser()
    path = r'..\data\config.ini'
    config.read(path)
    username = config.get('login', 'username2')
    password = config.get('login', 'password2')
    browser.find_element(By.XPATH, "//input[@class='gwt-TextBox']").send_keys(username)
    browser.find_element(By.XPATH, "//input[@class='gwt-PasswordTextBox']").send_keys(password)
    browser.find_element(By.XPATH, "//button[@class='Home_Login_Button']").click()
    time.sleep(5)
    # 5.Check user only has Home tab
    tabs = browser.find_elements(By.XPATH, "//div[@class='Tab_Label']")
    assert len(tabs) == 1, tabs[0].text == "Home"


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS40873.py"])
