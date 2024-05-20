from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)