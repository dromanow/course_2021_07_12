from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, get_object_or_404
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .models import Author, Book, Biography
from .serializers import AuthorSerializer, BiographySerializer, BookSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, \
    IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from rest_framework.authtoken.models import Token


# class AuthorView(ViewSet):
#     @action(methods=['GET'], detail=True)
#     def retrieve_name(self, request, pk=None):
#         author = get_object_or_404(Author, pk=pk)
#         return Response({'first_name': author.first_name})
#
#     @action(methods=['GET'], detail=False)
#     def list_all(self, request, pk=None):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def list(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data)

# class AuthorView(RetrieveModelMixin, ListModelMixin, GenericViewSet):
#     renderer_classes = [JSONRenderer]
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()


# class AuthorRetrieveAPIView(RetrieveAPIView):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()
#
#
# class AuthorDestroyAPIView(DestroyAPIView):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()

# def get_renderers(self):
#     return [JSONRenderer]

# def get_serializer(self, *args, **kwargs):
#     serializer = AuthorSerializer(authors, many=True)
#     return serializer
#
# def get(self, request, format=None):
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def get_authors(request):
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return Response(serializer.data)


# class AuthorPagination(LimitOffsetPagination):
#     default_limit = 2


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


    # permission_classes = [DjangoModelPermissions]
    # filterset_fields = ['first_name', 'last_name']
    # pagination_class = AuthorPagination

    # def get_queryset(self):
    #     first_name = self.request.query_params.get('first_name', None)
    #     if first_name:
    #         return Author.objects.filter(first_name=first_name)
    #     return Author.objects.all()


# class AuthorListAPIView(ListAPIView):
#     serializer_class = AuthorSerializer
#
#     def get_queryset(self):
#         first_name = self.kwargs['first_name']
#         return Author.objects.filter(first_name=first_name)


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BiographyViewSet(ModelViewSet):
    serializer_class = BiographySerializer
    queryset = Biography.objects.all()
