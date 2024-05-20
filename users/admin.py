from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        #a tuple of two-tuples defining the layout of form fields in the admin interface. 
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('shipping_address', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        #Similar to fieldsets, this defines the layout of form fields for adding new user instances. 
        #It's used when adding a new user through the admin interface.
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    #This is a tuple specifying the fields to display in the list view of user instances in the admin interface
    list_display = ('username', 'email', 'is_staff', 'date_joined')
    #This is a tuple specifying the fields that can be searched in the admin interface. 
    search_fields = ('username', 'email')
    #This specifies the default sorting order of user instances in the admin interface
    ordering = ('username',)

#The admin.site.register(User, UserAdmin) line registers the User model with the custom admin configuration defined by UserAdmin
admin.site.register(User, UserAdmin)
