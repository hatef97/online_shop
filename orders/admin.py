from django.contrib import admin

from .models import Order, OrderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price', ]
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'fist_name', 'last_name', 'datetime_created', 'is_paid', ]
    inlines = [
        OrderItemInLine,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]
