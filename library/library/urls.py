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
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import obtain_auth_token
from authors.views import AuthorViewSet, BookViewSet, BiographyViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView
# from authors.urls import urlpatterns
# from authors.views import AuthorView

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('biography', BiographyViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Authors',
        default_version='v1',
        description='Some description',
        contact=openapi.Contact('some@mail.com')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False))),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui()),

    # path('api/1.0/authors/', include('authors.urls', namespace='v1')),
    # path('api/2.0/authors/', include('authors.urls', namespace='v2')),
    # path('api/3.0/authors/', include('authors.urls', namespace='v3')),
    #
    # re_path(r'^api/(?P<version>(v1|v2))/authors/', AuthorViewSet.as_view({'get': 'list'})),
    # re_path(r'^api/(?P<version>(v1|v2))/authors/(<pk>)', AuthorViewSet.as_view({'get': 'details'}))

    # path('api/filter/kwargs/<str:first_name>/', AuthorListAPIView.as_view())
    # path('api/authors/', AuthorView.as_view()),
    # path('api/authors/<int:pk>/', AuthorRetrieveAPIView.as_view()),
    # path('api/authors/<int:pk>/', AuthorDestroyAPIView.as_view())
    # path('api/authors/', get_authors)
]
