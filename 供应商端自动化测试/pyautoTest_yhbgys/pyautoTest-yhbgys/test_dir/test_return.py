import sys
import pytest
from selenium import webdriver
from time import sleep

sys.path.append("..")
from page.login_page import LoginPage
# from page.index_page import IndexPage
from page.return_page import ReturnPage


class TestReturn:
    url = "http://183.60.104.92:8000/#/"
    sleep_time = 3

    # ==========Fixture==========
    def setup_class(self):
        print(self.url + "-------------------------------------------------------" + str(type(self.url)))
        self.driver = webdriver.Chrome()
        self.Login_Page = LoginPage(self.driver)
        self.Return_Page = ReturnPage(self.driver)
        self.driver.maximize_window()
        self.Login_Page.get(self.url + r"login")
        self.Login_Page.user_input = "test"
        self.Login_Page.password_input = "123456zxA"
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        self.Login_Page.select_hospital.click()
        self.Login_Page.select_ensure.click()
        sleep(self.sleep_time)
        self.Return_Page.return_button.click()
        sleep(self.sleep_time)
        pass

    def teardown_class(self):
        self.driver.close()
        pass

    # 医耗宝供应商进入退货界面测试用例
    def test_to_return(self):
        # sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"approval/returnGoodsApproved/returnGoodsApproved"
        pass

    # 医耗宝供应商进入退货管理界面测试用例
    def test_to_return_manage(self):
        self.Return_Page.return_manage.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"approval/returnGoodsApproved/returnGoodsApproved"
        pass

    # 医耗宝供应商进入退货管理-待审核界面测试用例
    def test_to_return_manage_approved(self):
        self.Return_Page.return_manage.click()
        self.Return_Page.return_manage_approved.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"approval/returnGoodsApproved/returnGoodsApproved"
        pass

    # 医耗宝供应商进入退货管理-审核记录界面测试用例
    def test_to_return_manage_record(self):
        self.Return_Page.return_manage.click()
        self.Return_Page.return_manage_record.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"approval/returnGoodsApproved/approvedRecord"
        pass

    # 医耗宝供应商进入退货记录管理界面测试用例
    def test_to_return_record(self):
        self.Return_Page.return_record.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"approval/returnRecordList"
        pass
    pass


if __name__ == '__main__':
    pytest.main(["test_return.py::TestReturn"])
    pass
