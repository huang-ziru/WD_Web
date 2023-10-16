import os, sys
from logging import Logger
import configparser
import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
@pytest.fixture()
def browser():
    global driver
    config = configparser.ConfigParser()
    path = r'..\data\config.ini'
    # open the config.ini and get the data
    config.read(path)
    browser_name = config.get('Browser', 'browser')
    if browser_name == 'Chrome':
        s = Service(r'..\data\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
    elif browser_name == 'Edge':
        driver = webdriver.Edge(r'..\data\msedgedriver.exe')
        driver.maximize_window()
    else:
        Logger.error('Do not support the Browser')
    servername = config.get('login', 'servername')
    username = config.get('login', 'username')
    password = config.get('login', 'password')
    url = "http://" + servername + "/WeighDispense/"
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@class='gwt-TextBox']").click()
    driver.find_element(By.XPATH, "//input[@class='gwt-TextBox']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@class='gwt-PasswordTextBox']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@class='Home_Login_Button']").click()
    time.sleep(15)
    yield driver
    time.sleep(5)
    driver.quit()
    return driver

def login_with_others():
    config = configparser.ConfigParser()
    path = r'..\data\config.ini'
    # open the config.ini and get the data
    config.read(path)
    s = Service(r'..\data\msedgedriver.exe')
    driver = webdriver.Edge(service=s)
    # driver = webdriver.(r'..\data\msedgedriver.exe')
    driver.maximize_window()
    servername = config.get('login', 'servername')
    url = "http://" + servername + "/WeighDispense/"
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@class='gwt-TextBox']").click()
    driver.find_element(By.XPATH, "//input[@class='gwt-TextBox']").send_keys("qae\\qaone2")
    driver.find_element(By.XPATH, "//input[@class='gwt-PasswordTextBox']").send_keys("Aspen111")
    driver.find_element(By.XPATH, "//button[@class='Home_Login_Button']").click()
    time.sleep(10)
    return driver

