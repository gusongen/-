from django.db import models

from main.models import Item, User


# 共有类
class BaseRemark(models.Model):
    R_Po = models.ForeignKey(User, on_delete=models.CASCADE)  # 评论人的ID
    R_Po_name =models.CharField(max_length=32,default="")
    R_like = models.IntegerField(default=0)  # 收到的点赞数
    R_remark_num = models.IntegerField(default=0)  # 评论数目
    time = models.DateTimeField(auto_now_add=True)  # 创建时间
    R_content = models.TextField(max_length=500)  # 评论内容

    def save(self,*args, **kwargs):
        try:
            self.R_Po_name=self.R_Po.u_name
        except Exception as e:
            print(e)
        super().save(*args, **kwargs)


# 一级评论,评论帖子
class RemarkI(BaseRemark):
    R_item = models.ForeignKey(Item, on_delete=models.CASCADE)  # 对应贴子的外键

    class Meta:
        ordering = ['-time']


# 二级评论,评论一级或二级评论
class RemarkR(BaseRemark):
    R_remark = models.ForeignKey(RemarkI, on_delete=models.CASCADE,related_name="RemarkR")  # 一级评论外键,所有均有
    R_replay = models.ForeignKey("self", on_delete=models.CASCADE, null=True)  # 评论的二级评论(如果评论的是一级评论这里就是空),如果为空则不用再次引用
    R_replay_to_name=models.CharField(max_length=32,null=True)

    class Meta:
        ordering = ['time']

    def save(self,*args, **kwargs):
        if self.R_replay :
            try:
                self.R_replay_to_name=self.R_Po.u_name
            except Exception as e:
                print(e)
        super().save(*args, **kwargs)

