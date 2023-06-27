# coding = utf-8
import configparser
import datetime
import time

import pytest
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun
from pages.Administration import AdministrationPage
from pages.Report import ReportPage


def test_audit_orders_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to order page and make change
    browser.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
    time.sleep(5)
    #  select a order, click Create campaign
    i = 0
    while i in range(10):
        try:
            browser.find_element(By.XPATH, "//td[text()='test3']")
        except NoSuchElementException:
            browser.find_element(By.XPATH, "//a[text()='Refresh']").click()
        i = i + 1
    time.sleep(3)
    select_order = browser.find_element(By.XPATH, "//td[text()='test3']")
    time.sleep(3)
    select_order.find_element(By.XPATH, "../td/span[@class='gwt-CheckBox']").click()
    time.sleep(2)
    # browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style OrderActivate_Image']").click()
    # time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@class='WD_TextBox']").send_keys("CampaignReport")
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    # delete the campaign
    browser.find_element(By.XPATH, "//tr/td/div[text()='Campaigns']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//td[text()='CampaignReport']/../td[10]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    # 2.Navigate to audit orders page
    ReportPage(browser).go_to_Report()
    # audit orders report
    try:
        browser.find_element(By.XPATH, "//div[text()='Orders']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[text()='Orders']").click()
    time.sleep(3)
    user = Select(browser.find_element(by=By.TAG_NAME,  value="select"))
    start_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[0]
    end_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[1]
    order = browser.find_element(By.XPATH, "//input[@class='WD_TextBox']")
    # action
    # active = browser.find_element(By.XPATH, "//label[text()='Activated']")
    add_campaign = browser.find_element(By.XPATH, "//label[text()='Added to campaign']")
    # set criteria
    # start time
    start_time.click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Zero']").click()
    time.sleep(3)
    user.select_by_visible_text(user_fullname)
    time.sleep(3)
    # end time
    end_time.click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    time.sleep(3)
    order.send_keys("test3")
    time.sleep(3)
    # active.click()
    # browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    # time.sleep(3)
    # # check the result is right-active
    # columns = ["User", "Order", "Action"]
    # dataTexts = [user_fullname, "test3", "Activated"]
    # ReportPage(browser).test_AuditData(columns, dataTexts)
    # # show differences only
    # nums = [10, 11, 12]
    # data = ["Action", "Planned", "Activated"]
    # ReportPage(browser).test_DifferenceData("gwt-Label", nums, data)

    # check the result is right-campaign
    # browser.find_element(By.XPATH, "//label[text()='Show Difference Only']").click()
    # active.click()
    add_campaign.click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    columns = ["User", "Order", "Action"]
    dataTexts = [user_fullname, "test3", "Added to campaign(CampaignReport)"]
    ReportPage(browser).test_AuditData(columns, dataTexts)
    # 3.show differences only
    nums = [10, 12]
    data = ["Action", "Added to campaign"]
    ReportPage(browser).test_DifferenceData("gwt-Label", nums, data)
    # rows = browser.find_elements(By.XPATH, "//table[@class='Permission_Table_body_Style']/tbody/tr")
    # rows[1].find_element(By.TAG_NAME,  "img").click()
    # time.sleep(3)
    # for i in range(len(nums)):
    #     diff = browser.find_elements(By.XPATH, "//div[@class='gwt-Label']")[nums[i]].text
    #     print(diff)
    #     assert diff == data[i]


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS42062.py"])
