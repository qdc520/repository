from django.shortcuts import render
from book.models import *


# Create your views here.




# def index(request):
#     return HttpResponse('AB122222222')


def index(request):
    dict1 = {'title': '首页', 'list': Bookinfo.objects.all()}
    return render(request, 'book/index.html', dict1)