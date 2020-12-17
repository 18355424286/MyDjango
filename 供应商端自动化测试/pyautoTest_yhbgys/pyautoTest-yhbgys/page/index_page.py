from poium import Page, NewPageElement


class IndexPage(Page):
    body = NewPageElement(css="body")
    index_button = NewPageElement(css="ul.el-menu > li:nth-child(1) > a")
    user_name = NewPageElement(css="div.supName > span")
    hospital_name = NewPageElement(css="div.nuhName")
    change_hospital_button = NewPageElement(css="div.nuhName > span")
    close_hospital = NewPageElement(xpath=r"/html/body/div[2]/div/div[1]/button")
    zi_zhi_ti_xing_button = NewPageElement(css="div.head-right > a:nth-child(1)")
    jin_xiao_ti_xing_button = NewPageElement(css="div.head-right > a:nth-child(2)")
    ku_cun_yu_jing_button = NewPageElement(css="div.head-right > a:nth-child(3)")
    wei_chu_li_button = NewPageElement(css="div.head-right > a:nth-child(4)")
    wei_wan_jie_button = NewPageElement(css="div.head-right > a:nth-child(5)")
    tui_huo_dan_button = NewPageElement(css="div.head-right > a:nth-child(6)")
    order_button = NewPageElement(css=
                                  "div.main-content > div:nth-child(1) > div:nth-child(3) > div > div > "
                                  "div.card-header > span.card-header-title > button")
    order_quarter_button = NewPageElement(css=
                                          "div.main-content > div:nth-child(1) > div:nth-child(3) > div > div > "
                                          "div.card-header > div.card-header-type > span:nth-child(1)")
    order_month_button = NewPageElement(css=
                                        "div.main-content > div:nth-child(1) > div:nth-child(3) > div > div > "
                                        "div.card-header > div.card-header-type > span:nth-child(2)")
    order_report_button = NewPageElement(css=
                                         "div.main-content > div:nth-child(1) > div:nth-child(3) > div > div > "
                                         "div.card-table > div:nth-child(2) > svg")
    return_button = NewPageElement(css=
                                   "div.main-content > div:nth-child(1) > div:nth-child(4) > div > "
                                   "div.card-header > span.card-header-title > button")
    return_quarter_button = NewPageElement(css=
                                           "div.main-content > div:nth-child(1) > div:nth-child(4) > div > "
                                           "div.card-header > div.card-header-type > span:nth-child(1)")
    return_month_button = NewPageElement(css=
                                         "div.main-content > div:nth-child(1) > div:nth-child(4) > div > "
                                         "div.card-header > div.card-header-type > span:nth-child(2)")
    return_report_button = NewPageElement(css=
                                          "div.main-content > div:nth-child(1) > div:nth-child(4) > div > "
                                          "div:nth-child(2) > div.card-table > div:nth-child(2) > svg")
    market_button = NewPageElement(css="div.ranking-row > div.card-header > span.card-header-title > button")
    market_year_button = NewPageElement(css="div.ranking-row > div.card-header > div.card-header-type > "
                                            "span:nth-child(1)")
    market_month_button = NewPageElement(css="div.ranking-row > div.card-header > div.card-header-type > "
                                             "span:nth-child(2)")
    market_quarter_button = NewPageElement(css="div.ranking-row > div.card-header > div.card-header-type > "
                                               "span:nth-child(3)")
    all_order_button = NewPageElement(css="div.order > div.card-header > div.card-header-type > "
                                          "span:nth-child(1)")
    wcl_order_button = NewPageElement(css="div.order > div.card-header > div.card-header-type > "
                                          "span:nth-child(2)")
    wwj_order_button = NewPageElement(css="div.order > div.card-header > div.card-header-type > "
                                          "span:nth-child(3)")
    ywc_order_button = NewPageElement(css="div.order > div.card-header > div.card-header-type > "
                                          "span:nth-child(4)")
    order_untreated = NewPageElement(css="div.order > div:nth-child(3) > svg")
    pass
