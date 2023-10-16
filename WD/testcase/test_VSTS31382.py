# coding = utf-8
import configparser
import datetime
import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun

from pages.Administration import AdministrationPage
from pages.OrdersPage import OrdersPage
from pages.Report import ReportPage


def test_order_print_report(browser):
    config = configparser.ConfigParser()
    config.read(r'..\data\config.ini')
    user_fullname = config.get('login', 'user_fullname')
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to order page and make change
    order_list = OrdersPage(browser).get_orders_list()
    order_list[1].find_element(By.NAME, "!checkall").click()
    browser.find_element(By.XPATH, "//a[text()='Print Report']").click()
    time.sleep(8)
    browser.find_element(By.XPATH, "//button[text()='Close']").click()
    time.sleep(3)
    # 2.Navigate to report page
    ReportPage(browser).go_to_Report()
    # Order print report
    browser.find_element(By.XPATH, "//div[text()='Order Print']").click()
    time.sleep(3)
    type = Select(browser.find_elements(By.TAG_NAME,  "select")[0])
    Operator = Select(browser.find_elements(By.TAG_NAME,  "select")[1])
    start_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[0]
    end_time = browser.find_elements(By.XPATH, "//input[@class='Date_TextBox_Style']/../../td/img")[1]
    order = browser.find_element(By.XPATH, "//input[@class='WD_TextBox']")
    # set criteria
    # start time
    start_time.click()
    browser.find_element(By.XPATH, "//button[text()='Zero']").click()
    time.sleep(3)
    Operator.select_by_visible_text(user_fullname)
    time.sleep(3)
    # end time
    end_time.click()
    browser.find_element(By.XPATH, "//button[text()='Now']").click()
    time.sleep(3)
    order.send_keys("test1")
    time.sleep(3)
    type.select_by_visible_text("In Progress")
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Generate Report']").click()
    time.sleep(3)
    # check the result is right
    columns = ["Type", "Order", "Operator"]
    dataTexts = ["In Progress", "test1", user_fullname]
    ReportPage(browser).test_ReportData(columns, dataTexts)
    # 3.save as /print


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS31382.py"])