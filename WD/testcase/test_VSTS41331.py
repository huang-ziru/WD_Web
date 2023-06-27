# coding = utf-8
import time
import pytest
from selenium.webdriver.common.by import By
from pages.Administration import AdministrationPage
from pages.Equipment import EquipmentPage
from common.baseFun import BaseFun


def test_Scale_info_no_modify(browser):
    # add all permission
    BaseFun(browser).grant_Allpermission()
    # 1.Navigate to Permission page and change no modify
    AdministrationPage(browser).go_to_administration()
    browser.find_element(By.XPATH, "//div[text()='Permissions']").click()
    time.sleep(3)
    permission = browser.find_elements(By.XPATH, "//label[text() ='Add+modify']/../input")[1]
    if permission.is_selected():
        permission.click()
        time.sleep(1)
    apply = browser.find_element(By.XPATH, "//button[text()='Apply']")
    if apply.is_enabled():
        apply.click()
        time.sleep(3)
        # Check apply successfully
        assert "Apply Permission Successful" in BaseFun(browser).get_AlterMessage()
    # 2.Navigate to Equipment page
    EquipmentPage(browser).go_to_Equipment()
    # 3.check the state is disabled
    scales = browser.find_elements(By.XPATH, "//table[@class='List_Table_Border_Style']")
    editScale = scales[1].find_elements(By.TAG_NAME,  "img")
    editScale[2].click()
    time.sleep(3)
    description = browser.find_element(By.NAME, "description")
    brand = browser.find_element(By.NAME, "brand")
    model = browser.find_element(By.NAME, "model")
    serialId = browser.find_element(By.NAME, "serialId")
    minRange = browser.find_element(By.NAME, "minRange")
    maxRange = browser.find_element(By.NAME, "maxRange")
    precision = browser.find_element(By.NAME, "precision")
    minTare = browser.find_element(By.NAME, "minTare")
    maxTare = browser.find_element(By.NAME, "maxTare")
    boothTag = browser.find_element(By.NAME, "boothTag")
    comAddress = browser.find_element(By.NAME, "comAddress")
    comProtocol = browser.find_element(By.NAME, "comProtocol")
    time.sleep(3)
    if not description.is_enabled() and not brand.is_enabled() and not model.is_enabled() \
            and not serialId.is_enabled() and not minRange.is_enabled() and not maxRange.is_enabled() \
            and not precision.is_enabled() and not minTare.is_enabled() and not maxTare.is_enabled() \
            and not boothTag.is_enabled() and not comAddress.is_enabled() and not comProtocol.is_enabled():
        result = True
    else:
        result = False
    assert result


if __name__ == '__main__':
    pytest.main(["-s", "test_VSTS41331.py"])
