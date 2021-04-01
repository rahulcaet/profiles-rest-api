from django.urls import path
from profiles_api import views

urlpatterns = [
    path(r'hello-view/', views.HelloApiView.as_view(), name='hello-view')
]