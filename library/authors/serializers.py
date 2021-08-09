from rest_framework.serializers import ModelSerializer, StringRelatedField, HyperlinkedRelatedField, HyperlinkedModelSerializer
from .models import Author, Biography, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
    # def create(self, validated_data):
    #     res = super(AuthorSerializer, self).create(validated_data)
    #     res.birthday_year = 'zaaa'
    #     res.save()
    #     return res


class AuthorSerializerV2(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class BookSerializer(ModelSerializer):
    # authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

