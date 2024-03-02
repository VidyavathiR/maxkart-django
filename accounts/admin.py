from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'last_name', 'first_name', 'date_joined', 'is_active', 'last_login')
    # readonly_fields = ('password',)  # to make the password field read-only
    filter_horizontal = ()
    list_filter = ()
    fieldsets  = ()

admin.site.register(Account, AccountAdmin)