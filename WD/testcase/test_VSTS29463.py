import time
import pytest
from selenium.webdriver.common.by import By

from common.baseFun import BaseFun
from pages.Administration import AdministrationPage


def test_user_exit_runtest(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Expand User Exit and select Barcode Scanning
    browser.find_element(By.XPATH, "//div[text()='User Exits']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Barcode Scanning']").click()
    time.sleep(3)
    # 3.Select row to set original script
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
    # 4.input test value and run test
    value = browser.find_element(By.XPATH, "//input[@class='TextBox_Style']")
    value.send_keys("~")
    test = browser.find_element(By.XPATH, "//button[text() ='Run Test']")
    test.click()
    time.sleep(3)
    # check test result
    result = browser.find_element(By.XPATH, "//div[text()='Results:']/../../td[3]/div")
    assert "Test result:Yes" == result.text
    # 4.change the script without commit and rerun test
    browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].click()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].clear()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].send_keys("LEFT(Barcode,1) = \"@\"")
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[1].click()
    time.sleep(5)
    test.click()
    time.sleep(3)
    assert "Test result:No" == result.text
    # change input value
    value.clear()
    value.send_keys("@")
    time.sleep(3)
    test.click()
    time.sleep(3)
    assert "Test result:Yes" == result.text
    # 5.compile failed
    browser.find_elements(By.XPATH, "//input[@name ='Code_OnYes']")[-1].click()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_OnYes']")[-1].send_keys("yes")
    time.sleep(3)
    browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[-1].click()
    time.sleep(3)
    # Check Commit fail
    test.click()
    time.sleep(3)
    message = BaseFun(browser).get_AlterMessage()
    print(message[0:57])
    assert "W1:Label required warning in method Phase main block null" in message[0:57]
    # 6.leave page without commit
    browser.find_element(By.XPATH, "//div[text()='Kitting Scan']").click()
    time.sleep(3)
    assert "The current view was modified. Do you want to leave without saving?" in BaseFun(browser).get_AlterMessage()
    browser.find_element(By.XPATH, "//div[text()='Barcode Scanning']").click()
    time.sleep(3)
    text = browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].get_attribute('value')
    assert "LEFT(Barcode,1) = \"~\"" == text


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS29463.py"])
