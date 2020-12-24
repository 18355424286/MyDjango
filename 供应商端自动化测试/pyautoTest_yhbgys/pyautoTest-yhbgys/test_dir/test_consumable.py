import sys
import pytest
from selenium import webdriver
from time import sleep

sys.path.append("..")
from page.login_page import LoginPage
# from page.index_page import IndexPage
from page.consumable_page import ConsumablePage


class TestConsumable:
    url = "http://183.60.104.92:8000/#/"
    sleep_time = 3

    # ==========Fixture==========
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.Login_Page = LoginPage(self.driver)
        self.Consumable_Page = ConsumablePage(self.driver)
        self.driver.maximize_window()
        self.Login_Page.get(self.url + r"login")
        self.Login_Page.user_input = "test"
        self.Login_Page.password_input = "123456zxA"
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        self.Login_Page.select_hospital.click()
        self.Login_Page.select_ensure.click()
        sleep(self.sleep_time)
        self.Consumable_Page.consumable_button.click()
        sleep(self.sleep_time)
        pass

    def teardown_class(self):
        self.driver.close()
        pass

    # 医耗宝供应商进入耗材界面测试用例
    def test_to_consumable(self):
        assert self.driver.current_url == self.url + r"consumable/currentStocks"
        pass

    # 医耗宝供应商进入耗材-当前库存界面测试用例
    def test_current_inventory(self):
        self.Consumable_Page.current_inventory.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/currentStocks"
        pass

    # 医耗宝供应商进入耗材-数据报表界面测试用例
    def test_data_report(self):
        self.Consumable_Page.data_report.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/dataReport/inventoryRATIO"
        pass

    # 医耗宝供应商进入耗材-数据报表-存货量界面测试用例
    def test_data_report_inventory(self):
        self.Consumable_Page.data_report.click()
        self.Consumable_Page.data_report_inventory.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/dataReport/inventoryRATIO"
        pass

    # 医耗宝供应商进入耗材-数据报表-使用量界面测试用例
    def test_data_report_usage(self):
        self.Consumable_Page.data_report.click()
        self.Consumable_Page.data_report_usage.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/dataReport/utilizationRate"
        pass

    # 医耗宝供应商进入耗材-数据报表-订货量界面测试用例
    def test_data_report_order(self):
        self.Consumable_Page.data_report.click()
        self.Consumable_Page.data_report_order.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/dataReport/orderRate"
        pass

    # 医耗宝供应商进入耗材-数据报表-退货量界面测试用例
    def test_data_report_return(self):
        self.Consumable_Page.data_report.click()
        self.Consumable_Page.data_report_return.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/dataReport/returnRate"
        pass

    # 医耗宝供应商进入耗材-数据报表-近效耗材界面测试用例
    def test_data_report_recent(self):
        self.Consumable_Page.data_report.click()
        self.Consumable_Page.data_report_recent.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/dataReport/nearArticle"
        pass

    # 医耗宝供应商进入耗材-耗材管理界面测试用例
    def test_material_management(self):
        self.Consumable_Page.material_management.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/management/whole"
        pass

    # 医耗宝供应商进入耗材-耗材管理-全部耗材界面测试用例
    def test_material_management_all(self):
        self.Consumable_Page.material_management.click()
        self.Consumable_Page.material_management_all.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/management/whole"
        pass

    # 医耗宝供应商进入耗材-耗材管理-在售耗材界面测试用例
    def test_material_management_sale(self):
        self.Consumable_Page.material_management.click()
        self.Consumable_Page.material_management_sale.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/management/onSale"
        pass

    # 医耗宝供应商进入耗材-耗材管理-停售耗材界面测试用例
    def test_material_management_halt_sale(self):
        self.Consumable_Page.material_management.click()
        self.Consumable_Page.material_management_halt_sale.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/management/haltSale"
        pass

    # 医耗宝供应商进入耗材-耗材管理-审核中耗材界面测试用例
    def test_material_management_review(self):
        self.Consumable_Page.material_management.click()
        self.Consumable_Page.material_management_review.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/management/notApprove"
        pass

    # 医耗宝供应商进入耗材-耗材管理-通过耗材界面测试用例
    def test_material_management_approved(self):
        self.Consumable_Page.material_management.click()
        self.Consumable_Page.material_management_approved.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/management/pass"
        pass

    # 医耗宝供应商进入耗材-耗材管理-通过耗材界面测试用例
    def test_material_management_unapproved(self):
        self.Consumable_Page.material_management.click()
        self.Consumable_Page.material_management_unapproved.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/management/refuse"
        pass
    pass


if __name__ == '__main__':
    pytest.main(["test_consumable.py::TestConsumable"])