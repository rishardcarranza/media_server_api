from django.contrib import admin
from .models import UserProfile, Server, ServerUser, Extension, Career, FilesUser, CommandServer, FileType, FilesUser
from django.contrib.auth.models import Group

# Register your models here.
# class ServerUserAdmin(admin.ModelAdmin):
#     readonly_fields = ('connect_date', 'last_date')
#     list_display = ('user', 'server', 'status')

class ServerAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip_address', 'port')

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'career')

class ExtensionAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

# class CareerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status')

class CommandServerAdmin(admin.ModelAdmin):
    list_display = ('action', 'file_type', 'command', 'status')
    search_fields = ('action',)
    list_filter = ('file_type__name',)

class FileTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_extensions', 'status')

class FilesUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'file')
    search_fields = ('user__username', 'file')

# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Server, ServerAdmin)
# admin.site.register(ServerUser, ServerUserAdmin)
admin.site.register(Extension, ExtensionAdmin)
# admin.site.register(Career, CareerAdmin)
admin.site.register(CommandServer, CommandServerAdmin)
admin.site.register(FileType, FileTypeAdmin)
admin.site.register(FilesUser, FilesUserAdmin)
admin.site.unregister(Group)
