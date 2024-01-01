from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('name','description','is_completed')
    list_filter=('is_completed',)
    list_editable=('is_completed',)
    search_fields=('name',)