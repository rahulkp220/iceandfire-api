import json
from django.test import TestCase, Client
from rest_framework.test import APIClient

from .views import BookViewset, ExternalBookView


# Create your tests here.
class ExternalBookViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        client = Client()

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


class BookViewset(TestCase):
    client = APIClient()

    def test_create(self):
        test_data = {
            "name": "Sample Book",
            "isbn": "123456789",
            "authors":[{
                "name":"Sample Author"
            }],
            "number_of_pages": 999,
            "publisher": "Sample Publisher",
            "country": "India",
            "release_date":"2019-05-28"
        }
        response = self.client.post(
            '/api/v1/books/', 
            data=json.dumps(test_data), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {
            "status_code": 201,
            "status": "success",
            "data": {
                "id": 1,
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
        response = self.client.get('/api/v1/books/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get('/api/v1/books/1/')
        self.assertEqual(response.status_code, 404)

    def test_patch(self):
        response = self.client.get('/api/v1/books/1/')
        self.assertEqual(response.status_code, 404)

    def test_destroy(self):
        response = self.client.get('/api/v1/books/1/')
        self.assertEqual(response.status_code, 404)