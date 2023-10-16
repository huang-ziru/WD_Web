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
from pages.Report import ReportPage


def test_materials_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to booth page and make change
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    time.sleep(10)
    pending_BOM = browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[6]")
    pending_BOM[2].click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@name='targetType']").clear()
    time.sleep(3)
    random_str = BaseFun(browser).Random_Str(5)
    name = "report test " + random_str
    browser.find_element(By.XPATH, "//input[@name='targetType']").send_keys(name)
    browser.find_element(By.XPATH, "//input[@name='targetType']").send_keys(Keys.ENTER)
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
    timedate = (datetime.datetime.now() + datetime.timedelta(seconds=20)).strftime("%m/%d/%y, %I:%M:%S %p")
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@class='Date_TextBox_Style']").send_keys(timedate)
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@id='Dialogbox_Bottom_OK_Button_Id']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(20)
    browser.find_element(By.XPATH, "//a[text()='Refresh']").click()
    time.sleep(2)
    delete_BOM = browser.find_element(By.XPATH, "//td[text()='Obsolete']/../td[31]")
    delete_BOM.click()
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    # 2.Navigate to materials report page
    ReportPage(browser).go_to_Report()
    # materials report
    try:
        browser.find_element(By.XPATH, "//div[text()='Materials']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='Materials']").click()
    user = Select(browser.find_elements(By.TAG_NAME,  "select")[1])
    material = Select(browser.find_elements(By.TAG_NAME,  "select")[0])
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
    material.select_by_visible_text("1902")
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    # 3.check the result is right
    columns = ["User", "Material"]
    dataTexts = [user_fullname, "1902"]
    ReportPage(browser).test_AuditData(columns, dataTexts)
    # 4.check show differences only.
    time.sleep(3)
    nums = [9, 11]
    data = ["Target type", name]
    ReportPage(browser).test_DifferenceData("gwt-Label", nums, data)


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS43253.py"])