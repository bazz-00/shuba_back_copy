from django.contrib import admin
from .models import Executor, Speciality, ExecutorComments


class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['title']

class ExecutorCommentsAdmin(admin.ModelAdmin):
    list_display = ('executor', 'user', 'body', 'created', 'is_active')
    list_filter = ('is_active', 'created', 'updated')
    search_fields = ('executor', 'user', 'body')


admin.site.register(Executor, ExecutorAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(ExecutorComments, ExecutorCommentsAdmin)

