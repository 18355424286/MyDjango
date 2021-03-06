from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout


# 登录处理
def log_in(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    user = authenticate(username=userName, password=passWord)
    print('-------------')
    print(userName)
    print(passWord)
    print('-------------')
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                request.session['usertype'] = 'mgr'
                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': -1, 'msg': "请使用管理员账户登录"})
        else:
            return JsonResponse({'ret': -1, 'msg': '用户被禁用'})

    else:
        return JsonResponse({'ret': -1, 'msg': '用户名或密码错误'})
    pass


def log_out(request):
    logout(request)
    return JsonResponse({'ret': 0})
    pass


def test(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    return JsonResponse({'ret': 0, 'msg': 'test', 'user': userName, 'pwd': passWord,
                         'data': [
                             {'id': 1, 'name': 'a'},
                             {'id': 2, 'name': 'b'},
                             {'id': 3, 'name': 'c'},
                             {'id': 4, 'name': 'd'},
                             {'id': 5, 'name': 'e'}
                         ]})



