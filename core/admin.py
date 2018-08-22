from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_dislpay = ['username', 'email', 'get_full_name']
    filter_horizontal = ['groups']
    exclude = ['password']
    readonly_fields = ['last_login', 'date_joined']

    def get_fields(self, request, queryset):
        fields = super().get_fields(request, queryset)
        return fields
