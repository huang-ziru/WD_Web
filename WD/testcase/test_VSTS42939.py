# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from common.baseFun import BaseFun

def test_Modifymaterials(browser):
    time.sleep(5)
    BaseFun(browser).grant_Allpermission()
    browser.find_element(By.XPATH, "//tr/td/div[text()='Material']").click()
    # edit the pending BOM
    time.sleep(5)
    browser.find_elements(By.XPATH, "//td[text()='Pending']/../td[6]/img")[1].click()
    time.sleep(3)
    # Description, type and Code are not edited
    disable_ele = browser.find_elements(By.XPATH, "//table[@class='Edit_Sub_Panel']//td[@class='Edit_Cell']/div[@class='gwt-Label']/../../td[1]/div")
    for disable in disable_ele:
        assert disable.text.replace(' ', '') in ["Description:", "Code:", "Type:"]
    # modify the characteristics
    # modify ToKG
    browser.find_element(By.XPATH, "//input[@name='toKg']").clear()
    browser.find_element(By.XPATH, "//input[@name='toKg']").send_keys("1")
    # modify NFPA 704 Health
    browser.find_element(By.NAME, "nfpaHealth").click()
    browser.find_element(By.XPATH, "//option[@value='0']").click()
    # modify NFPA 704 Special
    browser.find_element(By.NAME, "nfpaSpecial").click()
    browser.find_element(By.XPATH, "//option[@value='ACID']").click()
    # modify weigh notes
    browser.find_element(By.XPATH, "//input[@name='weighNote']/../../td[2]/button").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//textarea[@class='NoteDialogTextArea']").clear()
    browser.find_element(By.XPATH, "//textarea[@class='NoteDialogTextArea']").send_keys("Weigh Notes")
    browser.find_element(By.ID, "Dialogbox_Bottom_OK_Button_Id").click()
    time.sleep(3)
    browser.find_element(By.ID, "edit_save_Button").click()
    time.sleep(2)
    assert "Save was successful!" in BaseFun(browser).get_AlterMessage()
    # modify the other status
    browser.find_elements(By.XPATH, "//td[text()='In Use']/../td[6]")[1].click()
    time.sleep(3)
    assert browser.find_element(By.XPATH, "//select[@name='nfpaHealth']").get_property("disabled") is True




if __name__ == '__main__':

    pytest.main(["-s", "test_VSTS42939.py"])






