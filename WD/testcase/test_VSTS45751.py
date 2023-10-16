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


def test_campaigns_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to campaign page and make change
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
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@class='WD_TextBox']").send_keys("CampaignReport")
    time.sleep(3)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(3)
    # modify the campaign
    browser.find_element(By.XPATH, "//tr/td/div[text()='Campaigns']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//td[text()='CampaignReport']/../td[9]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//td[text()='1072']/../td[8]/select").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//option[@value='booth1']").click()
    # Select(browser.find_element(By.XPATH, "//td[text()='1072']/../td[8]/select")).select_by_value("booth1")
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    # active the campaign
    browser.find_element(By.XPATH, "//td[text()='CampaignReport']/../td[1]/span/input").click()
    browser.find_element(By.XPATH, "//a[text()='Activate Orders for Selected Campaigns']").click()
    browser.refresh()
    time.sleep(3)
    # delete the campaign
    browser.find_element(By.XPATH, "//td[text()='CampaignReport']/../td[10]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    # 2.Navigate to campaign report page
    ReportPage(browser).go_to_Report()
    # campaign report
    try:
        browser.find_element(By.XPATH, "//div[text()='Campaigns']").click()
    except ElementNotInteractableException:
        browser.find_element(By.XPATH, "//div[text()='Audits']").click()
        browser.find_element(By.XPATH, "//div[text()='Campaigns']").click()
    user = Select(browser.find_elements(by=By.TAG_NAME,  value="select")[1])
    campaign = Select(browser.find_elements(by=By.TAG_NAME,  value="select")[0])
    start_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[0]
    end_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[1]
    # action
    create = browser.find_element(By.XPATH, "//label[text()='Created']")
    modify = browser.find_element(By.XPATH, "//label[text()='Modified']")
    active = browser.find_element(By.XPATH, "//label[text()='Activated']")
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
    # campaign
    campaign.select_by_visible_text("CampaignReport")
    time.sleep(3)
    create.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(3)
    # check the result is right
    columns = ["User", "Campaign", "Action"]
    dataTexts = [user_fullname, "CampaignReport", "Created"]
    ReportPage(browser).test_AuditData(columns, dataTexts)
    # 3.show differences only
    nums = [0, 1]
    data = ["test3", "Added"]
    ReportPage(browser).test_DifferenceData("gwt-HTML", nums, data)
if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS45751.py"])