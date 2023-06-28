# coding = utf-8
import configparser
import os
import time
import pytest
from selenium.webdriver.common.by import By


def test_help_about(browser):
    # 获取config
    config = configparser.ConfigParser()
    path = r'..\data\config.ini'
    config.read(path)
    newfilename = config.get('version', 'OSSNotes')
    newversion = config.get('version', 'version')
    # 1.open help about
    browser.find_element(By.XPATH, "//tr/td/div[text()='About...']").click()
    time.sleep(5)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    # check the version and content(about OSS doc)
    version = browser.find_element(By.XPATH, "//div[@class='about-info']/div/span").text
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\809632.png")
    assert version == newversion
    # 2.Check the "OSSNotesV14.txt" under folder Program Files and Program Files (x86)
    # the file is on server
    path1 = "C:\\Program Files\\Common Files\\AspenTech Shared"
    path2 = "C:\\Program Files (x86)\\Common Files\\AspenTech Shared"
    # path1 = "D:\\WD"
    # path2 = "D:\\WD (x86)"
    files1 = os.listdir(path1)
    files2 = os.listdir(path2)
    filename = newfilename
    # 查找文件名字是f且以.txt后缀的文件
    result1 = False
    result2 = False
    for f in files1:
        if f == filename:
            print(f)
            result1 = True
            break
    for f in files2:
        if f == filename:
            print(f)
            result2 = True
            break
    assert result1 and result2


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS809632.py"])