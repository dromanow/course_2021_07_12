import io
import os

from rest_framework import serializers
from python_models import Author, Biography, Book


class AuthorSerializer(serializers.Serializer):
    # def update(self, instance, validated_data):
    #     print('Update')
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
    #     return instance
    #
    # def create(self, validated_data):
    #     print('Create')
    #     return Author(**validated_data)
    #
    # def validate_birthday_year(self, value):
    #     if value < 0:
    #         raise serializers.ValidationError('Год должен быть больше нуля')
    #     return value
    #
    # def validate(self, attrs):
    #     if attrs['name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
    #         raise serializers.ValidationError('Неверный год рождения Пушкина')
    #     return attrs

    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()


class BiographySerializer(serializers.Serializer):
    text = serializers.CharField(max_length=128)
    author = AuthorSerializer()


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    authors = AuthorSerializer(many=True)


def run():
    author = Author('Пушкин', 1799)
    author1 = Author('Грин', 1880)
    book = Book('name', [author, author1])
    serializer = BookSerializer(book)
    print(serializer.data)

    from rest_framework.renderers import JSONRenderer
    renderer = JSONRenderer()
    json_bytes = renderer.render(serializer.data)
    print(json_bytes)


    # print(type(json_bytes))

    # from rest_framework.parsers import JSONParser
    # stream = io.BytesIO(json_bytes)
    # data = JSONParser().parse(stream)
    # print(data)  # {'name': 'Грин', 'birthday_year': 1880}
    # print(type(data))  # <class 'dict'>

    # author1 = Author('Грин', 1880)
    # serializer = AuthorSerializer(author1, data={'name': 'Пушкин', 'birthday_year': -1800})
    # if serializer.is_valid():
    #     author = serializer.save()
    #     print(author)
    #     print(author.birthday_year)
    # else:
    #     print(serializer.errors)

    # print(type(serializer.validated_data))

#
# data = {'name': 'Грин', 'birthday_year': 1880}
# serializer = AuthorSerializer(data=data)
# serializer.is_valid()
# author = serializer.save()

# data = {'name': 'Александр', 'birthday_year': 1880}
# serializer = AuthorSerializer(author, data=data)
# serializer.is_valid()
# author = serializer.save()
#
# data = {'birthday_year': 2000}
# serializer = AuthorSerializer(author, data=data, partial=True)
# serializer.is_valid()
# author = serializer.save()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.library.settings')
    run()

if __name__ == '__main__':
    main()
