from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Article
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class CustomAdminSite(AdminSite):
    site_header = "Upwrite Publication Admin"
    site_title = "Upwrite Admin"
    index_title = "Welcome to the Admin Dashboard"

    def each_context(self, request):
        context = super().each_context(request)
        context['site_logo'] = '/static/images/logo.png'
        return context

    class Media:
        css = {
            'all': ('news/admin.css',)
        }

custom_admin_site = CustomAdminSite(name='custom_admin')

custom_admin_site.register(Article)
custom_admin_site.register(User)
custom_admin_site.register(Group)


# # Inline admin for Profile
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'

# # Extend UserAdmin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)
#     list_display = ('username', 'first_name', 'last_name', 'email', 'get_contact_number', 'is_staff')
#     search_fields = ('username', 'email', 'first_name', 'last_name')

#     def get_contact_number(self, obj):
#         return obj.profile.contact_number
#     get_contact_number.short_description = 'Contact Number'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'is_published', 'created_at')
    list_filter = ('section', 'is_published')
    search_fields = ('title', 'content')

    def has_module_permission(self, request):
        return request.user.groups.filter(name='Editor').exists()

    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name='Editor').exists()

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Editor').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Editor').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Editor').exists()

# Unregister default User and register new
# custom_admin_site.unregister(User)
# custom_admin_site.register(User, UserAdmin)


