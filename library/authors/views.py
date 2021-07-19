from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Author, Book, Biography
from .serializers import AuthorSerializer, BiographySerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BiographyViewSet(ModelViewSet):
    serializer_class = BiographySerializer
    queryset = Biography.objects.all()
