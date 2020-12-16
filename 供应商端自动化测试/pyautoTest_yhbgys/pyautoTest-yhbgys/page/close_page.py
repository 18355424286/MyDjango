from poium import Page, NewPageElement


class ClosePage(Page):
    close_button = NewPageElement(css="ul.el-menu > li:nth-child(6) > a")
    close_apply = NewPageElement(css="ul.flex > li:nth-child(1) > a")
    close_course = NewPageElement(css="ul.flex > li:nth-child(2) > a")
    close_record = NewPageElement(css="ul.flex > li:nth-child(3) > a")
    close_course_all = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(1) > a")
    close_course_investigated = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(2) > a")
    close_course_examine = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(3) > a")
    close_course_settlement = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(4) > a")
    close_course_return = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(5) > a")
    close_record_all = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(1) > a")
    close_record_completed = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(2) > a")
    close_record_withdraw = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(3) > a")
    pass
