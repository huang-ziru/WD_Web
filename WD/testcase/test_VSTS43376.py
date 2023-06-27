# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from pages.Administration import AdministrationPage
from common.baseFun import BaseFun


def test_commit_user_exit(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Expand User Exit and select one option
    browser.find_element(By.XPATH, "//div[text()='User Exits']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Barcode Scanning']").click()
    time.sleep(3)
    # 3.Select last row to add script
    AdministrationPage(browser).add_script_user_exit()
    # browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[-1].click()
    # time.sleep(3)
    # browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[-1].send_keys("abc")
    # time.sleep(3)
    # browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[-1].click()
    # time.sleep(3)
    # # 4.Click Commit
    # browser.find_element(By.XPATH, "//button[text() ='Commit User Exit']").click()
    # time.sleep(3)
    # # Check Commit successfully
    # assert "Commit User Exit Success" in BaseFun(browser).get_AlterMessage()
    # 4.Input wrong scripts
    browser.find_elements(By.XPATH, "//input[@name ='Code_OnYes']")[-1].click()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_OnYes']")[-1].send_keys("yes")
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[-1].click()
    time.sleep(3)
    # Check Commit fail
    browser.find_element(By.XPATH, "//button[text() ='Commit User Exit']").click()
    time.sleep(3)
    message = BaseFun(browser).get_AlterMessage()
    print(message[0:57])
    assert "W1:Label required warning in method Phase main block null" in message[0:57]


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS43376.py"])
