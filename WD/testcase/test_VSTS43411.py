# coding = utf-8
import datetime
import os
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun
from pages.Equipment import EquipmentPage

def test_manage_standardization_type(browser):
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to Equipment page
    EquipmentPage(browser).go_to_Equipment()
    # 2.add a scale
    browser.find_element(By.XPATH, "//a[text()='Add a Scale']").click()
    time.sleep(3)
    minRange = browser.find_element(By.NAME, "minRange")
    maxRange = browser.find_element(By.NAME, "maxRange")
    minTare = browser.find_element(By.NAME, "minTare")
    maxTare = browser.find_element(By.NAME, "maxTare")
    status = Select(browser.find_element(By.NAME, "statusValue"))
    minRange.send_keys("1")
    maxRange.send_keys("300")
    minTare.send_keys("1")
    maxTare.send_keys("100")
    status.select_by_value("Scale_Maintain")
    time.sleep(3)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # 3.add a standardization type
    time.sleep(3)
    editScale = browser.find_element(By.XPATH, "//td[text()='<TEMP>']/../td[3]/img")
    editScale.click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//a[text()='Add Type']").click()
    time.sleep(5)
    # rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
    # print(len(rows))
    cols = browser.find_element(By.XPATH, "//table[@class='Edit_Sub_Panel']/../../td[2]//tr[@class='List_Background_Color']/../tr[2]/td[1]")
    assert cols.text == "<TEMP>"
    # modify id
    # browser.find_element(By.XPATH, "//table[@class='Edit_Sub_Panel']/../../td[2]//tr[@class='List_Background_Color']/../tr[2]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[1]").click()
    # browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[1]/input").clear()
    browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[1]/input").send_keys("test ID")
    browser.find_element(By.XPATH, "//tr[@id='clicked_Row_Style']/td[1]/input").send_keys(Keys.ENTER)
    assert cols.text == "<TEMP>test ID"
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
    # attach PDF
    scales = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']")
    editScale = scales[1].find_elements(By.TAG_NAME,  "img")
    editScale[2].click()
    time.sleep(3)
    rows = browser.find_element(By.XPATH, "//td[text()='<TEMP>test ID']/..")
    img = rows.find_elements(By.TAG_NAME,  "img")
    print(len(img))
    img[0].click()
    time.sleep(3)
    PDF = browser.find_element(By.XPATH, "//input[@name='fileupload']")
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("WD\\") + len("WD\\")]
    pdf_path = rootPath + "resource\\PDF\\SOP1123_"
    PDF.send_keys(pdf_path)
    browser.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(3)
    assert "SOP1123_" == browser.find_element(By.XPATH, "//div[@class='gwt-Hyperlink']/a").text
    #  Expiration period
    cols = rows.find_elements(By.TAG_NAME,  "td")
    cols[5].click()
    time.sleep(3)
    Period = browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[-1]
    Period.clear()
    Period.send_keys("999")
    Period.send_keys(Keys.ENTER)
    time.sleep(3)
    assert cols[5].text == "999"
    # edit button
    img[1].click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//a[text()='Add Weight']").click()
    # weight_rows = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']/tbody/tr")
    # print(len(weight_rows))

    weight_rows = browser.find_elements(By.XPATH,
                                "//table[@class='Edit_Sub_Panel']/../../td[2]//tr[@class='List_Background_Color']/../tr[2]")
    weight_cols = weight_rows[1].find_elements(By.TAG_NAME,  "td")
    print(len(weight_cols))
    assert weight_cols[0].text == "<TEMP>"
    # input description, min and max.
    weight_cols[1].click()
    time.sleep(3)
    description = browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[-1]
    description.send_keys("test description")
    description.send_keys(Keys.ENTER)
    weight_cols[2].click()
    time.sleep(3)
    min_weight = browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[-1]
    min_weight.send_keys("10")
    time.sleep(3)
    min_weight.send_keys(Keys.ENTER)
    time.sleep(3)
    weight_cols[3].click()
    time.sleep(3)
    max_weight = browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[-1]
    time.sleep(3)
    max_weight.send_keys("1000")
    time.sleep(3)
    max_weight.send_keys(Keys.ENTER)
    time.sleep(3)
    assert weight_cols[1].text == "test description"
    assert weight_cols[2].text == "10"
    assert weight_cols[3].text == "1000"
    # time.sleep(3)
    # browser.find_element(By.XPATH, "//button[text()='Apply']").click()
    # apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    # if apply.is_enabled():
    #     apply.click()
    #     time.sleep(3)
    # add last check date
    # scales = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']")
    # editScale = scales[1].find_elements(By.TAG_NAME,  "img")
    # editScale[2].click()
    # time.sleep(3)
    rows = browser.find_element(By.XPATH, "//td[text()='<TEMP>test ID']/..")
    cols = rows.find_elements(By.TAG_NAME,  "td")
    print(len(cols))
    # modify last check date
    cols[6].click()
    time.sleep(3)
    CheckDate = browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[-1]
    CheckDate.clear()
    CheckDate.send_keys("4/1/22, 12:00:00 PM")
    CheckDate.send_keys(Keys.ENTER)
    time.sleep(3)
    # cols[5].click()
    # time.sleep(3)
    # Period = browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[-1]
    # Period.clear()
    # Period.send_keys("999")
    # Period.send_keys(Keys.ENTER)
    # time.sleep(3)
    Period = float(cols[5].text)
    # date1 = cols[6].text.split(',')[0]
    # date1 = date1.split('/')
    # date1 = "20"+date1[2]+"-"+date1[0]+"-"+date1[1]
    # date2 = cols[7].text.split(',')[0]
    # date2 = date2.split('/')
    # date2 = "20" + date2[2] + "-" + date2[0] + "-" + date2[1]
    # date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    # print(date1)
    # date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    date1 = datetime.datetime.strptime(cols[6].text, "%m/%d/%y, %I:%M:%S %p")
    date2 = datetime.datetime.strptime(cols[7].text, "%m/%d/%y, %I:%M:%S %p")
    print(date1)
    date1 = date1 + datetime.timedelta(days=Period)
    assert date1 == date2

    # 4.can't modify expiration date.
    cols[7].click()
    time.sleep(3)
    print(browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[-1].text)
    assert not cols[7].text == browser.find_elements(By.XPATH, "//input[@class='WD_TextBox']")[-1].text
    # apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    # if apply.is_enabled():
    #     apply.click()
    #     time.sleep(3)
    # 5.delete the scale
    scales2 = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']")
    editScale2 = scales2[1].find_elements(By.TAG_NAME,  "img")
    editScale2[3].click()
    time.sleep(3)
    text1 = "Do you want to discard the changes?"
    message1 = BaseFun(browser).get_AlterMessage()
    time.sleep(3)
    # browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']")[1].find_elements(By.TAG_NAME,  
    # "img")[3].click()
    editScale2[3].click()
    time.sleep(3)
    text2 = "Are you sure you want to delete scale \"<TEMP>\"?"
    message2 = BaseFun(browser).get_AlterMessage()
    assert text1 == message1, text2 == message2


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS43411.py"])
