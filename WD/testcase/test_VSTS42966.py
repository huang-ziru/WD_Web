# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from conftest import login_with_others

def test_booth_delete_when_edit(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # add a Booth
    BoothName = BaseFun(browser).Random_Str(6)
    browser.find_element(By.XPATH, "//a[text()='Add a Booth']").click()
    time.sleep(2)
    browser.find_element(By.NAME, "boothTag").clear()
    browser.find_element(By.NAME, "boothTag").send_keys(BoothName)
    browser.find_element(By.NAME, "boothDescription").send_keys("RandomBooth")
    browser.find_element(By.NAME, "labelPrinter").send_keys("\\shfile01\\SH2")
    browser.find_element(By.NAME, "lastCleanTypeValue").send_keys("Full Clean")
    browser.find_element(By.NAME, "cleanExpirePeriod").send_keys("10000")
    browser.find_element(By.NAME, "apiCleanExpirePeriod").send_keys("2000")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys("1000")
    browser.find_element(By.NAME, "excCleanExpirePeriod").send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    time.sleep(6)
    browser.refresh()
    time.sleep(10)
    # Edit the Booth.
    Booth1 = browser.find_element(By.XPATH, "//td[text()='" + BoothName + "']/../td[3]/img")
    Booth1.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys("for test")
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys(Keys.ENTER)
    # another user login the web and delete the same deleteBooth
    Edge_driver = login_with_others()
    time.sleep(5)
    Edge_driver.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # delete the Booth.
    Booth1 = Edge_driver.find_element(By.XPATH, "//td[text()='"+BoothName+"']/../td[17]")
    Booth1.click()
    time.sleep(2)
    Edge_driver.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)
    Edge_driver.refresh()
    time.sleep(6)
    assert BaseFun(Edge_driver).is_element_showed("//td[text()='"+BoothName+"']/..") is False
    time.sleep(5)
    # Edge_driver.quit()
    browser.find_element(By.XPATH,  "//button[text()='Apply']").click()
    time.sleep(3)
    assert "E4125: Another user has changed the data, you must perform a refresh from the server" in BaseFun(browser).get_AlterMessage()
if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS42966.py"])






