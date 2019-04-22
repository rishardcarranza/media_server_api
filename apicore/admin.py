from django.contrib import admin
from .models import Profile, Server, ServerUser, Extension, FilesUser

# Register your models here.
admin.site.register(Profile)
admin.site.register(Server)
admin.site.register(ServerUser)
admin.site.register(Extension)
admin.site.register(FilesUser)