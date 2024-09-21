from django.contrib import admin
#a10
from . models import Task

#a15
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',)

#a9
admin.site.register(Task, TaskAdmin)
