from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase, APISimpleTestCase
from .views import AuthorViewSet
from .models import Author, Biography, Book
from django.contrib.auth.models import User
from mixer.backend.django import mixer


class TestAuthorViewSet(APITestCase):
    url = '/api/authors/'

    def setUp(self):
        factory = APIRequestFactory()
        self.request = factory.get(self.url)

    def test_get_list(self):
        view = AuthorViewSet.as_view({'get': 'list'})
        response = view(self.request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, {
            'first_name': 'Александр',
            'last_name': 'Пушкин',
            'birthday_year': 1800
        })
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_user(self):
        factory = APIRequestFactory()
        admin = User.objects.create_superuser('test', 'test@test.ru', 'qwerty')
        request = factory.post(self.url, {
            'first_name': 'Александр',
            'last_name': 'Пушкин',
            'birthday_year': 1800
        })
        force_authenticate(request, admin)
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        # author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1800)
        author = mixer.blend(Author, first_name='Александр')
        response = self.client.get(f'{self.url}{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), 'Александр')

    def test_post_client(self):
        User.objects.create_superuser('test', 'test@test.ru', 'qwerty')
        client = APIClient()
        client.login(username='test', password='qwerty')
        response = client.post(self.url, {
            'first_name': 'Александр',
            'last_name': 'Пушкин',
            'birthday_year': 1800
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()
        response = client.post(self.url, {
            'first_name': 'Александр',
            'last_name': 'Пушкин',
            'birthday_year': 1800
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_bio(self):
        biography = mixer.blend(Biography, author__first_name='Александр')
        response = self.client.get(f'/api/biography/{biography.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('text'), biography.text)
        response = self.client.get(f'/api/authors/{biography.author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), 'Александр')

    def test_book(self):
        author = mixer.blend(Author)
        book = mixer.blend(Book, authors=[author])
        response = self.client.get(f'/api/books/{book.id}/')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SimpleTest(APISimpleTestCase):
    def test_simple(self):
        self.assertEqual(1+2, 3)
