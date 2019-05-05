from django.contrib import admin

# Register your models here.

from .models import *

#admin.site.register(Person)

@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('email',)

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'date')
    search_fields = ('title',)
    list_filter = ('status',)
    date_hierarchy = ('date')