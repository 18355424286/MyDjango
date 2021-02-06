from django.http import JsonResponse
from common.models import Customer
import json


def list_customers(request):
    qs = Customer.objects.values()
    ret_list = list(qs)
    return JsonResponse({"ret": 0, 'retList': ret_list})


def add_customer(request):
    info = request.params['data']
    record = Customer.objects.create(name=info['name'],
                                     phone_number=info['phone_number'],
                                     address=info['address'])
    # print(info)
    # print('======================')

    return JsonResponse({"ret": 0, "id": record.id})
    pass


def modify_customer(request):
    modify_id = request.params['id']
    new_data = request.params['data']

    try:
        customer = Customer.objects.get(id=modify_id)
    except Customer.DoesNotExist:
        return JsonResponse({
            "ret": -1,
            "msg": f'id为{modify_id}的用户不存在。'
        })
        pass

    if 'name' in new_data:
        customer.name = new_data['name']
    if 'phone_number' in new_data:
        customer.phone_number = new_data['phone_number']
    if 'address' in new_data:
        customer.address = new_data['address']

    customer.save()
    return JsonResponse({"ret": 0})


def delete_customer(request):
    delete_id = request.params['id']

    try:
        customer = Customer.objects.get(id=delete_id)
    except Customer.DoesNotExist:
        return JsonResponse({
            'ret': -1,
            'msg': f'id为{delete_id}的用户不存在。'
        })

    customer.delete()
    return JsonResponse({'ret': 0})
    pass


def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET.get('action', {'action': 'list_customer'})

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_customer':
        return list_customers(request)
    elif action == 'add_customer':
        return add_customer(request)
    elif action == 'modify_customer':
        return modify_customer(request)
    elif action == 'del_customer':
        return delete_customer(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
