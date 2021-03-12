from poium import Page, Element


class IndexPage(Page):
    body = Element(css="body")
    index_button = Element(css="ul.el-menu > li:nth-child(1) > a")
    user_name = Element(css="div.supName > span")
    hospital_name = Element(css="div.nuhName")
    change_hospital_button = Element(css="div.nuhName > span")
    close_hospital = Element(xpath=r"/html/body/div[2]/div/div[1]/button")
    zi_zhi_ti_xing_button = Element(css="div.head-right > a:nth-child(1)")
    jin_xiao_ti_xing_button = Element(css="div.head-right > a:nth-child(2)")
    ku_cun_yu_jing_button = Element(css="div.head-right > a:nth-child(3)")
    wei_chu_li_button = Element(css="div.head-right > a:nth-child(4)")
    wei_wan_jie_button = Element(css="div.head-right > a:nth-child(5)")
    tui_huo_dan_button = Element(css="div.head-right > a:nth-child(6)")
    order_button = Element(css=
                           "div.main-content > div:nth-child(1) > div:nth-child(3) > div > div > "
                           "div.card-header > span.card-header-title > button")
    order_quarter_button = Element(css=
                                   "div.main-content > div:nth-child(1) > div:nth-child(3) > div > div > "
                                   "div.card-header > div.card-header-type > span:nth-child(1)")
    order_month_button = Element(css=
                                 "div.main-content > div:nth-child(1) > div:nth-child(3) > div > div > "
                                 "div.card-header > div.card-header-type > span:nth-child(2)")
    order_report_button = Element(css=
                                  "div.main-content > div:nth-child(1) > div:nth-child(3) > div > div > "
                                  "div.card-table > div:nth-child(2) > svg")
    return_button = Element(css=
                            "div.main-content > div:nth-child(1) > div:nth-child(4) > div > "
                            "div.card-header > span.card-header-title > button")
    return_quarter_button = Element(css=
                                    "div.main-content > div:nth-child(1) > div:nth-child(4) > div > "
                                    "div.card-header > div.card-header-type > span:nth-child(1)")
    return_month_button = Element(css=
                                  "div.main-content > div:nth-child(1) > div:nth-child(4) > div > "
                                  "div.card-header > div.card-header-type > span:nth-child(2)")
    return_report_button = Element(css=
                                   "div.main-content > div:nth-child(1) > div:nth-child(4) > div > "
                                   "div:nth-child(2) > div.card-table > div:nth-child(2) > svg")
    market_button = Element(css="div.ranking-row > div.card-header > span.card-header-title > button")
    market_year_button = Element(css="div.ranking-row > div.card-header > div.card-header-type > "
                                     "span:nth-child(1)")
    market_month_button = Element(css="div.ranking-row > div.card-header > div.card-header-type > "
                                      "span:nth-child(2)")
    market_quarter_button = Element(css="div.ranking-row > div.card-header > div.card-header-type > "
                                        "span:nth-child(3)")
    all_order_button = Element(css="div.order > div.card-header > div.card-header-type > "
                                   "span:nth-child(1)")
    wcl_order_button = Element(css="div.order > div.card-header > div.card-header-type > "
                                   "span:nth-child(2)")
    wwj_order_button = Element(css="div.order > div.card-header > div.card-header-type > "
                                   "span:nth-child(3)")
    ywc_order_button = Element(css="div.order > div.card-header > div.card-header-type > "
                                   "span:nth-child(4)")
    order_untreated = Element(css="div.order > div:nth-child(3) > svg")
    pass
