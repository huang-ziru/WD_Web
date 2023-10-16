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


def test_booth_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to booth page and make change
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Add a Booth
    browser.find_element(By.XPATH, "//a[text()='Add a Booth']").click()
    time.sleep(2)
    browser.find_element(By.NAME, "boothTag").clear()
    browser.find_element(By.NAME, "boothTag").send_keys("testreportBooth")
    browser.find_element(By.NAME, "boothDescription").send_keys("for test")
    browser.find_element(By.NAME, "labelPrinter").send_keys("\\shfile01\SH2530_R&D")
    browser.find_element(By.NAME, "lastCleanTypeValue").send_keys("Full Clean")
    browser.find_element(By.NAME, "cleanExpirePeriod").send_keys("123456")
    browser.find_element(By.NAME, "apiCleanExpirePeriod").send_keys("23456")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys("3456")
    browser.find_element(By.XPATH, "//div[text()='Last Clean Date:']/../../td[2]//input").send_keys("9/19/22, 12:00:00 PM")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(12)
    browser.find_element(By.XPATH, "//a[text()='Refresh']").click()
    time.sleep(2)
    # edit the booth
    Booth = browser.find_element(By.XPATH, "//td[text()='testreportBooth']/../td[3]/img")
    Booth.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys(" change")
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(2)
    # delete the booth
    browser.find_element(By.XPATH, "//td[text()='testreportBooth']/../td[17]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    # 2.Navigate to booth report page
    ReportPage(browser).go_to_Report()
    # booth report
    try:
        browser.find_element(By.XPATH, "//div[text()='Booths']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='Booths']").click()
    user = Select(browser.find_elements(By.TAG_NAME,  "select")[1])
    booth = Select(browser.find_elements(By.TAG_NAME,  "select")[0])
    start_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[0]
    end_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[1]
    # action
    create = browser.find_element(By.XPATH, "//label[text()='Created']")
    modify = browser.find_element(By.XPATH, "//label[text()='Modified']")
    delete = browser.find_element(By.XPATH, "//label[text()='Deleted']")
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
    booth.select_by_visible_text("testreportBooth")
    time.sleep(3)
    modify.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    # 3.check the result is right
    columns = ["User", "Booth", "Action"]
    dataTexts = [user_fullname, "testreportBooth", "Modified"]
    ReportPage(browser).test_AuditData(columns, dataTexts)
    # 4.check show differences only.
    nums = [10, 11, 12]
    data = ["Description", "for test", "for test change"]
    modify.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    ReportPage(browser).test_DifferenceData("gwt-Label", nums, data)


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS42812.py"])