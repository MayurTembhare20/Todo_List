from django.contrib import admin

from todo.models import todolist

# Register your models here.
class todoadd(admin.ModelAdmin):
    list_display=('title','check_status')

admin.site.register(todolist,todoadd)

