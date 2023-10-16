# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_print(browser):
    now_handle = browser.window_handles[0]
    time.sleep(5)
    browser.find_element(By.XPATH, "//tr/td/div[text()='Report']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Audits']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Scales' and @class = 'Nav_Label']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(10)
    browser.find_element(By.XPATH, "//a[text()='Print']").click()
    time.sleep(5)
    handles = browser.window_handles
    for handle in handles:
        if handle != now_handle:
            print_handle = handle
    browser.switch_to_window(print_handle)
    browser.find_element(By.XPATH, "//select[@class='md-select']").click()
    browser.find_element(By.XPATH, "//option[@value='Save as PDF/local/']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//cr-button[@class='action-button']").click()
    time.sleep(3)
    handles33 = browser.window_handles
    print(handles33)
    # browser.find_element(By.XPATH, "//").send_keys(Keys.ENTER)


if __name__ == '__main__':

    pytest.main(["-s", "print.py"])






