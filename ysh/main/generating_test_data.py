from main.models import  User, Item

base_name = "你好世界"
for i in range(10):
    tt=User(u_name=base_name + str(i),
         u_pwd="123445")
    tt.save()
    Item(i_title=base_name + str(i),
         i_content=base_name + str(i),
         i_p_id=tt).save()

