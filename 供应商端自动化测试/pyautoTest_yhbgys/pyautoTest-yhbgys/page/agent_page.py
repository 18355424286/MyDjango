from poium import Page, NewPageElement


class AgentPage(Page):
    agent_button = NewPageElement(css="ul.el-menu > li:nth-child(4) > a")
    agent_company = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(1)")
    agent_record = NewPageElement(css="div.verticalRouterView-nav-list > nav > ul > li:nth-child(2)")
    pass

