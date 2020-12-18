import sys
import pytest
from selenium import webdriver
from time import sleep

sys.path.append("..")
from page.login_page import LoginPage
from page.setting_page import SettingPage


class TestSetting:
    url = r"http://183.60.104.92:8000/#/"
    sleep_time = 3

    # ==========Fixture==========
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.Login_Page = LoginPage(self.driver)
        self.Setting_Page = SettingPage(self.driver)
        self.driver.maximize_window()
        self.Login_Page.get(self.url + r"login")
        self.Login_Page.user_input = "test"
        self.Login_Page.password_input = "123456zxA"
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        self.Login_Page.select_hospital.click()
        self.Login_Page.select_ensure.click()
        sleep(self.sleep_time)
        self.Setting_Page.setting_button.click()
        sleep(self.sleep_time)
        pass

    def teardown_class(self):
        self.driver.close()
        pass

    # 医耗宝供应商进入设置界面测试用例
    def test_to_setting(self):
        assert self.driver.current_url == self.url + r"setting/setBasic/company"
        pass

    # 医耗宝供应商进入基本设置界面测试用例
    def test_to_set_basic(self):
        self.Setting_Page.set_basic.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"setting/setBasic/company"
        pass

    # 医耗宝供应商进入基本设置-公司信息界面测试用例
    def test_to_set_basic_company(self):
        self.Setting_Page.set_basic.click()
        self.Setting_Page.set_basic_company.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"setting/setBasic/company"
        pass

    # 医耗宝供应商进入基本设置-账号管理测试用例
    def test_to_set_basic_account(self):
        self.Setting_Page.set_basic.click()
        self.Setting_Page.set_basic_account.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"setting/setBasic/account"
        pass

    # 医耗宝供应商进入会员充值界面测试用例
    def test_to_set_vip(self):
        self.Setting_Page.set_vip.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"setting/vip"
        pass

    # 医耗宝供应商进入消费记录界面测试用例
    def test_to_consumption_records(self):
        self.Setting_Page.consumption_records.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"setting/consumptionRecords"
        pass
    pass


if __name__ == '__main__':
    pytest.main(["test_setting.py::TestSetting"])
    pass
