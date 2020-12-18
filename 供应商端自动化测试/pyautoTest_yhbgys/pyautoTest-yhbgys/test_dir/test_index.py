import sys
import pytest
from selenium import webdriver
from time import sleep

sys.path.append("..")
from page.login_page import LoginPage
from page.index_page import IndexPage
from basic_setting import BasicSetting


class TestChangeHospital:
    url = BasicSetting.url
    sleep_time = BasicSetting.sleep_time

    # ==========Fixture==========
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.Login_Page = LoginPage(self.driver)
        self.Index_Page = IndexPage(self.driver)
        self.driver.maximize_window()
        self.Login_Page.get(self.url + r"login")
        self.Login_Page.user_input = "test"
        self.Login_Page.password_input = "123456zxA"
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        self.Login_Page.select_hospital.click()
        self.Login_Page.select_ensure.click()
        sleep(self.sleep_time)
        pass

    def teardown_class(self):
        self.driver.close()
        pass

    def setup(self):
        if self.Index_Page.body.get_attribute("class") == "el-popup-parent--hidden":
            self.Index_Page.close_hospital.click()
            sleep(self.sleep_time)
            pass
        else:
            self.Index_Page.index_button.click()
            sleep(self.sleep_time)
            pass
        pass

    def teardown(self):
        # self.Index_Page.index_button.click()
        pass

    # 医耗宝供应商选择医院窗口测试用例
    def test_change_hospital(self):
        self.Index_Page.change_hospital_button.click()
        sleep(self.sleep_time)
        assert self.Index_Page.body.get_attribute("class") == "el-popup-parent--hidden"
        pass

    # 医耗宝供应商点击资质提醒测试用例
    def test_click_zztx(self):
        self.Index_Page.zi_zhi_ti_xing_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"index/remind/aptitudeTip"
        pass

    # 医耗宝供应商点击近效提醒测试用例
    def test_click_jxtx(self):
        self.Index_Page.jin_xiao_ti_xing_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"index/remind/effectTip"
        pass

    # 医耗宝供应商点击库存预警测试用例
    def test_click_kcyj(self):
        self.Index_Page.ku_cun_yu_jing_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/currentStocks"
        pass

    # 医耗宝供应商点击未处理测试用例
    def test_click_wcl(self):
        self.Index_Page.wei_chu_li_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/untreated/untreatedAll"
        pass

    # 医耗宝供应商点击未完结测试用例
    def test_click_wwj(self):
        self.Index_Page.wei_wan_jie_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/untreated/untreatedDesear"
        pass

    # 医耗宝供应商点击退货单测试用例
    def test_click_thd(self):
        self.Index_Page.tui_huo_dan_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"approval/returnGoodsApproved/returnGoodsApproved"
        pass

    # 医耗宝供应商点击耗材订货排行测试用例
    def test_click_order_button(self):
        self.Index_Page.order_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"index/ranking/consumablesOrderingRanking"
        pass

    # 医耗宝供应商点击耗材订货排行季榜测试用例
    def test_click_order_quarter_button(self):
        self.Index_Page.order_quarter_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.order_quarter_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击耗材订货排行月榜测试用例
    def test_click_order_month_button(self):
        self.Index_Page.order_month_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.order_month_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击耗材订货排行报表测试用例
    def test_click_order_report_button(self):
        self.Index_Page.order_report_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/dataReport/orderRate"
        pass

    # 医耗宝供应商点击耗材退货排行测试用例
    def test_click_return_button(self):
        self.Index_Page.return_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"index/ranking/consumablesReturnRanking"
        pass

    # 医耗宝供应商点击耗材退货排行季榜测试用例
    def test_click_return_quarter_button(self):
        self.Index_Page.return_quarter_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.return_quarter_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击耗材退货排行月榜测试用例
    def test_click_return_month_button(self):
        self.Index_Page.return_month_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.return_month_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击耗材退货排行报表测试用例
    def test_click_return_report_button(self):
        self.Index_Page.return_report_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"consumable/dataReport/returnRate"
        pass

    # 医耗宝供应商点击销量排行测试用例
    def test_click_market_button(self):
        self.Index_Page.market_button.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"index/ranking/salesRanking"
        pass

    # 医耗宝供应商点击销量排行年榜测试用例
    def test_click_market_year_button(self):
        self.Index_Page.market_year_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.market_year_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击销量排行月榜测试用例
    def test_click_market_month_button(self):
        self.Index_Page.market_month_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.market_month_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击销量排行季榜测试用例
    def test_click_market_quarter_button(self):
        self.Index_Page.market_quarter_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.market_quarter_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击全部订单-全部测试用例
    def test_click_all_order_button(self):
        self.Index_Page.all_order_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.all_order_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点全部订单-未处理测试用例
    def test_click_wcl_order_button(self):
        self.Index_Page.wcl_order_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.wcl_order_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击全部订单-未完结测试用例
    def test_click_wwj_order_button(self):
        self.Index_Page.wwj_order_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.wwj_order_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击全部订单-已完成测试用例
    def test_click_ywc_order_button(self):
        self.Index_Page.ywc_order_button.click()
        sleep(self.sleep_time)
        assert str(self.Index_Page.ywc_order_button.get_attribute("class")).find("active") != -1
        pass

    # 医耗宝供应商点击订单-未完成测试用例
    def test_click_order_untreated(self):
        self.Index_Page.order_untreated.click()
        sleep(self.sleep_time)
        assert self.driver.current_url == self.url + r"order/untreated/untreatedToday"
        pass
    pass


if __name__ == '__main__':
    pytest.main(["test_index.py::TestChangeHospital::test_click_order_untreated"])
    pass
