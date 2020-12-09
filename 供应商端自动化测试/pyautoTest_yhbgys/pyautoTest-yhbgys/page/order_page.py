from poium import Page, NewPageElement


class OrderPage(Page):
    order_button = NewPageElement(css="ul.el-menu > li:nth-child(2) > a")
    unfinished_button = NewPageElement(css="ul.flex > li:nth-child(1) > a")
    finished_button = NewPageElement(css="ul.flex > li:nth-child(2) > a")
    paid_button = NewPageElement(css="ul.flex > li:nth-child(3) > a")
    all_order_button = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(1) > a")
    untreated_order_button = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(2) > a")
    unfinished_order_button = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(3) > a")
    pass
