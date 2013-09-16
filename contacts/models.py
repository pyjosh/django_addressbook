from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Contact(models.Model):

    first_name = models.CharField(max_length=255,help_text='Please type your first name.',null=False,)
    last_name = models.CharField(max_length=255,null=False,)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    email = models.EmailField()

    # get_absolute_url is a Django convention for obtaining the URL of a single model instance
    # used in making the link to the single contact (contact preview)
    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})

    # def get_home_address(self):
    #     addresses = self.address_set.filter(address_type='HOME')
    #     return addresses[0] if addresses else None

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])



class Address(models.Model):
    ADDRESS_TYPE_CHOICES = (    # example of 2, there can be multiple selections
        ('HOME', 'Home'),
        ('OFFICE', 'Office'),
        ('PRIVATE', 'Private'),
    )

    contact         = models.ForeignKey(Contact)
    address_type    = models.CharField(max_length=255, choices=ADDRESS_TYPE_CHOICES, null=False,)
    address         = models.CharField(max_length=255)
    city            = models.CharField(max_length=255)
    state           = models.CharField(max_length=2)
    postal_code     = models.CharField(max_length=20)

    # there can NOT be two "john" with a_type: "home"
    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
        unique_together = ('contact', 'address_type',)