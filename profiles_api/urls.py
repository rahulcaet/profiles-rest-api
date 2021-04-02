from django.urls import path, include
from profiles_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('helloprview', views.HelloViewSet, basename='hello')
router.register(r'profile', views.ProfileModelViewSet, basename='profile')

urlpatterns = [
    path(r'hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path(r'helloviews/', views.HelloViewSet.as_view({'get' : 'list'}), name='helloview'),
    path(r'', include(router.urls))
]