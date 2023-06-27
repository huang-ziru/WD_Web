# coding = utf-8
import random

from selenium.webdriver.common.by import By
import time
import os


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class BaseFun(BasePage):
    def is_element_showed(self, xpath):
        lenth = self.driver.find_elements(By.XPATH, xpath)
        if len(lenth) == 0:
            return False
        else:
            return True

    def get_AlterMessage(self):
        time.sleep(3)
        message = self.driver.find_element(By.XPATH, "//div[@class='gwt-Label Alert_Label']").text
        Ok_button = self.driver.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']")
        self.driver.execute_script("arguments[0].click();", Ok_button)
        time.sleep(5)
        return message

    def grant_Allpermission(self):
        self.driver.find_element(By.XPATH, "//div[text()='Administration']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[text()='Permissions']").click()
        time.sleep(3)
        # 3.Grant all permission
        inputs = self.driver.find_elements(By.XPATH, "//input[@type ='checkbox']")
        for input in inputs:
            if not input.is_selected():
                input.click()
                time.sleep(1)
        # 4.Apply
        apply = self.driver.find_element(By.XPATH, "//button[text()='Apply']")
        time.sleep(3)
        if apply.is_enabled():
            apply.click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
        time.sleep(5)

    def Assert_CSV(self, filename):
        path = "C:\\Users\\huangzi\\Downloads"
        files = os.listdir(path)
        # 查找文件名字含有fish且以.png后缀的文件
        for f in files:
            if filename in f and f.endswith('.csv'):
                return f
                break

    def Random_Str(self,randomlength=5):
        random_str = ''
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        length = len(base_str) - 1
        for i in range(randomlength):
            random_str += base_str[random.randint(0, length)]
        return random_str

