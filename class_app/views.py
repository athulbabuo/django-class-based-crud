from django.shortcuts import render

from .models import Book
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Bookcreateview(CreateView):

    model=Book

    template_name='home.html'

    fields=('title','price')

    success_url =reverse_lazy('booklist')

class Booklistview(ListView):

    model=Book

    template_name = 'listview.html'

    context_object_name='books'

class Bookdetailview(DetailView):

    model=Book

    template_name = 'details.html'

    context_object_name='Book'

class Bookupdateview(UpdateView):

    model=Book

    template_name = 'update.html'

    fields=('title','price')

    success_url =reverse_lazy('booklist')

class Bookdeleteview(DeleteView):

    model=Book

    template_name ='Delete.html'

    context_object_name='Book'

    success_url =reverse_lazy('booklist')



