import os

from django.core import serializers
from django.core.paginator import *
from django.http import HttpResponse, JsonResponse
from main.models import Item, Image, UserLikeItem, User
from ysh.settings import MEDIA_ROOT, error_msg, OK_msg


def item(request):
    """
    * get
    itn:item_num每次取得贴子条数
    st:start_pos:开始条数
    cat:catalog :分类
    tag:拼音缩写 JY ZH PC XK XR TC todo 管理员自定义
    # todo :缓存
    #todo 用户id查询
    #todo 用户id
    ps :删除在post的基础上op=DELETE
    *post
    """
    res = ""
    op = request.POST.get("op", None)
    if request.method == "GET":
        item_num = request.GET.get('itn', 10)
        start_pos = request.GET.get("st", None)
        catalog = request.GET.get("tag", "all")  # TODO
        page = request.GET.get("pg", 1)
        # 上拉刷新
        if start_pos is None:
            select_obj = Item.objects.all()
            start_pos = Item.objects.order_by('-pk').first().id
            # 下拉刷新,前端自动返回启刷的id
        else:
            # 只搜索id值小于起始点的
            select_obj = Item.objects.filter(pk__lte=start_pos)
        # 图片请求令启一个api,减轻服务器压力
        select_obj = select_obj.order_by('-pk').values()
        paginator = Paginator(select_obj, item_num)
        try:
            content = paginator.page(page)
        except PageNotAnInteger as e:
            content = paginator.page(1)
            print(e)  # todo 改log
        except EmptyPage as e:  # 是invalid的子类要放在前面 #todo 前端要判断最后一页到了没,到了就不能在页面加载最后一页了
            content = paginator.page(paginator.num_pages)
            print(e)
        except InvalidPage as e:
            content = paginator.page(1)
            print(e)  # todo 改log

        # for per_item in content:
        #     if()
        # content=serializers.serialize("json", content, ensure_ascii=False)

        content = list(content)
        data = {'mag': 'ok', 'status': 200, 'per_page': int(paginator.per_page), 'num_page': int(paginator.num_pages),
                'start_pos': start_pos,
                "page_now": page,
                'content': content}
        return JsonResponse(data)
    # end if
    ###########
    # 发帖
    elif request.method == "POST" and op is None:
        i_title = request.POST.get('ttl', False)
        i_content = request.POST.get('cnt', False)  # 内容
        i_tag = request.POST.get('tag', False)  # 标签
        i_p_id = request.POST.get('p_id', False)  # 发帖人id  #todo 身份验证
        i_id = request.POST.get('i_id', False)

        if i_title and i_tag and i_content and i_p_id:
            dict_to_add = {'i_title': i_title, 'i_content': i_content, 'i_tag': i_tag, 'i_p_id': i_p_id}
            try:
                if not i_id:
                    it = Item(**dict_to_add)
                    it.save()
                    msg = 'add_success'
                else:
                    it = Item.objects.filter(pk=i_id)
                    it.update(**dict_to_add)  # 创建并写入数据库
                    msg = 'update_success'
                    # 先储存否则外码设置有问题
                    # todo 图片修改?
                if request.FILES:
                    image_list = request.FILES.getlist("img")
                    for image in image_list:
                        img = Image(file=image, item=it)
                        img.save()
                return JsonResponse({"msg": msg, 'status': 200})
            except Exception as e:
                res = str(e)
        else:
            res = "missing argument"
    elif request.method == "POST" and op == "DELETE":
        i_p_id = request.POST.get('p_id', False)  # 发帖人id  #todo 身份验证
        i_id = request.POST.get('i_id', False)  # todo 无法访问
        if not Item.objects.filter(pk=i_id).exists():
            res = "not found"
        else:
            the_item = Item.objects.filter(pk=i_id).first()
            print(the_item)
            print(i_p_id)
            print(i_id)
            print(the_item.i_p_id)

            if not i_p_id or the_item.i_p_id != i_p_id:
                res = "no access to delete"
            else:
                the_item.delete()
                return JsonResponse({"msg": 'delete_success', 'status': 200})

    return JsonResponse({"msg": 'illegal operation::' + res,
                         "status": 400})


def image_requester(request):
    if request.method == "GET":
        i_id = request.GET.get('id', None)
        try:
            all_pictue = Item.objects.get(pk=i_id).image_set.all().values_list("file")
            pic_list = []
            for i in all_pictue:
                url = os.path.join("/static/upload", i[0])
                pic_list.append(url)
            return JsonResponse({"img": pic_list, "msg": 'OK', 'status': 200})
        except:
            pass
    return JsonResponse({"msg": 'error', 'status': 400})


def like_item(request):
    i_pk = request.POST.get("i_pk", None)
    u_pk = request.POST.get("u_pk", None)
    op = request.POST.get("op", None)  # 默认点赞
    if i_pk and u_pk:
        if op is None:
            if not UserLikeItem.objects.filter(i_pk=i_pk, u_pk=u_pk).exists():  # 每个人每条帖子只能点赞一次
                try:
                    item = Item.objects.get(pk=i_pk)
                    user = User.objects.get(pk=u_pk)
                    UserLikeItem(i_pk=item, u_pk=user).save()
                    return JsonResponse(OK_msg)
                except:
                    pass
        elif op == "DELETE":
            print("hhhh")
            try:
                UserLikeItem.objects.get(i_pk=i_pk, u_pk=u_pk).delete()
                return JsonResponse(OK_msg)
            except:
                pass
    return JsonResponse(error_msg)
