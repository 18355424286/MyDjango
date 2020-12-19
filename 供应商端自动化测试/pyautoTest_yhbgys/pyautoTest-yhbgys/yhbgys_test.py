import pytest
import sys
import time
sys.path.append("test_dir")


if __name__ == '__main__':
    test_file_list = ["test_dir/test_login.py",
                      "test_dir/test_index.py",
                      "test_dir/test_order.py",
                      "test_dir/test_consumable.py",
                      "test_dir/test_agent.py",
                      "test_dir/test_return.py",
                      "test_dir/test_close.py",
                      "test_dir/test_setting.py"]
    choose = input("请输入测试项目：0.测试全部。1.测试登录。2.测试主页。3.测试订单。4.测试耗材。5.测试配送。6.测试退货。7.测试结算。8.测试设置。")
    try:
        choose = int(choose)-1
        if choose == -1:
            # print(choose)
            pytest.main(test_file_list)
            pass
        else:
            print(test_file_list[choose])
            pytest.main([test_file_list[choose]])
            pass
        pass
    except Exception as e:
        print(e)
        print("输入错误")
        pass
    pass
