from poium import Page, Element


class LoginPage(Page):
    a = "1111111111"
    company_name = Element(css=
                           "div#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > p:nth-child(1)")
    body = Element(css="body")
    user_input = Element(css="form > div:nth-child(1) > div > div > input")
    password_input = Element(css="form > div:nth-child(2) > div > div > input")
    login_button = Element(css="form > button")
    forget_password_button = Element(css="form > div:nth-child(4) > span:nth-child(1)")
    register_button = Element(css="form > div:nth-child(4) > span:nth-child(1)")
    select_hospital = Element(
        css="div.el-scrollbar__view > ul > li:nth-child(1) > div > div:nth-child(2) > div:nth-child(2) > button")
    select_ensure = Element(css="div.el-dialog__body > div > div:nth-child(3) > button")
    pass
