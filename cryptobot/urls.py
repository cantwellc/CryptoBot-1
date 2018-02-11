from django.conf.urls import url, include
from rest_framework import routers
from cryptobot import views

# use default router
router = routers.DefaultRouter()

# register viewsets with the router
router.register(r'users', views.UserViewSet)

# set router urls
urlpatterns = [
    url(r'^', include(router.urls)),
]
