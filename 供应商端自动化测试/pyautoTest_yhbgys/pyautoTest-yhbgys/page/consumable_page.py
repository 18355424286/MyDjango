from poium import Page, NewPageElement


class ConsumablePage(Page):
    consumable_button = NewPageElement(css="ul.el-menu > li:nth-child(3) > a")
    current_inventory = NewPageElement(css="ul.flex > li:nth-child(1) > a")
    data_report = NewPageElement(css="ul.flex > li:nth-child(2) > a")
    material_management = NewPageElement(css="ul.flex > li:nth-child(3) > a")
    data_report_inventory = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(1) > a")
    data_report_usage = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(2) > a")
    data_report_order = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(3) > a")
    data_report_return = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(4) > a")
    data_report_recent = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(5) > a")
    material_management_all = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(1) > a")
    material_management_sale = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(2) > a")
    material_management_halt_sale = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(3) "
                                                       "> a")
    material_management_review = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(4) > a")
    material_management_approved = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(5) > a")
    material_management_unapproved = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(6) "
                                                        "> a")
    pass
