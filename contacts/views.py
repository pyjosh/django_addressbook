# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from contacts.models import Address, Contact

import forms



#The ListView that we subclass from is itself composed of several mixins that provide some behaviour !!!
class ListContactView(ListView):

    model = Contact                             # this view is going to list all the Contacts in our database
    template_name = 'contact_list.html'



# Most generic views that do form processing have 
# the concept of the 'success URL': where to redirect 
# the user when the form is successfully submitted.
class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'
    # after adding 'email_filed' in forms.py we have to tell this view to use it
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')   # contact_list - the name of a view defined in URLS !

    # in order to use the same template for create and update (add/edit) we have to add info
    # about where the form should redirect to the context
    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')

        return context


class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'edit_contact.html'
    # after adding 'email_filed' in forms.py we have to tell this view to use it
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    # in order to use the same template for create and update (add/edit) we have to add info
    # about where the form should redirect to the context
    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit', kwargs = {'pk': self.get_object().id})

        return context

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class ContactView(DetailView):

    model = Contact
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        home_addresses = Address.objects.filter(contact_id=self.get_object().id, address_type='HOME')
        context['home_address'] = home_addresses[0] if home_addresses else None

        return context




#
# to work with Contact and Address models together
#
# class EditContactAddressView(UpdateView):

#     model = Contact                     # inline formset takes the parent object as its starting point
#     template_name = 'edit_addresses.html'
#     form_class = forms.ContactAddressFormSet

#     def get_success_url(self):

#         # redirect to the Contact view.
#         return self.get_object().get_absolute_url()

class EditContactAddressView(UpdateView):

    model = Address                     # inline formset takes the parent object as its starting point
    template_name = 'edit_addresses.html'
    #form_class = forms.ContactAddressFormSet

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(EditContactAddressView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit-addresses', kwargs = {'pk': self.get_object().id})

        return context