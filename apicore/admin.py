from django.contrib import admin
from .models import Profile, Server, ServerUser, Extension, Career, FilesUser

# Register your models here.
class ServerUserAdmin(admin.ModelAdmin):
    readonly_fields = ('connect_date', 'last_date')
    list_display = ('user', 'server', 'status')

class ServerAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip_address', 'port')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'career')

class ExtensionAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(ServerUser, ServerUserAdmin)
admin.site.register(FilesUser)
admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Career, CareerAdmin)