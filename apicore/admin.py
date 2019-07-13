from django.contrib import admin
from .models import Profile, Server, ServerUser, Extension, Career, FilesUser

# Register your models here.
admin.site.register(Profile)
admin.site.register(Server)
admin.site.register(ServerUser)
admin.site.register(FilesUser)
admin.site.register(Extension)
admin.site.register(Career)