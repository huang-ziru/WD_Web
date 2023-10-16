# coding = utf-8
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.baseFun import BaseFun
from pages.Administration import AdministrationPage
from pages.Equipment import EquipmentPage


def test_clean_rules_states(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Select Cleaning rules-States
    browser.find_element(By.XPATH, "//div[text()='Cleaning Rules']").click()
    time.sleep(3)
    AdministrationPage(browser).add_new_states("test state")
    # browser.find_element(By.XPATH, "//div[text()='States']").click()
    # time.sleep(3)
    # # 3.Add a state and apply
    # browser.find_element(By.XPATH, "//a[text()='Add a State']").click()
    # state = browser.find_element(By.XPATH, "//input[@name='CleanRule_State']")
    # state.clear()
    # state.send_keys("test state")
    # description = browser.find_element(By.XPATH, "//textarea[@name='Description']")
    # description.send_keys("test description")
    # apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    # time.sleep(3)
    # if apply.is_enabled():
    #     apply.click()
    #     time.sleep(3)
    # # Check add success
    # table = browser.find_element(By.XPATH, "//table[@class='List_Table_Border_Style']")
    # rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
    # row_num = len(rows)
    # print(row_num)
    # state_text = rows[-1].find_elements(By.TAG_NAME,  "td")[0].text
    # # state_text = rows[-1].find_elements_by_xpath("/td")[0].text
    # assert state_text == "test state"
    # 4.try to move up/down a state
    up = browser.find_element(By.XPATH, "//a[text()='Move Up']")
    down = browser.find_element(By.XPATH, "//a[text()='Move Down']")
    # move top line
    rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
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
    # 5.Delete states
    rows[-1].find_elements(By.TAG_NAME,  "img")[-1].click()
    time.sleep(3)
    assert "Are you sure you want to delete test state?" in BaseFun(browser).get_AlterMessage()
    # 6. Check the state added to the booth status.
    # add state
    random_str = BaseFun(browser).Random_Str(5)
    name = "test state "+random_str
    AdministrationPage(browser).add_new_states(name)
    # browser.find_element(By.XPATH, "//a[text()='Add a State']").click()
    # state = browser.find_element(By.XPATH, "//input[@name='CleanRule_State']")
    # state.clear()
    # state.send_keys("test state")
    # description = browser.find_element(By.XPATH, "//textarea[@name='Description']")
    # description.send_keys("test description")
    # apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    # time.sleep(3)
    # if apply.is_enabled():
    #     apply.click()
    #     time.sleep(3)
    commit = browser.find_element(By.XPATH, "//button[text()='Commit Rules']")
    if commit.is_enabled():
        commit.click()
        time.sleep(3)
    time.sleep(5)
    assert "Clean rules committed successfully." in BaseFun(browser).get_AlterMessage()
    # go to equipment\booth check states
    EquipmentPage(browser).go_to_Equipment()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//img[@class='gwt-Image Head_Blue_Style']")[1].click()
    status = browser.find_element(By.XPATH, "//select[@name='boothStatusValue']")
    time.sleep(3)
    options = status.find_elements(By.TAG_NAME,  "option")
    for option in options:
        # print(option.get_attribute("value"))
        if option.get_attribute("value") == name:
            result = True
            break
    assert result


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41179.py"])