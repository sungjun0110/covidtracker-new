from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import State, Strategy, Kit, CustomUser, Photo

# custom user class
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 'state'
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(State)
admin.site.register(Strategy)
admin.site.register(Kit)
admin.site.register(Photo)