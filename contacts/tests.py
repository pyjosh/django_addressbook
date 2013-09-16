"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from contacts.models import Contact
from django.test import TestCase


class ContactTest(TestCase):
	"""
	Contact model test.
	"""
	def test_unicode_return(self):
		contact = Contact(first_name='John', last_name='Travolta')

		self.assertEquals(unicode(contact), 'John Travolta')

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

