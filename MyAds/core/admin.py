from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from django.utils.translation import gettext_lazy as _
# Register your models here.



@admin.register(MyUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id","username")
    list_filter = ("is_active", "is_staff", "groups")
    search_fields = ("username",)
    ordering = ("username",)
 

    fieldsets = (
        (None, {"fields": ("username",)}),
        (
            _("Permissions"),
            {"fields": ("is_active","is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("phone", "password1", "password2")}),)
