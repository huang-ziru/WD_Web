# coding = utf-8
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def test_create_machine_name(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Equipment']").click()
    time.sleep(10)
    # Edit the Booth1.
    Booth1 = browser.find_element(By.XPATH, "//td[text()='booth1']/../td[3]/img")
    Booth1.click()
    time.sleep(3)
    # Click the button near the machine name.
    browser.find_element(By.XPATH, "//select[@name='workstation']/../../td[2]/button").click()
    # In the Workstation Dialog window, input a machine name in the Workstation column.
    browser.find_elements(By.XPATH, "//div[@class='dialogMiddleCenterInner dialogContent']//table[@class='List_Table_Border_Style']/tbody/tr")[-1].click()
    testWorkstation = BaseFun(browser).Random_Str(8)
    browser.find_element(By.XPATH, "//*[@id='clicked_Row_Style']/td[1]/input").send_keys(testWorkstation)
    browser.find_element(By.XPATH, "//*[@id='clicked_Row_Style']/td[2]/input").send_keys("for test")
    browser.find_element(By.XPATH, "//*[@id='clicked_Row_Style']/td[2]/input").send_keys(Keys.ENTER)
    # Select a Role and click the ok button
    browser.find_element(By.XPATH, "//*[@id='clicked_Row_Style']/td[3]/select").click()
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(5)
    browser.find_element(By.NAME, "workstation").click()
    time.sleep(3)
    workstation_name1 = []
    workstations1 = browser.find_elements(By.XPATH, "//select[@name='workstation']/option")
    for workstation_ele in workstations1:
        workstation_name1.append(workstation_ele.text)
    assert testWorkstation in workstation_name1
    # Click the button near the machine name.
    browser.find_element(By.XPATH, "//select[@name='workstation']/../../td[2]/button").click()
    # In the Workstation Dialog window, delete a machine name
    workstationName_list = browser.find_elements(By.XPATH, "//input[@name='WorkStation_Name']")
    for num in range(len(workstationName_list) - 1):
        if workstationName_list[num].get_property("value") == testWorkstation:
            workstationPath = "//div[@class='dialogMiddleCenterInner dialogContent']//table[@class='List_Table_Border_Style']/tbody/tr[" + str(num + 2) + "]/td[4]/img"
            browser.find_element(By.XPATH, workstationPath).click()
            break
    # click OK button
    time.sleep(3)
    Ok_button = browser.find_elements(By.XPATH, "//button[@class='gwt-Button OkStyle']")
    browser.execute_script("arguments[0].click();", Ok_button[1])
    time.sleep(2)
    dialog_OK = browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id")
    browser.execute_script("arguments[0].click();", dialog_OK)
    # 'Workstation dialog' will be closed. And can't see the machine name we
    # delete under the machine name drop down box.
    time.sleep(3)
    browser.find_element(By.NAME, "workstation").click()
    time.sleep(3)
    workstation_name2 = []
    workstations2 = browser.find_elements(By.XPATH, "//select[@name='workstation']/option")
    for workstation_ele in workstations2:
        workstation_name2.append(workstation_ele.text)
    assert testWorkstation not in workstation_name2

if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS42821.py"])






