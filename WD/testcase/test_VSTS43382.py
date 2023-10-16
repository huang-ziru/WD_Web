# coding = utf-8
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.baseFun import BaseFun


def test_order_add_material(browser):
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to order page and Create campaign
    # test1
    browser.find_element(By.XPATH, "//tr/td/div[text()='Order']").click()
    time.sleep(5)
    #  select a order
    i = 0
    while i in range(10):
        try:
            browser.find_element(By.XPATH, "//td[text()='test3']")
        except NoSuchElementException:
            browser.find_element(By.XPATH, "//a[text()='Refresh']").click()
            time.sleep(3)
        i = i + 1
    time.sleep(3)
    select_order = browser.find_element(By.XPATH, "//td[text()='test3']")
    time.sleep(3)
    select_order.find_element(By.XPATH, "..//td/span[@class='gwt-CheckBox']").click()
    time.sleep(3)
    status = select_order.find_element(By.XPATH, "../td[7]").text
    time.sleep(3)
    # active order
    if status == "Planned":
        browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style OrderActivate_Image']").click()
        time.sleep(3)
    assert "Active" == select_order.find_element(By.XPATH, "../td[7]").text
    time.sleep(3)
    # check sequence
    force_sequence = browser.find_element(By.XPATH, "//*[@id='clicked_Row_Style']/td[15]").text
    result = ["Yes", "No"]
    assert force_sequence in result
    # click Create campaign
    browser.find_element(By.XPATH, "//button[@class='WDAnchor_Common_Image16_Style CreateCampaign_Image']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@class='WD_TextBox']").send_keys("CampaignMaterial")
    time.sleep(3)
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(8)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(3)
    # 2. add material
    select_order.find_element(By.XPATH, "../td/img").click()
    time.sleep(3)
    origin_materails = browser.find_elements(By.XPATH, "//a[text()='Material']/../../../../../../../../../../../../tr/td[@class='Inner_Column_Left'][2]")
    oms = []
    for om in origin_materails:
        oms.append(om.text)
        # print(oms)
    # check yes/no Allow multiple lots per order
    lots = browser.find_elements(By.XPATH, "//table[@class='Order_Table_body_Style_Collapse']/tbody/tr/td[@class='Inner_Column_Left'][24]")
    for lot in lots:
        assert lot.get_attribute('innerHTML') in result
    time.sleep(3)
    browser.find_element(By.XPATH, "//a[text()='Add a Material']").click()
    time.sleep(3)
    # need change message after defect791570 fix
    message = "This order test3 currently belongs to campaign"
    # print(BaseFun(browser).get_AlterMessage())
    assert message in BaseFun(browser).get_AlterMessage()
    # 3.select material
    material = Select(browser.find_element(By.XPATH, "//div[text()='Material:']/../..//select"))
    quantity = browser.find_element(By.XPATH, "//div[text()='Quantity:']/../..//input")
    sequence = browser.find_element(By.XPATH, "//div[text()='Sequence:']/../..//input")
    time.sleep(3)
    # check BOM material
    select_materials = material.all_selected_options
    for sm in select_materials:
        print(sm.text.split(' ')[1])
        assert sm.text.split(' ')[1] in oms
    material.select_by_value("1072")
    time.sleep(3)
    # 4.input quantity
    num = "100"
    quantity.send_keys(num)
    time.sleep(3)
    # 5.check sequence is automatic generated
    assert not sequence.is_enabled()
    print(sequence.get_attribute("value"))
    assert "3-004" == sequence.get_attribute("value")
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Add Material']").click()
    time.sleep(5)
    # check quantity
    added_num = browser.find_element(By.XPATH,"//td[text()='3-004']/../td[@class='Inner_Column_Right'][2]").text
    assert num == added_num
    print(added_num)
    # 6.cancel apply
    browser.find_element(By.XPATH, "//table[@class='Edit_Panel']/tbody/tr/td/table/tbody/tr[2]//button[text()='Cancel']").click()
    time.sleep(3)
    assert "Do you want to discard the changes?" in BaseFun(browser).get_AlterMessage()
    # check no change the order
    select_order = browser.find_element(By.XPATH, "//td[text()='test3']")
    time.sleep(3)
    select_order.find_element(By.XPATH, "../td/img").click()
    time.sleep(3)
    cancel_sequences = browser.find_elements(By.XPATH, "//a[text()='Material']/../../../../../../../../../../../../tr/td[@class='Inner_Column_Left'][1]")
    for cs in cancel_sequences:
        print(cs.text)
        assert cs.text in ["1", "2", "3","4"]
    # test2
    time.sleep(3)
    # 2.add material
    browser.find_element(By.XPATH, "//a[text()='Add a Material']").click()
    time.sleep(3)
    # need change message after defect791570 fix
    message = "This order test3 currently belongs to campaign"
    assert message in BaseFun(browser).get_AlterMessage()
    # 3.select material
    material = Select(browser.find_element(By.XPATH, "//div[text()='Material:']/../..//select"))
    quantity = browser.find_element(By.XPATH, "//div[text()='Quantity:']/../..//input")
    sequence = browser.find_element(By.XPATH, "//div[text()='Sequence:']/../..//input")
    time.sleep(3)
    # check BOM material
    select_materials = material.all_selected_options
    for sm in select_materials:
        assert sm.text.split(' ')[1] in oms
    material.select_by_value("X0125")
    time.sleep(3)
    # 4.input quantity
    num = "100"
    quantity.send_keys(num)
    time.sleep(3)
    # 5.check sequence is automatic generated
    assert not sequence.is_enabled()
    assert "1-004" == sequence.get_attribute("value")
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Add Material']").click()
    time.sleep(3)
    Alert_message = BaseFun(browser).get_AlterMessage()
    # print(Alert_message)
    assert "The selected material cannot be added again since it is the Main ingredient!" in Alert_message
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[text()='Close']").click()
    time.sleep(3)
    # 6.cancel apply
    browser.find_element(By.XPATH, "//table[@class='Edit_Panel']/tbody/tr/td/table/tbody/tr[2]//button[text()='Cancel']").click()
    time.sleep(3)
    # check no change the order
    select_order = browser.find_element(By.XPATH, "//td[text()='test3']")
    time.sleep(3)
    # browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    # time.sleep(3)
    select_order.find_element(By.XPATH, "../td/img").click()
    time.sleep(3)
    cancel_sequences = browser.find_elements(By.XPATH, "//a[text()='Material']/../../../../../../../../../../../../tr/td[@class='Inner_Column_Left'][1]")
    for cs in cancel_sequences:
        print(cs.text)
        assert cs.text in ["1", "2", "3","4"]
    # delete the campaign
    browser.find_element(By.XPATH, "//tr/td/div[text()='Campaigns']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "//td[text()='CampaignMaterial']/../td[10]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[@class='gwt-Button OkStyle']").click()
    time.sleep(2)


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS43382.py"])
