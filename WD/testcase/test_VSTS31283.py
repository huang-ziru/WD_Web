# coding = utf-8
import configparser
import datetime
import time

import pytest
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.baseFun import BaseFun
from pages.Administration import AdministrationPage
from pages.Report import ReportPage


def test_user_exits_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to user_exits page and make change
    AdministrationPage(browser).go_to_administration()
    browser.find_element(By.XPATH, "//div[text()='User Exits']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Kitting Scan']").click()
    time.sleep(3)
    AdministrationPage(browser).add_script_user_exit()
    # browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[-1].click()
    # time.sleep(3)
    # browser.find_elements(By.XPATH, "//input[@name ='Code_Code']")[-1].send_keys("abc")
    # time.sleep(3)
    # browser.find_elements(By.XPATH, "//input[@name ='Code_Label']")[-1].click()
    # time.sleep(3)
    # browser.find_element(By.XPATH, "//button[text() ='Commit User Exit']").click()
    # time.sleep(3)
    # # Check Commit successfully
    # assert "Commit User Exit Success" in BaseFun(browser).get_AlterMessage()
    # 2.Navigate to report page
    ReportPage(browser).go_to_Report()
    # User Exit report
    try:
        browser.find_element(By.XPATH, "//div[text()='User Exits']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='User Exits']").click()
    time.sleep(3)
    user_exit = Select(browser.find_elements(By.TAG_NAME,  "select")[0])
    user = Select(browser.find_elements(By.TAG_NAME,  "select")[1])
    start_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[0]
    end_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[1]
    # start time
    start_time.click()
    browser.find_element(By.XPATH, "//button[text()='Zero']").click()
    time.sleep(3)
    user_exit.select_by_value("Kitting Scan")
    # end time
    end_time.click()
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    time.sleep(3)
    user.select_by_visible_text(user_fullname)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    # check the result is right
    columns = ["User", "User-exit"]
    dataTexts = [user_fullname, "Kitting Scan"]
    ReportPage(browser).test_AuditData(columns, dataTexts)
    # rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    # for row in rows:
    #     # date?
    #     u = row.find_elements(By.TAG_NAME,  "td")[2].text
    #     e = row.find_elements(By.TAG_NAME,  "td")[3].text
    #     print(u)
    #     print(e)
    #     if u != "" and e != "":
    #         assert u == "qapart(qapart)", e == "Kitting Scan"
    # time.sleep(3)
    # 3.check show differences only.
    nums = [1]
    data = ["@ @ @ abc"]
    ReportPage(browser).test_DifferenceData("gwt-HTML", nums, data)
    # browser.find_element(By.XPATH, "//label[text()='Show Difference Only']").click()
    # time.sleep(3)
    # rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    # rows[1].find_element(By.TAG_NAME,  "img").click()
    # time.sleep(3)
    # diff = browser.find_elements(By.XPATH, "//div[@class='gwt-HTML']")[1].text
    # print(diff)
    # assert diff == "@ @ @ abc"
    # 4.print


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS31283.py"])
