# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from pages.Report import ReportPage


def test_modify_booth(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='Administration']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//label[text()='Change state']/../input").click()
    browser.find_element(By.XPATH, "//button[@class='OkStyle']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Edit the Booth1.
    Booth1 = browser.find_element(By.XPATH, "//td[text()='booth1']/../td[3]/img")
    Booth1.click()
    time.sleep(3)
    # modify the any of booth NON-state related information Description,Machine name,Booth Group name, Label Printer Address, Report Printer Address
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys("for testing")
    browser.find_element(By.XPATH, "//select[@name='workstation']").click()
    browser.find_element(By.XPATH, "//select[@name='workstation']/option[1]").click()
    browser.find_element(By.XPATH, "//select[@name='boothGroup']").click()
    browser.find_element(By.XPATH, "//input[@name='labelPrinter']").send_keys("testing")
    browser.find_element(By.XPATH, "//input[@name='cleanExpirePeriod']").clear()
    browser.find_element(By.XPATH, "//input[@name='cleanExpirePeriod']").send_keys("123")
    browser.find_element(By.XPATH, "//input[@name='apiCleanExpirePeriod']").clear()
    browser.find_element(By.XPATH, "//input[@name='apiCleanExpirePeriod']").send_keys("12")
    browser.find_element(By.XPATH, "//input[@name='excCleanExpirePeriod']").clear()
    browser.find_element(By.XPATH, "//input[@name='excCleanExpirePeriod']").send_keys("23")
    browser.find_element(By.XPATH, "//input[@name='excCleanExpirePeriod']").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    browser.refresh()
    time.sleep(5)
    # check the report
    browser.find_element(By.XPATH, "//div[text()='Report']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[text()='Audits']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//div[text()='Booths']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//div[text()='User:']/../../td[5]/select[@class='gwt-ListBox Report_Cretiria_Combobox_Width']").click()
    browser.find_element(By.XPATH, "//div[text()='User:']/../../td[5]/select[@class='gwt-ListBox Report_Cretiria_Combobox_Width']/option[text()='qaone1(qaone1)']").click()
    browser.find_element(By.XPATH, "//div[text()='Booth:']/../../td[5]/select[@class='gwt-ListBox Report_Cretiria_Combobox_Width']").click()
    browser.find_element(By.XPATH, "//div[text()='Booth:']/../../td[5]/select[@class='gwt-ListBox Report_Cretiria_Combobox_Width']/option[@value='booth1']").click()
    browser.find_element(By.XPATH, "//label[text()='Modified']/../input").click()
    browser.find_element(By.XPATH, "//button[text()='Generate Audit']").click()
    time.sleep(5)
    # assert report
    columns = ["User", "Booth"]
    dataTexts = ["qaone1(qaone1)", "booth1"]
    ReportPage(browser).test_AuditData(columns, dataTexts)




if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS43508.py"])






