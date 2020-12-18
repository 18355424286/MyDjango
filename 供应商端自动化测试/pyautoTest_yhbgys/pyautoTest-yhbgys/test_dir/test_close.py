import sys
import pytest
from selenium import webdriver
from time import sleep

sys.path.append("..")
from page.login_page import LoginPage
from page.close_page import ClosePage
from basic_setting import BasicSetting


class TestClose:
    url = BasicSetting.url
    sleep_time = BasicSetting.sleep_time

    # ==========Fixture==========
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.Login_Page = LoginPage(self.driver)
        self.Close_Page = ClosePage(self.driver)
        self.driver.maximize_window()
        self.Login_Page.get(self.url + r"login")
        self.Login_Page.user_input = "test"
        self.Login_Page.password_input = "123456zxA"
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        self.Login_Page.select_hospital.click()
        self.Login_Page.select_ensure.click()
        sleep(self.sleep_time)
        self.Close_Page.close_button.click()
        sleep(self.sleep_time)
        pass

    def teardown_class(self):
        self.driver.close()
        pass

    # 医耗宝供应商进入结算界面测试用例
    def test_to_return(self):
        assert self.driver.current_url == self.url + r"close/closeApply"
        pass

    # 医耗宝供应商进入结算申请界面测试用例
    def test_to_close_apply(self):
        self.Close_Page.close_apply.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/closeApply"
        pass

    # 医耗宝供应商进入结算管理界面测试用例
    def test_to_close_course(self):
        self.Close_Page.close_course.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/course/courseAll"
        pass

    # 医耗宝供应商进入结算管理-全部界面测试用例
    def test_to_close_course_all(self):
        self.Close_Page.close_course.click()
        self.Close_Page.close_course_all.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/course/courseAll"
        pass

    # 医耗宝供应商进入结算管理-待审核界面测试用例
    def test_to_close_course_investigated(self):
        self.Close_Page.close_course.click()
        self.Close_Page.close_course_investigated.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/course/courseInvestigated"
        pass

    # 医耗宝供应商进入结算管理-审核中界面测试用例
    def test_to_close_course_examine(self):
        self.Close_Page.close_course.click()
        self.Close_Page.close_course_examine.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/course/courseExamine"
        pass

    # 医耗宝供应商进入结算管理-结算中界面测试用例
    def test_to_close_course_settlement(self):
        self.Close_Page.close_course.click()
        self.Close_Page.close_course_settlement.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/course/courseSettlement"
        pass

    # 医耗宝供应商进入结算管理-被驳回界面测试用例
    def test_to_close_course_return(self):
        self.Close_Page.close_course.click()
        self.Close_Page.close_course_return.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/course/courseReturn"
        pass

    # 医耗宝供应商进入结算记录界面测试用例
    def test_to_close_record(self):
        self.Close_Page.close_record.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/record/recordAll"
        pass

    # 医耗宝供应商进入结算记录-全部界面测试用例
    def test_to_close_record_all(self):
        self.Close_Page.close_record.click()
        self.Close_Page.close_record_all.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/record/recordAll"
        pass

    # 医耗宝供应商进入结算记录-已完成界面测试用例
    def test_to_close_record_completed(self):
        self.Close_Page.close_record.click()
        self.Close_Page.close_record_completed.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/record/recordCompleted"
        pass

    # 医耗宝供应商进入结算记录-已撤回界面测试用例
    def test_to_close_record_withdraw(self):
        self.Close_Page.close_record.click()
        self.Close_Page.close_record_withdraw.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"close/record/courseWithdraw"
        pass

    pass


if __name__ == '__main__':
    pytest.main(["test_close.py::TestClose"])
    pass
