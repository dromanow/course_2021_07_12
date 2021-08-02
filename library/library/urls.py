"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token
from authors.views import AuthorViewSet, BookViewSet, BiographyViewSet
# from authors.views import AuthorView

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('books', BookViewSet)
router.register('biography', BiographyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token)
    # path('api/filter/kwargs/<str:first_name>/', AuthorListAPIView.as_view())
    # path('api/authors/', AuthorView.as_view()),
    # path('api/authors/<int:pk>/', AuthorRetrieveAPIView.as_view()),
    # path('api/authors/<int:pk>/', AuthorDestroyAPIView.as_view())
    # path('api/authors/', get_authors)
]
