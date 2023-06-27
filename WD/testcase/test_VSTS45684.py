import time
import pytest
from selenium.webdriver.common.by import By

from common.baseFun import BaseFun
from pages.Administration import AdministrationPage


def test_user_exit_runtest_nochange(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Expand User Exit and select Barcode Scanning
    browser.find_element(By.XPATH, "//div[text()='User Exits']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Barcode Scanning']").click()
    time.sleep(3)
    # 3.Select  script row  without change
    browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].click()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].clear()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].send_keys("LEFT(Barcode,1) = \"~\"")
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[1].click()
    time.sleep(5)
    commit = browser.find_element(By.XPATH, "//button[text() ='Commit User Exit']")
    if commit.is_enabled():
        commit.click()
        # Check Commit successfully
        assert "Commit User Exit Success" in BaseFun(browser).get_AlterMessage()
    browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].click()
    time.sleep(3)
    # 4.input test value and run test
    value = browser.find_element(By.XPATH, "//input[@class='TextBox_Style']")
    value.send_keys("~")
    test = browser.find_element(By.XPATH, "//button[text() ='Run Test']")
    test.click()
    time.sleep(3)
    # check test result
    result = browser.find_element(By.XPATH, "//div[text()='Results:']/../../td[3]/div")
    assert "Test result:Yes" == result.text


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS45684.py"])
