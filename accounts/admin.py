from django.contrib import admin

from accounts.models import InviteCode, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User
    """

    list_display = "id", "username", "email", "first_name", "last_name"
    list_display_links = "id", "username", "email", "first_name", "last_name"
    search_fields = "id", "username"


@admin.register(InviteCode)
class InviteCodeAdmin(admin.ModelAdmin):
    """
    InviteCode
    """

    list_display = "code",
    list_display_links = "code",
