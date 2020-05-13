from django.db.models import QuerySet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.


from main.models import Item, User
from remarksys.models import RemarkI, RemarkR
from ysh.settings import OK_msg, error_msg


def hello(request):
    return HttpResponse("hi")


def remark(request):
    """
    remark
    get请求评论
        pk 帖子主键,type 1为一级评论 2为二级评论
    post 添加评论
    """
    if request.method == "GET":
        type = int(request.GET.get("type", None))
        pk = request.GET.get("pk", None)
        try:
            assert pk and type
            print(pk,type)
            objs = None
            if type == 1:
                objs = Item.objects.get(pk=pk).remarki_set.all().values()
            elif type == 2:
                objs = RemarkI.objects.get(pk=pk).RemarkR.all().values()
                print(objs)
            objs = {"remarks": list(objs)}
            # objs = {"remarks":"indiof"}
            return JsonResponse(objs)
            # return JsonResponse({})
        except Exception as e:
            # raise (e)
            print(e)
    elif request.method == "POST":
        # todo 评论数目自动增加减轻查询压力
        type = int(request.POST.get("type", None))
        po = request.POST.get("po", None)
        content = request.POST.get("cnt", "")
        # remark_to =request.POST.get("rt",None)
        po = User.objects.get(pk=po)
        try:
            assert type and po
            print("HHHHH")
            objs = None
            if type == 1:
                i_pk=int(request.POST.get("i_pk",None))
                item=Item.objects.get(pk=i_pk)
                item.i_remark_num+=1
                objs = RemarkI(R_Po=po,R_content=content,R_item=item)
            elif type == 2:
                i_pk=request.POST.get("i_pk",None)
                r_pk=request.POST.get("r_pk",None)
                ry_pk=request.POST.get("ry_pk",None)
                item=Item.objects.get(pk=i_pk)
                remark=RemarkI.objects.get(pk=r_pk)
                replay=None
                if ry_pk:
                    replay=RemarkR.objects.get(pk=ry_pk)
                    replay.R_remark_num+=1
                else:
                    remark.R_remark_num+=1
                objs = RemarkR(R_Po=po,R_content=content,R_item=item,R_replay=replay,R_remark=remark)
            objs.save()
            return JsonResponse(OK_msg)
        except Exception as e:
            # raise (e)
            print(e)
    return JsonResponse(error_msg)
