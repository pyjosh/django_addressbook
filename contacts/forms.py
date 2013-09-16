from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from contacts.models import (
    Contact,
    Address,
)


class ContactForm(forms.ModelForm):

	# We are also adding an additional field, confirm_email
	confirm_email = forms.EmailField("confirm email", required=True)

	# here we associate our model with this form
	class Meta:
		model = Contact

	def __init__(self, *args, **kwargs):

		if kwargs.get('instance'):
			email = kwargs['instance'].email
			kwargs.setdefault('initial', {})['confirm_email'] = email

		return super(ContactForm, self).__init__(*args, **kwargs)

	# form (not filed) validation takes place here
	# all of the fields that validated are available in the cleaned_data dictionary
	# The 'clean' method may add, remove, or modify values, but must return the dictionary of cleaned data
	def clean(self):

		if (self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email')):
			raise ValidationError("Email must match !")

		return self.cleaned_data


# inlineformset_factory creates a Class from a parent model (Contact)
# to a child model (Address)
ContactAddressFormSet = inlineformset_factory(
    Contact,
    Address,
)