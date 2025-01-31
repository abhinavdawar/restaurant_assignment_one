from django.contrib import admin
from core.models import Product, Order, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'dish_name', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('is_veg', 'nationality')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
