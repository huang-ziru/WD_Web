# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select
from selenium import webdriver
from common.baseFun import BaseFun
from pages.Equipment import EquipmentPage
import configparser


def test_delete_scale_two_user(browser):
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to Equipment page
    EquipmentPage(browser).go_to_Equipment()
    time.sleep(5)
    # 2.add a scale
    browser.find_element(By.XPATH, "//a[text()='Add a Scale']").click()
    time.sleep(3)
    minRange = browser.find_element(By.NAME, "minRange")
    maxRange = browser.find_element(By.NAME, "maxRange")
    minTare = browser.find_element(By.NAME, "minTare")
    maxTare = browser.find_element(By.NAME, "maxTare")
    status = Select(browser.find_element(By.NAME, "statusValue"))
    minRange.send_keys("1")
    time.sleep(3)
    maxRange.send_keys("300")
    time.sleep(3)
    minTare.send_keys("1")
    time.sleep(3)
    maxTare.send_keys("100")
    time.sleep(3)
    status.select_by_value("Scale_Maintain")
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(5)
    edge = webdriver.Edge()
    edge.maximize_window()
    config = configparser.ConfigParser()
    path = r'..\data\config.ini'
    config.read(path)
    servername = config.get('login', 'servername')
    username = config.get('login', 'username')
    password = config.get('login', 'password')
    url = "http://" + servername + "/WeighDispense/"
    edge.get(url)
    time.sleep(5)
    edge.find_element(By.XPATH, "//input[@class='gwt-TextBox']").click()
    edge.find_element(By.XPATH, "//input[@class='gwt-TextBox']").send_keys(username)
    edge.find_element(By.XPATH, "//input[@class='gwt-PasswordTextBox']").send_keys(password)
    edge.find_element(By.XPATH, "//button[@class='Home_Login_Button']").click()
    time.sleep(10)
    EquipmentPage(edge).go_to_Equipment()
    time.sleep(5)
    # 4.delete a scale
    scales = edge.find_element(By.XPATH, "//td[text()='<TEMP>']/../td[18]/img")
    scales.click()
    time.sleep(3)
    text = "Are you sure you want to delete scale"
    message = BaseFun(edge).get_AlterMessage()
    assert text in message
    edge.quit()
    # 5. return to user1 and delete scale
    time.sleep(3)
    editScale = browser.find_element(By.XPATH, "//td[text()='<TEMP>']/../td[18]/img")
    editScale.click()
    time.sleep(3)
    message2 = BaseFun(browser).get_AlterMessage()
    assert text in message2
    time.sleep(8)
    text2 = "E4125: Another user has changed the data, you must perform a refresh from the server."
    message3 = BaseFun(browser).get_AlterMessage()
    assert text2 == message3


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41360.py"])
