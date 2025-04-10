from django.contrib import admin
from .models import Category,Gender,ThriftRegister,Purchased

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

class GenderAdmin(admin.ModelAdmin):
    list_display = ('id','gender')
    list_display_links = ('id','gender')

class ThriftRegisterAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

class PurchasedAdmin(admin.ModelAdmin):
    list_display = ('id','user')
    list_display_links = ('id','user')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(ThriftRegister, ThriftRegisterAdmin)
admin.site.register(Purchased,PurchasedAdmin)