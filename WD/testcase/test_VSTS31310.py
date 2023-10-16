# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun
from conftest import login_with_others


@pytest.mark.skip(reason="none mvt")
def test_booth_edit(browser):
    time.sleep(5)
    # BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Edit the Booth1.
    Booth1 = browser.find_element(By.XPATH, "//td[text()='booth1']/../td[3]/img")
    Booth1.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys("for test")
    browser.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys(Keys.ENTER)
    # another user login the web and edit the same Booth1
    Edge_driver = login_with_others()
    time.sleep(10)
    Edge_driver.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Edit the Booth.
    Booth1 = Edge_driver.find_element(By.XPATH, "//td[text()='booth1']/../td[3]/img")
    Booth1.click()
    time.sleep(3)
    Edge_driver.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys("for Update")
    Edge_driver.find_element(By.XPATH, "//input[@name='boothDescription']").send_keys(Keys.ENTER)
    time.sleep(2)
    # user1 click apply
    browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    # user2 click apply
    Edge_driver.find_element(By.XPATH, "//button[text()='Apply']").click()
    message = BaseFun(Edge_driver).get_AlterMessage()
    assert "E4125: Another user has changed the data, you must perform a refresh from the server." in message


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS31310.py"])
