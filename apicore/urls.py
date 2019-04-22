from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from apicore import views

urlpatterns = [
    path('extensions/', views.ExtensionList.as_view()),
    path('extensions/<int:pk>/', views.ExtensionDetail.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)