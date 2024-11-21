from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title='The Great Gatsby', author='F. Scott Fitzgerald', publication_date='1925-04-10')
        Book.objects.create(title='To Kill a Mockingbird', author='Harper Lee', publication_date='1960-07-11')

    def test_book_creation(self):
        """Test that books are created successfully"""
        book1 = Book.objects.get(title='The Great Gatsby')
        book2 = Book.objects.get(title='To Kill a Mockingbird')
        
        self.assertEqual(book1.author, 'F. Scott Fitzgerald')
        self.assertEqual(book2.author, 'Harper Lee')

    def test_book_count(self):
        """Test the number of books in the database"""
        self.assertEqual(Book.objects.count(), 2)