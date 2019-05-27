from datetime import datetime
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    SlugRelatedField
)
from .models import Book, Author


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

    def create(self, validated_data):
        instance = Book.objects.create(**validated_data)
        for author in authors:
            instance.authors.add(author)

        return instance

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
