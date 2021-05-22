from django.contrib import admin
from book.models import *  # 卡壳点：没有使用 包.模块 导致出错
# Register your models here.
class BookinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class PeopleinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']

admin.site.register(Bookinfo, BookinfoAdmin)
admin.site.register(Peopleinfo, PeopleinfoAdmin)