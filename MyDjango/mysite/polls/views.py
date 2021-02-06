from django.shortcuts import HttpResponse
from common.models import Customer

# Create your views here.


def index(request):
    return HttpResponse("Hello,world.You`re at the pools index.")


def list_customers(request):
    qs = Customer.objects.values()

    # 检查url是否有参数id
    phone_number = request.GET.get('phone_number', None)
    if phone_number:
        qs = qs.filter(phone_number=phone_number)

    retStr = ''
    for customer in qs:
        retStr += '<div style=color:green>'
        for name, value in customer.items():
            retStr += f'{name} : {value} |'
            pass
        retStr += '<div>'
        retStr += '<br>'
        pass
    return HttpResponse(retStr)
    pass
