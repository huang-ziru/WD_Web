# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By

from pages.Administration import AdministrationPage


def test_user_exit_tool_bar(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Expand User Exit and select one option
    browser.find_element(By.XPATH, "//div[text()='User Exits']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Barcode Scanning']").click()
    time.sleep(3)
    # first line text
    text_cut_old = browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[0].get_attribute('value')
    # 3.Select one row of define logic, then click cut button.
    browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[0].click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class ='WDAnchor_Common_Image16_Style Cut-16_Image']").click()
    time.sleep(3)
    # Check the first line is cut
    text_cut_new = browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[0].get_attribute('value')
    assert text_cut_old != text_cut_new
    # 4.Select a row and click paste.
    browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[1].click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class ='WDAnchor_Common_Image16_Style Paste-16_Image']").click()
    time.sleep(3)
    # Check the cut line is paste to second line
    text_cut_paste = browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].get_attribute('value')
    assert text_cut_old == text_cut_paste
    # 5.Select one row of define logic, then click copy button.
    text_copy_old = browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].get_attribute('value')
    browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[1].click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class ='WDAnchor_Common_Image16_Style Copy-16_Image']").click()
    time.sleep(3)
    # 6.Click paste.
    browser.find_element(By.XPATH, "//button[@class ='WDAnchor_Common_Image16_Style Paste-16_Image']").click()
    time.sleep(3)
    # Check past and copy line
    text_paste_old = browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[1].get_attribute('value')
    text_paste_new = browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[2].get_attribute('value')
    assert text_copy_old == text_paste_old == text_paste_new


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS31386.py"])
