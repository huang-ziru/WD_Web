# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def test_add_twoBooth(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Add Booth A.
    browser.refresh()
    time.sleep(6)
    browser.find_element(By.XPATH, "//a[text()='Add a Booth']").click()
    time.sleep(2)
    browser.find_element(By.NAME, "boothTag").clear()
    browser.find_element(By.NAME, "boothTag").send_keys("A")
    browser.find_element(By.NAME, "boothDescription").send_keys("booth A")
    browser.find_element(By.NAME, "labelPrinter").send_keys("\\shfile01\SH25_R&D")
    browser.find_element(By.NAME, "lastCleanTypeValue").send_keys("Full Clean")
    browser.find_element(By.NAME, "cleanExpirePeriod").send_keys("123456")
    browser.find_element(By.NAME, "apiCleanExpirePeriod").send_keys("23456")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys("3456")
    browser.find_element(By.XPATH, "//div[text()='Last Clean Date:']/../../td[2]//input").send_keys("9/19/22, 12:00:00 PM")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(3)
    browser.refresh()
    time.sleep(20)
    # Add BoothB.
    browser.find_element(By.XPATH, "//a[text()='Add a Booth']").click()
    time.sleep(2)
    browser.find_element(By.NAME, "boothTag").clear()
    browser.find_element(By.NAME, "boothTag").send_keys("B")
    browser.find_element(By.NAME, "boothDescription").send_keys("booth B")
    browser.find_element(By.NAME, "labelPrinter").send_keys("\\shfile01\SH2530D")
    browser.find_element(By.NAME, "lastCleanTypeValue").send_keys("Full Clean")
    browser.find_element(By.NAME, "cleanExpirePeriod").send_keys("123456")
    browser.find_element(By.NAME, "apiCleanExpirePeriod").send_keys("23456")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys("3456")
    browser.find_element(By.XPATH, "//div[text()='Last Clean Date:']/../../td[2]//input").send_keys("9/19/22, 12:00:00 PM")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(2)
    browser.refresh()
    time.sleep(5)
    # Add a Scale
    browser.find_element(By.XPATH, "//a[text()='Add a Scale']").click()
    time.sleep(2)
    browser.find_element(By.NAME, "scaleTag").clear()
    browser.find_element(By.NAME, "scaleTag").send_keys("ScaleA")
    browser.find_element(By.NAME, "description").send_keys("Scale A")
    browser.find_element(By.NAME, "boothTag").click()
    browser.find_element(By.XPATH, "//option[@value='A']").click()
    browser.find_element(By.NAME, "minRange").send_keys("123")
    browser.find_element(By.NAME, "maxRange").send_keys("234")
    browser.find_element(By.NAME, "minTare").send_keys("1")
    browser.find_element(By.NAME, "maxTare").send_keys("2")
    browser.find_element(By.NAME, "statusValue").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[@value='Scale_Maintain']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(2)
    browser.refresh()
    time.sleep(6)
    assert "A" in browser.find_element(By.XPATH, "//td[text()='ScaleA']/../td[13]").text
    # edit the ScaleA
    browser.find_element(By.XPATH, "//td[text()='ScaleA']/../td[3]/img").click()
    time.sleep(2)
    browser.find_element(By.NAME, "boothTag").click()
    browser.find_element(By.XPATH, "//option[@value='B']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    browser.refresh()
    time.sleep(6)
    assert "B" in browser.find_element(By.XPATH, "//td[text()='ScaleA']/../td[13]").text

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS45682.py"])






