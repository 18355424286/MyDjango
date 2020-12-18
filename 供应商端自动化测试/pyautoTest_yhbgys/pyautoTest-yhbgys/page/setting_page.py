from poium import Page, NewPageElement


class SettingPage(Page):
    setting_button = NewPageElement(css="ul.el-menu > li:nth-child(7) > a")
    set_basic = NewPageElement(css="ul.flex > li:nth-child(1) > a")
    set_vip = NewPageElement(css="ul.flex > li:nth-child(2) > a")
    consumption_records = NewPageElement(css="ul.flex > li:nth-child(3) > a")
    set_basic_company = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(1) > a")
    set_basic_account = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(2) > a")
    pass
