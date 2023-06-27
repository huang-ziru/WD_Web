# coding = utf-8
import configparser
import datetime
import time

import pytest
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun
from pages.Administration import AdministrationPage
from pages.Equipment import EquipmentPage
from pages.Report import ReportPage


def test_clean_rules_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.add signature when commit
    AdministrationPage(browser).go_to_administration()
    browser.find_element(By.XPATH, "//div[text()='Signatures']").click()
    time.sleep(3)
    row = browser.find_element(By.XPATH, "//div[text()='Cleaning Rules' and @class='gwt-Label']/../..")
    signature = row.find_element(By.TAG_NAME,  "input")
    reason = Select(row.find_element(By.TAG_NAME,  "select"))
    if not signature.is_selected():
        signature.click()
    reason.select_by_visible_text("Optional")
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
        text = "Apply Signature Successful"
        assert text in BaseFun(browser).get_AlterMessage()
    # 2.Select Cleaning rules-States and add a new state
    browser.find_element(By.XPATH, "//div[text()='Cleaning Rules']").click()
    time.sleep(3)
    random_str = BaseFun(browser).Random_Str(5)
    name = "test state report " + random_str
    AdministrationPage(browser).add_new_states(name)
    # browser.find_element(By.XPATH, "//div[text()='States']").click()
    # time.sleep(3)
    # browser.find_element(By.XPATH, "//a[text()='Add a State']").click()
    # state = browser.find_element(By.XPATH, "//input[@name='CleanRule_State']")
    # state.clear()
    # state.send_keys("test state report")
    # description = browser.find_element(By.XPATH, "//textarea[@name='Description']")
    # description.send_keys("test description")
    # apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    # time.sleep(3)
    # if apply.is_enabled():
    #     apply.click()
    #     time.sleep(3)
    # # Check add success
    # rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
    # row_num = len(rows)
    # print(row_num)
    # state_text = rows[-1].find_elements(By.TAG_NAME,  "td")[0].text
    # assert state_text == "test state"
    # 3.commit and check signature
    commit = browser.find_element(By.XPATH, "//button[text()='Commit Rules']")
    if commit.is_enabled():
        commit.click()
        time.sleep(3)
    time.sleep(3)
    AdministrationPage(browser).check_signature_optional()
    assert "Clean rules committed successfully." in BaseFun(browser).get_AlterMessage()
    time.sleep(3)
    # 4.Navigate to report page
    ReportPage(browser).go_to_Report()
    time.sleep(3)
    # Cleaning Rules report
    try:
        browser.find_element(By.XPATH, "//div[text()='Cleaning Rules']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='Cleaning Rules']").click()
    user = Select(browser.find_elements(By.TAG_NAME,  "select")[0])
    start_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[0]
    end_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[1]
    # set criteria
    # start time
    start_time.click()
    browser.find_element(By.XPATH, "//button[text()='Zero']").click()
    time.sleep(3)
    user.select_by_visible_text(user_fullname)
    time.sleep(3)
    # end time
    end_time.click()
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    # check the result is right
    columns = ["User"]
    dataTexts = [user_fullname]
    ReportPage(browser).test_AuditData(columns, dataTexts)
    # rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    # for row in rows:
    #     # date?
    #     u = row.find_elements(By.TAG_NAME,  "td")[3].text
    #     print(u)
    #     if u != "Commit date":
    #         assert u == "qapart(qapart)"
    # time.sleep(3)
    # 5.check show differences only.
    nums = [4, 5]
    data = ["   "+name, "Added"]
    ReportPage(browser).test_DifferenceData("gwt-HTML", nums, data)
    # browser.find_element(By.XPATH, "//label[text()='Show Difference Only']").click()
    # time.sleep(3)
    # rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    # rows[1].find_element(By.TAG_NAME,  "img").click()
    # time.sleep(3)
    # diff = browser.find_elements(By.XPATH, "//div[@class='gwt-HTML']")[4].text
    # action = browser.find_elements(By.XPATH, "//div[@class='gwt-HTML']")[5].text
    # print(diff)
    # assert diff == "   test state report"
    # assert action == "Added"

    # delete signature when commit
    AdministrationPage(browser).go_to_administration()
    browser.find_element(By.XPATH, "//div[text()='Signatures']").click()
    time.sleep(3)
    row = browser.find_element(By.XPATH, "//div[text()='Cleaning Rules' and @class='gwt-Label']/../..")
    signature = row.find_element(By.TAG_NAME, "input")
    reason = Select(row.find_element(By.TAG_NAME, "select"))
    if signature.is_selected():
        signature.click()
    reason.select_by_visible_text("None")
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
        text = "Apply Signature Successful"
        assert text in BaseFun(browser).get_AlterMessage()
    # 6.print


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS40961.py"])
