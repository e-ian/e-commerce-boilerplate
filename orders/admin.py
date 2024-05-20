from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    #In Django admin, inline model admins are used to display and edit related models on the same page as the parent model.
    #admin.TabularInline: This is the base class for inline model admins that display related models in a tabular format (i.e., a table).
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'order_date', 'shipping_address')
    search_fields = ('user__username', 'user__email', 'shipping_address')
    list_filter = ('order_date',)
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
