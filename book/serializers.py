from datetime import datetime
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from .models import Book, Author
from django.contrib.auth.validators import UnicodeUsernameValidator


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ('name',)


class BookSerializer(ModelSerializer):
    authors = SerializerMethodField()
    release_date = SerializerMethodField()

    def get_authors(self, instance):
        qs = instance.authors.get_queryset()
        return [auth.name for auth in qs]

    def get_release_date(self, instance):
        return instance.release_date.strftime("%Y-%m-%d")

    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'isbn',
            'authors',
            'number_of_pages',
            'publisher',
            'country',
            'release_date'
        )
        depth = 1


class BookCreateUpdateSerializer(ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'isbn',
            'authors',
            'number_of_pages',
            'publisher',
            'country',
            'release_date'
        )
        # extra_kwargs = {
        #     'name': {
        #         'validators': [],
        #     }
        # }

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        instance = Book.objects.create(**validated_data)
        for author in authors_data:
            author_instance, created = Author.objects.get_or_create(**author)
            instance.authors.add(author_instance)
        return instance

    def update(self, instance, validated_data):
        authors_data = validated_data.pop('authors')
        authors = list((instance.authors).all())

        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.country = validated_data.get('country', instance.country)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()

        for author_data in authors_data:
            author = authors.pop(0)
            author.name = author_data.get('name', author.name)
            author.save()

        return instance
