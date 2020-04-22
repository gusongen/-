from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('hello/', views.hello, name='hello')
    path('login/', views.login, name='login'),
    path('reg/', views.register, name='reg'),
    path('main/', views.main, name='main'),
    path('classify/', views.classify, name='classify'),

]
