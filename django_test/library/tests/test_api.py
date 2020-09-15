from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Books
from books.serializers import BookSerializer


class TestBookListAPIView(APITestCase):
    def test_get(self):
        book_1 = Books.objects.create(
            title='Test1 Titile1',
            author_name='Test1 author1',
            description='Test1 description1'
        )
        book_2 = Books.objects.create(
            title='Test2 Titile2',
            author_name='222aaaaaaaaaaaaaaaa',
            description='Test2 description2'
        )
        url = reverse('books-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
