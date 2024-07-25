# menu/admin.py
from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

admin.site.register(Menu, MenuAdmin)
