from django.urls import path
from book import views

# 这个是固定写法 urlpatterns = []
urlpatterns = [
    # path(路由， 视图函数名)
    path('index/', views.index)
]