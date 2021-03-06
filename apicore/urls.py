from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from apicore import views

urlpatterns = [
    path('extensions/', views.ExtensionList.as_view()),
    path('extensions/<int:pk>/', views.ExtensionDetail.as_view()),
    path('careers/', views.CareerList.as_view()),
    path('careers/<int:pk>/', views.CareerDetail.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('servers/', views.ServerList.as_view()),
    path('servers/<int:pk>/', views.ServerDetail.as_view()),
    path('servers-users/', views.ServerUserList.as_view()),
    path('servers-users/<int:pk>/', views.ServerUserDetail.as_view()),
    path('server-info/', views.LocalServerView.as_view()),
    path('media-files/', views.FilesUserList.as_view()),
    path('media-files/<int:pk>/', views.FilesUserDetail.as_view()),
    path('command/', views.CommandServerView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# Custom title for Administration Panel
admin.site.site_header = "uEasyShare Server"
admin.site.site_title = "uEasyShare"
admin.site.index_title = "Bienvenido(a) al Panel de Administración de uEasyShare server"