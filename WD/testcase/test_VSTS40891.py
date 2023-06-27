# coding = utf-8
import time

import pytest
from selenium.webdriver.common.by import By
from pages.Administration import AdministrationPage


def test_clean_rules_states(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Select Cleaning rules-States
    browser.find_element(By.XPATH, "//div[text()='Cleaning Rules']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Data']").click()
    time.sleep(3)
    # 3.Add an Action and apply
    try:
        browser.find_element(By.XPATH, "//a[text()='Add a Data']").click()
        result = False
    except:
        result = True
    # Check no add data
    assert result
    # 4.try to move up/down a data
    rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
    print(len(rows))
    up = browser.find_element(By.XPATH, "//a[text()='Move Up']")
    down = browser.find_element(By.XPATH, "//a[text()='Move Down']")
    print(len(rows))
    # move top line
    rows[1].find_elements(By.TAG_NAME,  "td")[0].click()
    time.sleep(3)
    assert up.get_attribute("class") == "gwt-Anchor WDAnchor_Common_Disable_Style", \
        down.get_attribute("class") == "gwt-Anchor "
    # move down
    down.click()
    time.sleep(3)
    assert up.get_attribute("class") == "gwt-Anchor", down.get_attribute("class") == "gwt-Anchor"
    # move bottom line
    rows[-1].find_elements(By.TAG_NAME,  "td")[0].click()
    time.sleep(3)
    assert down.get_attribute("class") == "gwt-Anchor WDAnchor_Common_Disable_Style", \
        up.get_attribute("class") == "gwt-Anchor "
    # move up
    up.click()
    time.sleep(3)
    assert up.get_attribute("class") == "gwt-Anchor", down.get_attribute("class") == "gwt-Anchor"


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41179.py"])
