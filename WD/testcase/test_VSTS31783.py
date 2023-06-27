# coding = utf-8
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.baseFun import BaseFun
from pages.Administration import AdministrationPage
from pages.Equipment import EquipmentPage


def test_clean_rules_save(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Select Cleaning rules-States
    browser.find_element(By.XPATH, "//div[text()='Cleaning Rules']").click()
    time.sleep(3)
    # 3.add state and save
    random_str = BaseFun(browser).Random_Str(5)
    name = "test state save " + random_str
    AdministrationPage(browser).add_new_states(name)
    save = browser.find_element(By.XPATH, "//button[text()='Save Rules']")
    if save.is_enabled():
        save.click()
        time.sleep(3)
    time.sleep(5)
    assert "Clean rules saved successfully." in BaseFun(browser).get_AlterMessage()
    # go to equipment\booth check states
    EquipmentPage(browser).go_to_Equipment()
    time.sleep(3)
    browser.find_elements(By.XPATH, "//img[@class='gwt-Image Head_Blue_Style']")[1].click()
    status = browser.find_element(By.XPATH, "//select[@name='boothStatusValue']")
    time.sleep(3)
    options = status.find_elements(By.TAG_NAME, "option")
    for option in options:
        print(option.get_attribute("value"))
        if option.get_attribute("value") == name:
            result = False
            break
        else:
            result = True
    assert result
    # 3.add state and cancel
    AdministrationPage(browser).go_to_administration()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Cleaning Rules']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='States']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//a[text()='Add a State']").click()
    state = browser.find_element(By.XPATH, "//input[@name='CleanRule_State']")
    state.clear()
    random_str = BaseFun(browser).Random_Str(5)
    name1 = "test state cancel " + random_str
    state.send_keys(name1)
    description = browser.find_element(By.XPATH, "//textarea[@name='Description']")
    description.send_keys("test description")
    cancel = browser.find_element(By.XPATH, "//button[text()='Cancel']")
    time.sleep(3)
    if cancel.is_enabled():
        cancel.click()
        time.sleep(3)
    assert "Do you want to discard the changes?" in BaseFun(browser).get_AlterMessage()
    # Check cancel success
    rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
    print(len(rows))
    for row in rows:
        if row.find_elements_by_tag_name("td")[0].text == name1:
            result = False
            break
        else:
            result = True
    assert result
    # commit rules
    browser.find_element(By.XPATH, "//div[text()='Effective date:']/../../td[2]//img").click()
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    time.sleep(3)
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
    options = status.find_elements(By.TAG_NAME, "option")
    for option in options:
        print(option.get_attribute("value"))
        if option.get_attribute("value") == name:
            result = True
            break
    assert result


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS31783.py"])
