from django.test import TestCase, SimpleTestCase
from .models import Catalogue
from django.urls import reverse
from django.urls.base import resolve
from .views import home
from .forms import AddBookForm


class CatalogueTemplateTests(SimpleTestCase):

    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'E-library Application')

    def test_hompage_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Hello World')

class CatalogueFormTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_book_form(self):
        form = self.response.context.get('add_book_form')
        self.assertIsInstance(form, AddBookForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_bootstrap_class_used_for_default_styling(self):
        form = self.response.context.get('add_book_form')
        self.assertIn('class="form-control"', form.as_p())

    def test_book_form_validation_for_blank_items(self):
        add_book_form = AddBookForm(
            data={'title': '', 'ISBN': '', 'author': '', 'price': '', 'availability': ''}
            )
        self.assertFalse(add_book_form.is_valid())

class ElibraryURLsTest(SimpleTestCase):

    def test_homepage_url_name(self):
        response = self.client.get(reverse(home))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

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
