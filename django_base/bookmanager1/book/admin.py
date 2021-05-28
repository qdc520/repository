from django.contrib import admin

# Register your models here.
from book.models import *
# Register your models here.

class BookinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pub_date', 'readcount', 'commentcount']

class PeopleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'description', 'is_delete', 'book']

admin.site.register(Bookinfo, BookinfoAdmin)
admin.site.register(Peopleinfo, PeopleAdmin)