from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_date')


class PostInline(admin.TabularInline):
    model = Post


class CustomUserAdmin(UserAdmin):
    inlines = [PostInline]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('info'), {'fields': ('phone', 'avatar', 'middle_name', 'gender', 'bio', 'status')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
