from django.db import models


# Create your models here.


class Item(models.Model):  # 贴子
    i_title = models.CharField(max_length=32, null=False)  # 标题
    i_content = models.CharField(max_length=200, null=False)  # 内容
    i_tag = models.CharField(max_length=128, null=True)  # 标签
    i_p_id = models.CharField(max_length=32,null=False)  # 发帖人id
    i_time = models.DateTimeField(auto_now=True)


class User(models.Model):
    u_name = models.CharField(max_length=32, null=False)
    u_pwd = models.CharField(max_length=32, null=False)
