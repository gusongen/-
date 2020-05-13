# remarksys api
from django.contrib import admin
from django.urls import path
from remarksys import views

app_name = 'remarksys'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('api/', views.remark),

]
