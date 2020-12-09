from poium import Page, NewPageElement


class LoginPage(Page):
    a = "1111111111"
    company_name = NewPageElement(css=
                                  "div#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > p:nth-child(1)")
    body = NewPageElement(css="body")
    user_input = NewPageElement(css="form > div:nth-child(1) > div > div > input")
    password_input = NewPageElement(css="form > div:nth-child(2) > div > div > input")
    login_button = NewPageElement(css="form > button")
    forget_password_button = NewPageElement(css="form > div:nth-child(4) > span:nth-child(1)")
    register_button = NewPageElement(css="form > div:nth-child(4) > span:nth-child(1)")
    select_hospital = NewPageElement(
        css="div.el-scrollbar__view > ul > li:nth-child(1) > div > div:nth-child(2) > div:nth-child(2) > button")
    select_ensure = NewPageElement(css="div.el-dialog__body > div > div:nth-child(3) > button")
    pass
