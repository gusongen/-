from django.core import serializers
from django.core.paginator import *
from django.http import HttpResponse, JsonResponse
from main.models import Item


def item(request):
    """
    * get
    itn:item_num每次取得贴子条数
    st:start_pos:开始条数
    cat:catalog :分类
    tag:拼音缩写 JY ZH PC XK XR TC todo 管理员自定义
    # todo :缓存

    *post
    """
    res = ""
    if request.method == "GET":
        item_num = request.GET.get('itn', 10)
        start_pos = request.GET.get("st", None)
        catalog = request.GET.get("cat", "all")  # TODO
        page = request.GET.get("pg", 1)
        # 上拉刷新
        if start_pos is None:
            select_obj = Item.objects.all()
            start_pos = Item.objects.order_by('-pk').first().id;
            # 下拉刷新,前端自动返回启刷的id
        else:
            # 只搜索id值小于起始点的
            select_obj = Item.objects.filter(pk__lte=start_pos)
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

        print(content)
        # content=serializers.serialize("json", content, ensure_ascii=False)
        content = list(content)
        data = {'mag': 'ok', 'status': 200, 'per_page': int(paginator.per_page), 'num_page': int(paginator.num_pages),
                'start_pos': start_pos,
                "page_now":page,
                'content': content}
        return JsonResponse(data)
    # end if
    ###########
    # 发帖
    elif request.method == "POST":
        i_title = request.POST.get('ttl', False)
        i_content = request.POST.get('cnt', False)  # 内容
        i_tag = request.POST.get('tag', False)  # 标签
        i_p_id = request.POST.get('p_id', False)  # 发帖人id  #todo 身份验证
        i_id = request.POST.get('i_id', False)
        print(i_p_id)
        print(i_content)
        print(i_title)
        print(i_tag)
        if i_title and i_tag and i_content and i_p_id:
            dict_to_add = {'i_title': i_title, 'i_content': i_content, 'i_tag': i_tag, 'i_p_id': i_p_id}
            try:
                if not i_id:
                    Item(**dict_to_add).save()
                    return JsonResponse({"msg": 'add_success', 'status': 200})
                else:
                    Item.objects.filter(pk=i_id).update(**dict_to_add)  # 创建并写入数据库
                    return JsonResponse({"msg": 'update_success', 'status': 200})
            except Exception as e:
                res = str(e)
        else:
            res = "missing argument"
    elif request.method == "DELETE":
        i_p_id = request.GET.get('p_id', False)  # 发帖人id  #todo 身份验证
        i_id = request.GET.get('i_id', False)
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
