import pytest
import sys
sys.path.append("test_dir")

if __name__ == '__main__':
    choose = input("请输入测试项目：0.测试全部。1.测试登录。2.测试主页。3.测试订单。4.测试耗材。5.测试配送。6.测试退货。7.测试结算。")
    if choose == "0":
        pytest.main()
    elif choose == "1":
        pytest.main(["test_dir/test_login.py"])
    elif choose == "2":
        pytest.main(["test_dir/test_index.py"])
    elif choose == "3":
        pytest.main(["test_dir/test_order.py"])
    elif choose == "4":
        pytest.main(["test_dir/test_consumable.py"])
    elif choose == "5":
        pytest.main(["test_dir/test_agent.py"])
    elif choose == "6":
        pytest.main(["test_dir/test_return.py"])
    elif choose == "7":
        pytest.main(["test_dir/test_close.py"])
    else:
        print("输入错误")
    pass
