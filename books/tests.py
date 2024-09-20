from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="ML",
            subtitle="ML",
            author="Amirreza Hosseini",
            isbn="12345678901234", 
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "ML")
        self.assertEqual(self.book.subtitle, "ML")    
        self.assertEqual(self.book.author, "Amirreza Hosseini")    
        self.assertEqual(self.book.isbn, "12345678901234")        

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hosseini")
        self.assertTemplateUsed(response, "books/book_list.html")