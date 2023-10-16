# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def test_booth_edit(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(20)
    BoothName = BaseFun(browser).Random_Str(6)
    # Add a Booth
    browser.find_element(By.XPATH, "//a[text()='Add a Booth']").click()
    time.sleep(2)
    browser.find_element(By.NAME, "boothTag").clear()
    browser.find_element(By.NAME, "boothTag").send_keys(BoothName)
    browser.find_element(By.NAME, "boothDescription").send_keys("for test")
    browser.find_element(By.NAME, "labelPrinter").send_keys("shfile01")
    browser.find_element(By.NAME, "lastCleanTypeValue").send_keys("Full Clean")
    browser.find_element(By.NAME, "cleanExpirePeriod").send_keys("123456")
    browser.find_element(By.NAME, "apiCleanExpirePeriod").send_keys("23456")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys("3456")
    browser.find_element(By.XPATH, "//div[text()='Last Clean Date:']/../../td[2]//input").send_keys("9/19/22, 12:00:00 PM")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(5)
    # assert the Booth
    browser.refresh()
    time.sleep(15)
    TestBooth = "//td[text()='"+BoothName+"']/.."
    # print(TestBooth)
    assert BaseFun(browser).is_element_showed(TestBooth) is True
    # copy a Booth
    browser.find_element(By.XPATH, TestBooth).click()
    browser.find_element(By.XPATH, "//a[text()='Copy selected row']").click()
    time.sleep(2)
    browser.find_element(By.NAME, "boothDescription").clear()
    browser.find_element(By.NAME, "boothDescription").send_keys("test for copy")
    browser.find_element(By.NAME, "boothDescription").send_keys(Keys.ENTER)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(5)
    browser.refresh()
    time.sleep(5)
    assert BaseFun(browser).is_element_showed("//td[text()='"+BoothName+"***']/..") is True
    # delete a booth
    browser.find_element(By.XPATH, "//td[text()='"+BoothName+"***']/../td[17]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    browser.refresh()
    time.sleep(25)
    assert BaseFun(browser).is_element_showed("//td[text()='"+BoothName+"***']/..") is False
    # edit the booth1
    Booth1 = browser.find_element(By.XPATH, "//td[text()='booth1']/../td[3]/img")
    Booth1.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys("for test")
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys(Keys.ENTER)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(5)
    browser.refresh()
    time.sleep(25)
    assert "for test" in browser.find_element(By.XPATH, "//td[text()='booth1']/../td[2]").text
    # export CSV
    browser.refresh()
    time.sleep(5)
    browser.find_elements(By.XPATH, "//a[@class='Line_No_Wrap' and text()='CSV']")[0].click()
    time.sleep(20)
    assert BaseFun(browser).Assert_CSV("WDEquipmentBoothData") is not None

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41001.py"])






