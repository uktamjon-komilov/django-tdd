from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)
    
    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b"<html>"))
        self.assertIn(b"<title>To-Do Lists</title>", response.content)
        self.assertTrue(response.content.endswith(b"</html>"))