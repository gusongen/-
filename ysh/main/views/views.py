#用户注册登入
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# from main.formset import MultiImageForm
from main.models import Item, Image, User
from ysh.settings import error_msg, OK_msg


def hello(request):
    print(request.POST.get('test'))
    print(request.POST['test'])
    return JsonResponse({'mag': 'hello'})


def login(request):
    if request.method == 'GET':
        return render(request, 'dengru.html')
    if request.method == "POST":  # 微信登入,绑定学号
        name = request.POST.get("name", None)
        pwd = request.POST.get("pwd", None)
        # print(name,pwd)
        if name and pwd:
            u = User.objects.filter(u_name=name).first()
            if u and u.u_pwd == pwd:
                return JsonResponse(OK_msg)# 返回token
    return JsonResponse(error_msg)


def register(request):
    if request.method == 'GET':
        return render(request, 'zhuce.html')
    if request.method == "POST":  # 微信登入,绑定学号
        name = request.POST.get("name", None)
        pwd = request.POST.get("pwd", None)
        #todo 用户名 密码合法检测 长度或存在
        if name and pwd and not User.objects.filter(u_name=name).exists():
            User(u_name=name, u_pwd=pwd,).save()
            return JsonResponse(OK_msg)
    return JsonResponse(error_msg)


def UserUpdate():
    #修改头像和昵称
    
    pass


def main(request):
    if request.method == 'GET':
        return render(request, 'zhuye.html')


def classify(request):
    if request.method == 'GET':
        return render(request, 'fenlei.html')

#
# def message(request):
#     if request.method == 'GET':
#         return render(request, "test.html")
#     MultiImageForm = modelformset_factory(Image, fields=('file', 'item'))
#     if request.method == "POST":
#         mes = Item(
#             i_title=request.POST.get("title", None),
#             i_content=request.POST.get("content", None),
#             i_p_id=request.POST.get("pid", None),
#         )
#         mes.save()  # 先储存否则外码设置有问题
#         if request.FILES:
#             image_list = request.FILES.getlist("img")
#             for image in image_list:
#                 img = Image(file=image, item=mes)
#                 img.save()
#         return JsonResponse({"status": 200, "msg": "OK"})
#     return JsonResponse({"status": 400, "msg": "receive nothing"})
