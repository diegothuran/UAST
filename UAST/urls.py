"""
Definition of urls for Diego.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views

import pessoal.forms
import pessoal.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', pessoal.views.home, name='home'),
    url(r'^contact$', pessoal.views.contact, name='contact'),
    url(r'^about', pessoal.views.about, name='about'),
    url(r'^lp', pessoal.views.lp, name='lp'),
    url(r'^postagem/(?P<pk>[0-9]+)/', pessoal.views.NoticiaDetailView.as_view(), name='noticia'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'pessoal/login.html',
            'authentication_form': pessoal.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

]
