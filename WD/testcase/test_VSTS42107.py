# coding = utf-8
import configparser
import time

import pytest
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.baseFun import BaseFun

from pages.Equipment import EquipmentPage
from pages.Report import ReportPage


def test_scale_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to scale page and make change
    EquipmentPage(browser).go_to_Equipment()
    scales = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']")
    scale_name = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr[2]/td[1]")[1].text
    editScale = scales[1].find_elements(By.TAG_NAME,  "img")
    editScale[2].click()
    time.sleep(3)
    description = browser.find_element(By.NAME, "description")
    description.clear()
    random_str = BaseFun(browser).Random_Str(5)
    name = "test description report " + random_str
    description.send_keys(name)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 2.Navigate to report page
    ReportPage(browser).go_to_Report()
    try:
        browser.find_element(By.XPATH, "//div[text()='Scales']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='Scales']").click()
    # browser.find_element(By.XPATH, "//div[text()='Audits']").click()
    # # Scales report
    # browser.find_element(By.XPATH, "//div[text()='Scales']").click()
    booth = Select(browser.find_elements(By.TAG_NAME,  "select")[0])
    scale = Select(browser.find_elements(By.TAG_NAME,  "select")[1])
    user = Select(browser.find_elements(By.TAG_NAME,  "select")[2])
    start_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[0]
    end_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[1]
    action = browser.find_element(By.XPATH, "//label[text()='Modified']")
    time.sleep(3)
    # set criteria
    # # start time
    # start_time.click()
    # browser.find_element(By.XPATH, "//button[text()='Zero']").click()
    # time.sleep(3)
    booth.select_by_value("booth2")
    time.sleep(3)
    # # end time
    # end_time.click()
    # browser.find_element(By.XPATH, "//button[text()='Now']").click()
    # time.sleep(3)
    user.select_by_visible_text(user_fullname)
    time.sleep(3)
    scale.select_by_visible_text(scale_name)
    time.sleep(3)
    action.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    # check the result is right
    columns = ["User", "Scale", "Action"]
    dataTexts = [user_fullname, scale_name, "Modified"]
    ReportPage(browser).test_AuditData(columns, dataTexts)
    # rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    # for row in rows:
    #     # date?
    #     u = row.find_elements(By.TAG_NAME,  "td")[2].text
    #     s = row.find_elements(By.TAG_NAME,  "td")[3].text
    #     a = row.find_elements(By.TAG_NAME,  "td")[4].text
    #     print(u)
    #     print(s)
    #     print(a)
    #     if u != "" and s != "" and a != "":
    #         assert u == "qapart(qapart)", s == "PL1501-S"
    #         assert a == "Modified"
    # time.sleep(3)
    # 3.check show differences only.
    nums = [3]
    data = [name]
    ReportPage(browser).test_DifferenceData("gwt-HTML", nums, data)
    # browser.find_element(By.XPATH, "//label[text()='Show Difference Only']").click()
    # time.sleep(3)
    # rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    # rows[1].find_element(By.TAG_NAME,  "img").click()
    # time.sleep(3)
    # diff = browser.find_elements(By.XPATH, "//div[@class='gwt-HTML']")[3].text
    # print(diff)
    # assert diff == "test description report"
    # 4.print


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS42107.py"])
