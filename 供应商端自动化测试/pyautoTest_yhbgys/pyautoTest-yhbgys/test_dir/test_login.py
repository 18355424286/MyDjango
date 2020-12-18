import sys
import pytest
from os.path import dirname, abspath
from time import sleep
from selenium import webdriver

sys.path.append("..")
from page.login_page import LoginPage
from page.index_page import IndexPage
from basic_setting import BasicSetting


class TestLogin:
    url = BasicSetting.url
    sleep_time = BasicSetting.sleep_time

    # ==========Fixture==========
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.Login_Page = LoginPage(driver=self.driver)
        self.Login_Page.get(self.url + r"login")
        pass

    def teardown(self):
        self.driver.close()
        pass

    # 医耗宝供应商登录模块测试用例
    def test_login_open(self):
        """
        打开登录界面
        :return:null
        """
        sleep(self.sleep_time)
        # print("--------------------" + self.Login_Page.company_name.text)
        assert self.Login_Page.company_name.text == "福建星联科技有限公司"
        pass

    def test_login_all_null(self):
        """
        未输入账号密码时进行登录
        :return:
        """
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        assert self.Login_Page.body.get_attribute("class") == ""
        pass

    @pytest.mark.parametrize(
        "user",
        [("test", ),
         ("qewl", )],
        ids=["case1", "case2"]
    )
    def test_login_password_null(self, user):
        """
        未输入密码时进行登录
        :param user: 用户名
        :return:
        """
        self.Login_Page.user_input = user
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        assert self.Login_Page.body.get_attribute("class") == ""
        pass

    @pytest.mark.parametrize(
        "password",
        [("123456zxA",)],
        ids=["case1"]
    )
    def test_login_user_null(self, password):
        """
        未输入用户名时进行登录
        :param password: 密码
        :return:
        """
        self.Login_Page.password_input = password
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        assert self.Login_Page.body.get_attribute("class") == ""
        pass

    @pytest.mark.parametrize(
        "user, password",
        [("test", "11111111",
          "qewl", "11111111")],
        ids=["case1", "case2"]
    )
    def test_login_password_is_wrong(self, user, password):
        """
        输入错误的密码时进行登录
        :param user: 用户名
        :param password: 密码
        :return:
        """
        self.Login_Page.user_input = user
        self.Login_Page.password_input = password
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        assert self.Login_Page.body.get_attribute("class") == ""
        pass

    @pytest.mark.parametrize(
        "user, password",
        [("test", "123456zxA"),
         ("qewl", "123456zxA")],
        ids=["case1", "case2"]
    )
    def test_login_password_is_wrong(self, user, password):
        """
        输入正确的用户名密码时进行登录
        :param user: 用户名
        :param password: 密码
        :return:
        """
        self.Login_Page.user_input = user
        self.Login_Page.password_input = password
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        assert self.Login_Page.body.get_attribute("class") == "el-popup-parent--hidden"
        pass


class TestSelectHospital:
    url = r"http://183.60.104.92:8000/#/"
    sleep_time = 5

    # ==========Fixture==========
    def setup(self):
        self.driver = webdriver.Chrome()
        self.Login_Page = LoginPage(driver=self.driver)
        self.Index_Page = IndexPage(driver=self.driver)
        self.driver.maximize_window()
        self.Login_Page.get(self.url + "login")
        pass

    def teardown(self):
        self.driver.close()
        pass

    # 医耗宝供应商选择医院测试用例
    @pytest.mark.parametrize(
        "username, user, password",
        [("test测试公司", "test", "123456zxA"),
         ("企鹅物流", "qewl", "123456zxA")],
        ids=["case1", "case2"]
    )
    def test_select_hospital(self, username, user, password):
        self.Login_Page.user_input = user
        self.Login_Page.password_input = password
        self.Login_Page.login_button.click()
        sleep(self.sleep_time)
        self.Login_Page.select_hospital.click()
        self.Login_Page.select_ensure.click()
        sleep(self.sleep_time)
        assert (self.Index_Page.user_name.text, self.Index_Page.hospital_name.text) == (username, "附一医院 （切换医院）")
        pass


if __name__ == '__main__':
    pytest.main(["test_login.py::TestLogin", "test_login.py::TestSelectHospital"])
    pass
