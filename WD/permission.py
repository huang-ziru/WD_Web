import os, sys
from logging import Logger
import configparser
import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def open_Chrome():
    config = configparser.ConfigParser()
    path = r'data\config.ini'
    # open the config.ini and get the data
    config.read(path)
    s = Service(r'data\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    # driver = webdriver.(r'..\data\msedgedriver.exe')
    driver.maximize_window()
    servername = config.get('login', 'servername')
    url = "http://" + servername + "/WeighDispense/"
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@class='gwt-TextBox']").click()
    driver.find_element(By.XPATH, "//input[@class='gwt-TextBox']").send_keys("apem-c-d6\\administrator")
    driver.find_element(By.XPATH, "//input[@class='gwt-PasswordTextBox']").send_keys("Aspen100")
    driver.find_element(By.XPATH, "//button[@class='Home_Login_Button']").click()
    time.sleep(10)
    return driver


def grant_Allpermission(driver):
    driver.find_element(By.XPATH, "//div[text()='Administration']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(3)
    # 3.Grant all permission
    inputs = driver.find_elements(By.XPATH, "//input[@type ='checkbox']")
    for input in inputs:
        if not input.is_selected():
            input.click()
            time.sleep(1)
    # 4.Apply
    apply = driver.find_element(By.XPATH, "//button[text()='Apply']")
    time.sleep(3)
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(5)


def import_XML():
    os.system(r"C:\\p4\\WD_Web\\WD\\importxml.bat")
    time.sleep(5)


webdriver = open_Chrome()

grant_Allpermission(webdriver)

import_XML()
