from django.urls import  path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('chanpin',views.chanpin,name = 'chanpin'),
    path('liyong',views.liyong,name = 'liyong'),
    path('liuyan',views.liuyan,name = 'liuyan'),
    path('upload',views.upload,name = 'upload'),
    path('women',views.women,name = 'women'),
    path('newsa',views.newsa,name = 'newsa'),
    path('newsb',views.newsb,name = 'newsb'),
    path('newsc',views.newsc,name='newsc'),
    path('newsd',views.newsd,name='newsd'),
    path('xinwen',views.xinwen,name = 'xinwen'),
    path('zhishi',views.zhishi,name = 'zhishi'),
    path('upload1',views.upload1,name = 'upload1'),
    # path('upload1',views.upload1,name = 'upload1'),    
]
