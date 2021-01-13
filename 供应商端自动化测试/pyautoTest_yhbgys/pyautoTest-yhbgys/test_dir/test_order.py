import sys
import pytest
from selenium import webdriver
from time import sleep

sys.path.append("..")
from page.login_page import LoginPage
# from page.index_page import IndexPage
from page.order_page import OrderPage


class TestAllOrder:
    url = "http://183.60.104.92:8000/#/"
    sleep_time = 3

    # ==========Fixture==========
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.Login_Page = LoginPage(self.driver)
        self.Order_Page = OrderPage(self.driver)
        self.driver.maximize_window()
        self.Login_Page.get(self.url + r"login")
        self.Login_Page.user_input = "test"
        self.Login_Page.password_input = "123456zxA"
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        self.Login_Page.select_hospital.click()
        self.Login_Page.select_ensure.click()
        sleep(self.sleep_time)
        self.Order_Page.order_button.click()
        sleep(self.sleep_time)
        pass

    def teardown_class(self):
        self.driver.close()
        pass

    # 医耗宝供应商进入订单界面测试用例
    def test_to_order(self):
        assert self.driver.current_url == self.url + r"order/untreated/untreatedAll"
        pass

    # 医耗宝供应商订单界面未完成-未处理测试用例
    def test_unfinished_untreated(self):
        self.Order_Page.unfinished_button.click()
        self.Order_Page.untreated_order_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/untreated/untreatedAll"
        pass

    # 医耗宝供应商订单界面未完成-备货中测试用例
    def test_unfinished_prepare(self):
        self.Order_Page.unfinished_button.click()
        self.Order_Page.prepare_order_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/untreated/untreatedPrepare"
        pass

    # 医耗宝供应商订单界面未完成-配送中测试用例
    def test_unfinished_distribution(self):
        self.Order_Page.unfinished_button.click()
        self.Order_Page.distribution_order_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/untreated/untreatedDistribution"
        pass

    # 医耗宝供应商订单界面未完成-未完结测试用例
    def test_unfinished_unfinished(self):
        self.Order_Page.unfinished_button.click()
        self.Order_Page.unfinished_order_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/untreated/untreatedDesear"
        pass

    # 医耗宝供应商订单界面已完成测试用例
    def test_finished(self):
        self.Order_Page.finished_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/delivery"
        pass

    # 医耗宝供应商订单界面已撤回测试用例
    def test_paid(self):
        self.Order_Page.paid_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/achieve"
        pass

    pass


if __name__ == '__main__':
    pytest.main(["test_order.py::TestAllOrder"])
