# -*- coding: utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from models import Article, Category
from django.views import generic

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pessoal/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pessoal/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pessoal/about.html',
        {
            'title':'Sobre',
            'message':'Página contendo informações sobre mim.',
            'year':datetime.now().year,
        }
    )

def lp(request):
    assert isinstance(request, HttpRequest)
    postagens = Article.objects.filter(category__name="lp").order_by('created_time').reverse()
    return render(
        request,
        'pessoal/lp.html',
        {
            'title': 'Laboratório de Programação',
            'message': 'Your pessoallication description page.',
            'year': datetime.now().year,
            'postagens': postagens,
        }
    )

def pds(request):
    assert isinstance(request, HttpRequest)
    postagens = Article.objects.filter(category__name="pds")
    return render(
        request,
        'pessoal/lp.html',
        {
            'title': 'Processo de Desenvolvimento de Software',
            'message': 'Your pessoallication description page.',
            'year': datetime.now().year,
            'postagens': postagens,
        }
    )

def ie(request):
    assert isinstance(request, HttpRequest)
    postagens = Article.objects.filter(category__name="ie")
    return render(
        request,
        'pessoal/lp.html',
        {
            'title': 'Instrumentação para o Ensino',
            'message': 'Your pessoallication description page.',
            'year': datetime.now().year,
            'postagens': postagens,
        }
    )

class NoticiaDetailView(generic.DetailView):
    model = Article
    template_name = 'pessoal/noticia.html'