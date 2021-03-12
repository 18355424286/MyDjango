from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render


def page1_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def page0_view(request):
    html = "<h1>这是第0个页面</h1>"
    return HttpResponse(html)


def page_view(request, n):
    html = "<h1>这是第%s个页面</h1>" % n
    return HttpResponse(html)


def return_a(request):
    if request.method == "GET":
        a = request.GET.get("a", "没有参数a")
        return HttpResponse("<h1>a = {0}</h1>".format(a))
    else:
        return HttpResponse("请使用GET")


def login_view(request):
    if request.method == 'GET':
        # 返回模板生成的html给浏览器
        # t = loader.get_template('mylogin.html')
        # html = t.render()
        return render(request, 'mylogin.html', {'name': '', 'password': ''})
    elif request.method == 'POST':
        name = request.POST.get('username', '属性错误')
        return HttpResponse("<h1>{}</h1>".format(name))
    pass


def mytemp_view(request):
    x = -5
    # locals返回当前作用域内全部的局部变量
    return render(request, 'mytemp.html', locals())
    pass


def my_cal_view(request):
    if request.method == 'GET':
        return render(request, 'MyCal.html')
    elif request.method == 'POST':
        x = int(request.POST.get('x', '0'))
        y = int(request.POST.get('y', '0'))
        op = request.POST.get('op')
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        else:
            result = 0.0
        return render(request, 'MyCal.html', locals())


def for_view(request):
    if request.method == "GET":
        lst = ['北京', '上海', '天津']
        s = 'Hello!'
        n = 100
        return render(request, 'for.html', locals())


def index_view(request):
    return render(request, 'base.html')


def sport_view(request):
    return render(request, 'sport.html')
