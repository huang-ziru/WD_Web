# coding = utf-8
import time

import pytest
from selenium.webdriver.common.by import By
from pages.Administration import AdministrationPage
from common.baseFun import BaseFun


def test_clean_rules_states(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Select Cleaning rules-States
    browser.find_element(By.XPATH, "//div[text()='Cleaning Rules']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Actions']").click()
    time.sleep(3)
    # 3.Add an Action and apply
    browser.find_element(By.XPATH, "//a[text()='Add an Action']").click()
    action = browser.find_element(By.XPATH, "//input[@name='CleanRule_Action']")
    action.clear()
    action.send_keys("test action")
    description = browser.find_element(By.XPATH, "//textarea[@name='CleanRule_Comment']")
    description.send_keys("test comment")
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    time.sleep(3)
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # Check add success
    rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
    print(len(rows))
    action_text = rows[-1].find_elements(By.TAG_NAME,  "td")[0].text
    # action_text = rows[-1].find_elements_by_xpath("/td")[0].text
    assert action_text == "test action"
    # 4.try to move up/down a action
    up = browser.find_element(By.XPATH, "//a[text()='Move Up']")
    down = browser.find_element(By.XPATH, "//a[text()='Move Down']")
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
    # 5.Delete action
    rows[-1].find_elements(By.TAG_NAME,  "img")[-1].click()
    time.sleep(3)
    assert "Are you sure you want to delete test action?" in BaseFun(browser).get_AlterMessage()


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41179.py"])