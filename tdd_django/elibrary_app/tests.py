from django.test import TestCase

# Create your tests here.
from .models import Catalogue

class CatalogueModelTests(TestCase):

    def setUp(self):
        self.book = Catalogue(
            title = 'First Title',
            ISBN = '978-3-16-148410-0',
            author = 'Samuel Torimiro',
            price = '9.99',
            availability = 'True'
        )

    def test_create_book(self):
        self.assertIsInstance(self.book, Catalogue)

    def test_str_representation(self):
        self.assertEqual(str(self.book.title), "First Title")

    def test_saving_and_retrieving_book(self):
        first_book = Catalogue()
        first_book.title = 'First Title'
        first_book.ISBN = '978-3-16-148410-0'
        first_book.author = 'Samuel Torimiro'
        first_book.price = '9.99'
        first_book.availability = 'True'
        first_book.save()

        second_book = Catalogue()
        second_book.title = 'Second Title'
        second_book.ISBN = '978-3-16-148410-1'
        second_book.author = 'Hannah Torimiro'
        second_book.price = '19.99'
        second_book.availability = 'False'
        second_book.save()

        saved_books = Catalogue.objects.all()
        self.assertEqual(saved_books.count(), 2)

        first_saved_book = saved_books[0]
        second_saved_book = saved_books[1]
        self.assertEqual(first_saved_book.title, 'First Title')
        self.assertEqual(second_saved_book.author, 'Hannah Torimiro')
