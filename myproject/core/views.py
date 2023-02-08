from django.views.generic.list import ListView
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import *
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic import DetailView


# Create your views here.
def index(request):
    return render(request , 'index.html')

class TodoListView(ListView):
    model = Todo
    paginate_by = 3
    template_name = "all_todos.html"
    def get_queryset(self):
        return Todo.objects.all().order_by('-id')
    


class TodoCreateView(CreateView):
    model = Todo
    fields = ['text']
    template_name = 'new_todos.html'
    success_url = '/all/'


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_detial.html"

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['text']
    template_name = 'update_todos.html'
    success_url = '/all/'
    
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "delete_todos.html"
    success_url = '/all/'
    
