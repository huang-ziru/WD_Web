# coding = utf-8
import time, os
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.Administration import AdministrationPage


def test_print_picture(browser):
    # 1.Navigate to administration page
    AdministrationPage(browser).go_to_administration()
    # 2.Select Permissions
    browser.find_element(By.XPATH, "//div[text()='Printing']").click()
    time.sleep(3)
    # 3.Choose picture
    picture = browser.find_element(By.XPATH, "//input[@name='Image']")
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("WD\\") + len("WD\\")]
    print(rootPath + "resource\\picture\\aspenLogo.png")
    picture_path = rootPath + "resource\\picture\\aspenLogo.png"
    # picture_path = r'..\..\resource\picture\aspenLogo.png'
    print(picture_path)
    picture.send_keys(picture_path)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    time.sleep(3)
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 4.Check picture upload success
    try:
        img = browser.find_element(By.XPATH, "//img[@class='Image_LogoImage_Style']")
        result = True
    except NoSuchElementException:
        result = False

    assert result, picture.text == "aspenLogo.png"


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS43369.py"])
