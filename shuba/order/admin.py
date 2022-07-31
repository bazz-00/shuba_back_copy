from django.contrib import admin
from .models import Order, OrderComments, OrderPhotos, SpecialityOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')


class SpecialityOrderAdmin(admin.ModelAdmin):
    list_display = ['title']


class OrderCommentsAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'body', 'created', 'is_active')
    list_filter = ('is_active', 'created', 'updated')
    search_fields = ('order', 'user', 'body')


class OrderPhotosAdmin(admin.ModelAdmin):
    list_display = ('order', 'photo')


admin.site.register(Order, OrderAdmin)
admin.site.register(SpecialityOrder, SpecialityOrderAdmin)
admin.site.register(OrderComments, OrderCommentsAdmin)
admin.site.register(OrderPhotos, OrderPhotosAdmin)







