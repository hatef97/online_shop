from django.contrib import admin

from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'text', 'stars', 'active']


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'text', 'stars', 'datetime_modified', 'active']
