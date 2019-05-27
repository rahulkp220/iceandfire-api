import requests
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
from .models import Book
from .serializers import BookSerializer, AuthorSerializer


def external_books(request):
    query = request.GET.get('name', '')
    response = requests.get(f"https://www.anapioficeandfire.com/api/books?name={query}")
    data = []
    if response.ok:
        for d in response.json():
            data.append({
                'name': d['name'],
                'isbn': d['isbn'],
                'authors': d['authors'],
                'numberOfPages': d['numberOfPages'],
                'publisher': d['publisher'],
                'country': d['country'],
                'release_date': datetime.strptime(d['released'], '%Y-%m-%dT%H:%M:%S').strftime("%Y-%m-%d")
            })
    message = {
            'status_code': 200,
            'status': 'success',
            'data': data
        }
    return JsonResponse(message, safe=False)


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        name = self.request.query_params.get('name', None)
        country = self.request.query_params.get('country', None)
        publisher = self.request.query_params.get('publisher', None)
        release_date = self.request.query_params.get('release_date', None)

        if name is not None:
            return queryset.filter(name=name)
        elif country is not None:
            return queryset.filter(country=country)
        elif publisher is not None:
            return queryset.filter(publisher=publisher)
        elif release_date is not None:
            return queryset.filter(release_date__year=release_date)
        else:
            return queryset

    def list(self, request, *args, **kwargs):
        books = self.get_queryset()
        if books:
            serializer = BookSerializer(books, many=True)
            serializer_data = serializer.data
        else:
            serializer_data = []
        return Response({
            'status_code': 200,
            'status': 'success',
            'data': serializer_data
        })

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        return Response({
            'status_code': 201,
            'status': 'success',
            'data': BookSerializer(instance).data
        })

    def retrieve(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = BookSerializer(book)
        return Response({
            'status_code': 200,
            'status': 'success',
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        book_name = book.name
        book.delete()
        return Response({
            'status_code': 204,
            'status': 'success',
            'message': f'The book {book_name} was deleted successfully',
            'data': []
        })

    def partial_update(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = BookSerializer(book)
        return Response({
            'status_code': 200,
            'status': 'success',
            'data': serializer.data
        })
