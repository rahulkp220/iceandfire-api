import json
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from .views import BookViewset, ExternalBookView
from .models import Book, Author


class ExternalBookViewTest(TestCase):

    def test_get_without_data(self):
        response = self.client.get('/api/external-books/?name=Test')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
                'status_code': 200,
                'status': 'success',
                'data': []
            })

    def test_get_with_data(self):
        response = self.client.get('/api/external-books/?name=A%20Game%20of%20Thrones')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
                "status_code": 200,
                "status": "success",
                "data": [
                    {
                        "name": "A Game of Thrones",
                        "isbn": "978-0553103540",
                        "authors": [
                            "George R. R. Martin"
                        ],
                        "number_of_pages": 694,
                        "publisher": "Bantam Books",
                        "country": "United States",
                        "release_date": "1996-08-01"
                    }
                ]
            })


class BookViewset(APITestCase):

    def setUp(self):
        self.author = Author(name="Test Author")
        self.author.save()

        self.book = Book(
            name="Test Book",
            isbn="123456788",
            number_of_pages=888,
            publisher="Test Publisher",
            country="India",
            release_date="2019-05-28"
        )
        self.book.save()
        self.book.authors.add(self.author)

    def test_create(self):
        test_data = {
            "name": "Sample Book",
            "isbn": "123456789",
            "authors": [{
                "name": "Sample Author"
            }],
            "number_of_pages": 999,
            "publisher": "Sample Publisher",
            "country": "India",
            "release_date": "2019-05-28"
        }
        response = self.client.post(
            reverse('v1:books-list'),
            data=json.dumps(test_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
            "status_code": 201,
            "status": "success",
            "data": {
                "id": 2,
                "name": "Sample Book",
                "isbn": "123456789",
                "authors": [
                    "Sample Author"
                ],
                "number_of_pages": 999,
                "publisher": "Sample Publisher",
                "country": "India",
                "release_date": "2019-05-28"
            }
        })

    def test_list(self):
        response = self.client.get(reverse('v1:books-list'))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
            "status_code": 200,
            "status": "success",
            "data": [
                {
                    "id": self.book.id,
                    "name": "Test Book",
                    "isbn": "123456788",
                    "authors": [
                        "Test Author"
                    ],
                    "number_of_pages": 888,
                    "publisher": "Test Publisher",
                    "country": "India",
                    "release_date": "2019-05-28"
                }
            ]
        })

    def test_retrieve(self):
        response = self.client.get(reverse('v1:books-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
            "status_code": 200,
            "status": "success",
            "data": {
                "id": self.book.id,
                "name": "Test Book",
                "isbn": "123456788",
                "authors": [
                    "Test Author"
                ],
                "number_of_pages": 888,
                "publisher": "Test Publisher",
                "country": "India",
                "release_date": "2019-05-28"
            }
        })

    def test_patch(self):
        patch_data = {
            "name": "Patch Book",
            "isbn": "123456788",
            "authors": [{
                "name": "Test Author"
            }],
            "number_of_pages": 999,
            "publisher": "Test Publisher",
            "country": "India",
            "release_date": "2019-05-28"
        }
        response = self.client.patch(
            reverse('v1:books-detail', kwargs={'pk': self.book.id}),
            data=json.dumps(patch_data), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
            "status_code": 200,
            "status": "success",
            "message": "The book Patch Book was updated successfully",
            "data": {
                "id": self.book.id,
                "name": "Patch Book",
                "isbn": "123456788",
                "authors": [
                    "Test Author"
                ],
                "number_of_pages": 999,
                "publisher": "Test Publisher",
                "country": "India",
                "release_date": "2019-05-28"
            }
        })

    def test_destroy(self):
        response = self.client.delete(reverse('v1:books-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
            'status_code': 204,
            'status': 'success',
            'message': 'The book Test Book was deleted successfully',
            'data': []
        })