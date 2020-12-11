from poium import Page, NewPageElement


class ReturnPage(Page):
    return_button = NewPageElement(css="ul.el-menu > li:nth-child(5) > a")
    return_manage = NewPageElement(css="ul.flex > li:nth-child(1) > a")
    return_record = NewPageElement(css="ul.flex > li:nth-child(2) > a")
    return_manage_approved = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(1) > a")
    return_manage_record = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(2) > a")
    pass
