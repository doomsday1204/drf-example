"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women.views import *
from rest_framework import routers
from rest_framework.routers import Route, DynamicRoute, SimpleRouter
#
# class CustomReadOnlyRouter(SimpleRouter):
#     """
#     A router for read-only APIs, which doesn't use trailing slashes.
#     """
#     routes = [
#         Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         ),
#         DynamicRoute(
#             url=r'^{prefix}/{lookup}/{url_path}$',
#             name='{basename}-{url_name}',
#             detail=True,
#             initkwargs={}
#         )
#     ]
# router = routers.SimpleRouter()
# router.register(r'women', WomenViewSet)
#router = routers.SimpleRouter()
#
# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls))
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path(r'api/v1/auth/', include('djoser.urls')), #djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')), #djoser
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', TokenVerifyView.as_view(), name='token_verify'),

]
