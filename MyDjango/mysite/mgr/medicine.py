from django.http import JsonResponse
from common.models import Medicine
import json


def list_medicines(request):
    qs = Medicine.objects.values()
    ret_list = list(qs)
    return JsonResponse({"ret": 0, 'retList': ret_list})


def add_medicine(request):
    info = request.params['data']
    medicine = Medicine.objects.create(name=info['name'],
                                       sn=info['sn'],
                                       desc=info['desc'])
    # print(info)
    # print('======================')

    return JsonResponse({"ret": 0, "id": medicine.id})
    pass


def modify_medicine(request):
    modify_id = request.params['id']
    new_data = request.params['data']

    try:
        medicine = Medicine.objects.get(id=modify_id)
    except Medicine.DoesNotExist:
        return JsonResponse({
            "ret": -1,
            "msg": f'id为{modify_id}的用户不存在。'
        })
        pass

    if 'name' in new_data:
        medicine.name = new_data['name']
    if 'sn' in new_data:
        medicine.phone_number = new_data['sn']
    if 'desc' in new_data:
        medicine.address = new_data['desc']

    medicine.save()
    return JsonResponse({"ret": 0})


def delete_medicine(request):
    delete_id = request.params['id']

    try:
        medicine = Medicine.objects.get(id=delete_id)
    except Medicine.DoesNotExist:
        return JsonResponse({
            'ret': -1,
            'msg': f'id为{delete_id}的用户不存在。'
        })

    medicine.delete()
    return JsonResponse({'ret': 0})
    pass


def dispatcher(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            "ret": 302,
            "msg": "未登录",
            "redirect": "/admin/"
        }, status=302)

    if request.session['usertype'] != 'mgr':
        return JsonResponse({
            "ret": 302,
            "msg": "用户非mge类型",
            "redirect": "/admin/"
        }, status=302)

    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET.get('action', {'action': 'list_medicine'})

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_medicine':
        return list_medicines(request)
    elif action == 'add_medicine':
        return add_medicine(request)
    elif action == 'modify_medicine':
        return modify_medicine(request)
    elif action == 'del_medicine':
        return delete_medicine(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
