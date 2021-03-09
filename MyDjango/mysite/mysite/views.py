from django.http import HttpResponse


def page1_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def page0_view(request):
    html = "<h1>这是第0个页面</h1>"
    return HttpResponse(html)


def page_view(request, n):
    html = "<h1>这是第%s个页面</h1>" % n
    return HttpResponse(html)
