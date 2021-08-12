import graphene
from graphene_django import DjangoObjectType
from .models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)

    def resolve_all_authors(self, info):
        return Author.objects.all()

    all_books = graphene.List(BookType)

    def resolve_all_books(self, info):
        return Book.objects.all()

    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))

    def resolve_author_by_id(self, info, id):
        try:
            return Author.objects.get(id=id)
        except Author.DoesNotExist:
            return None

    books_by_author = graphene.List(BookType, name=graphene.String(required=False))

    def resolve_books_by_author(self, info, name=None):
        books = Book.objects.all()
        if name:
            books = books.filter(name=name)
        return books


class AuthorUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id, birthday_year):
        author = Author.objects.get(id=id)
        author.birthday_year = birthday_year
        author.save()
        return AuthorUpdateMutation(author=author)


class AuthorCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday_year):
        author = Author(first_name=first_name, last_name=last_name, birthday_year=birthday_year)
        author.save()
        return AuthorCreateMutation(author=author)


class Mutations(graphene.ObjectType):
    update_author = AuthorUpdateMutation.Field()
    create_author = AuthorCreateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
