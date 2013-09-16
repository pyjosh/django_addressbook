from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import contacts.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^addressbook/', include('addressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # FOR LIST CONTACTS
    url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list',),   # Giving a URL pattern a name allows you to do a reverse lookup
    # FOR CREATE
    url(r'^new$', contacts.views.CreateContactView.as_view(), name='contacts-new',),
    # FOR UPDATE
    url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(), name='contacts-edit',),
    # FOR DELETE
    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(), name='contacts-delete',),
    # TO PRESENT SINGLE CONTACT
    url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(), name='contacts-view',),
    # for CONTACT and ADDRESS
    url(r'^edit/(?P<pk>\d+)/addresses$', contacts.views.EditContactAddressView.as_view(), name='contacts-edit-addresses',),
)


urlpatterns += staticfiles_urlpatterns()