# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.baseFun import BaseFun
from pages.Administration import AdministrationPage


def test_permission_modify(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.go to permission
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(3)
    # select user role
    select = Select(browser.find_element(By.XPATH, "//select[@class='gwt-ListBox']"))
    select.select_by_value("Production Execution Administrator")
    time.sleep(3)
    # don't check out the Administrations-permission modify
    browser.find_element(By.XPATH, "//div[text()='Permissions' and @class='gwt-Label']/../../td[2]//input").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(3)
    # Check apply error
    text = "Invalid configuration.  At least one role must have the Modify-Permissions permission."
    assert text in BaseFun(browser).get_AlterMessage()
    time.sleep(3)
    # 3. refresh and check current role is displaying
    browser.find_element(By.XPATH, "//a[text()='Refresh']").click()
    time.sleep(3)
    select = Select(browser.find_element(By.XPATH, "//select[@class='gwt-ListBox']"))
    role = select.first_selected_option.text
    assert "Production Execution Administrator" == role


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS29638.py"])

