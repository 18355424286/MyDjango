import sys
import pytest
from selenium import webdriver
from time import sleep

sys.path.append("..")
from page.login_page import LoginPage
# from page.index_page import IndexPage
from page.agent_page import AgentPage


class TestAgent:
    url = r"http://183.60.104.92:8000/#/"

    # ==========Fixture==========
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.Login_Page = LoginPage(self.driver)
        self.Agent_Page = AgentPage(self.driver)
        self.driver.maximize_window()
        self.Login_Page.get(self.url + r"login")
        self.Login_Page.user_input = "test"
        self.Login_Page.password_input = "123456zxA"
        self.Login_Page.login_button.click()
        sleep(2)
        self.Login_Page.select_hospital.click()
        self.Login_Page.select_ensure.click()
        sleep(2)
        self.Agent_Page.agent_button.click()
        sleep(2)
        pass

    def teardown_class(self):
        self.driver.close()
        pass

    # 医耗宝供应商进入配送界面测试用例
    def test_to_agent(self):
        assert self.driver.current_url == self.url + r"distribution/maintain/agent"
        pass

    # 医耗宝供应商进入配送公司界面测试用例
    def test_to_agent_company(self):
        self.Agent_Page.agent_company.click()
        sleep(2)
        assert self.driver.current_url == self.url + r"distribution/maintain/agent"
        pass

    # 医耗宝供应商进入审核记录界面测试用例
    def test_to_agent_record(self):
        self.Agent_Page.agent_record.click()
        sleep(2)
        assert self.driver.current_url == self.url + r"distribution/maintain/agentRecord"
        pass
    pass


if __name__ == '__main__':
    pytest.main(["test_agent.py::TestAgent"])
