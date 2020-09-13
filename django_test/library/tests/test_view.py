from django.db import connection
from django.urls import reverse
from rest_framework.test import APITestCase

from books.models import Books


class TestBookListAPIView(APITestCase):
    def test_missing_title(self):
        self.book_test = Books.objects.create(
            title='Test Titile',
            author_name='Test author',
            description='Test description'
        )
        self.book_test1 = Books.objects.create(
            title='Test1 Titile1',
            author_name='Test1 author1',
            description='Test1 description1'
        )

        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM books_books WHERE id = %s', [self.book_test.id])

        self.exp_books = [
            {
                'title': 'Test Titile',
                'author_name': 'Test author',
                'description': 'Test description'
            },
            {
                'title': 'Test1 Titile1',
                'author_name': 'Test1 author1',
                'description': 'Test1 description1'
            }
        ]
        resp = self.client.get(reverse('book-detail', args=[]))
        self.assertListEqual(self.exp_books, resp.data['results'])
