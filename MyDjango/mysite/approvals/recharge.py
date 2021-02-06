from django.http import JsonResponse
from common.models import Recharge
import json


def list_recharge(request):
    # user_id = request.params["id"]
    all_recharge = Recharge.objects.values()
    ret_list = list(all_recharge)
    return JsonResponse({"code": 0, "data": ret_list})
    pass


def add_recharge(request):
    info = request.params['data']
    record = Recharge.objects.create(recharge_id=info['recharge_id'],
                                     supplier=info['supplier'],
                                     recharge_user=info['recharge_user'],
                                     recharge_time=info['recharge_time'],
                                     recharge_way=info['recharge_way'],
                                     recharge_money=info['recharge_money'])
    # print(info)
    # print('======================')

    return JsonResponse({"ret": 0, "id": record.id})
    pass


def recharge_dispatcher(request):
    if request.method not in ['POST']:
        return JsonResponse({
            "code": -1,
            "msg": "不支持该类型http请求"
        })
        pass
    else:
        request.params = json.loads(request.body)
        action = request.params['action']
        if action == "add":
            return add_recharge(request)
            pass
        else:
            request.params = json.loads(request.body)
            return list_recharge(request)
    pass
