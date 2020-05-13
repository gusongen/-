from django.db import models

from main.storage import ImageStorage


# Create your models here.

class User(models.Model):
    u_name = models.CharField(max_length=32)
    u_pwd = models.CharField(max_length=32)
    u_ico = models.ImageField(upload_to='userIco/%Y/%m/%d/',
                              storage=ImageStorage(), null=True,
                              default=r"userIco\default_ico\default.jpeg")
    u_nname = models.CharField(max_length=32)  # 昵称,默认是账号

    def save(self, *args, **kwargs):
        if self.u_nname is None:
            self.u_nname = self.u_name
        super().save(*args, **kwargs)


class Item(models.Model):  # 贴子
    i_title = models.CharField(max_length=32, null=False)  # 标题
    i_content = models.CharField(max_length=200, null=False)  # 内容
    i_tag = models.CharField(max_length=128, null=True)  # 标签
    i_p_id = models.ForeignKey(User, null=False, related_name="item", on_delete=models.CASCADE)  # 发帖人id
    i_time = models.DateTimeField(auto_now_add=True)
    # todo 外键
    # 新加点赞数和评论数
    i_remark_num = models.IntegerField(default=0)
    i_like_num = models.IntegerField(default=0)


class Image(models.Model):
    file = models.ImageField(upload_to='itemPic/%Y/%m/%d/', storage=ImageStorage())  # 按日期分文件夹
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # 图片对贴子是多对一,外键,级联删除


class UserLikeItem(models.Model):
    i_pk = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='likers')
    u_pk = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likedItems')
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.i_pk.i_like_num += 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.i_pk.i_like_num -= 1
        super().delete(*args, **kwargs)
