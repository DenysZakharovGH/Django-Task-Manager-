from django.contrib import admin

# Register your models here.

from .models import *

#admin.site.register(Person)

@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('email',)

class CheklistInLine(admin.TabularInline):
    model = Cheklist
    extra = 0

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'doer', 'status', 'stasus_in_percents', 'deadline')
    search_fields = ('title',)
    list_filter = ('status',)
    date_hierarchy = ('date')
    inlines = [CheklistInLine]

@admin.register(Cheklist)
class CheklistModelAdmin(admin.ModelAdmin):
    list_display = ('active', 'body',)
    search_fields = ('body',)
    raw_id_fields = ('task',)