from django.forms import ModelForm
from .models import Todo

class NewTodoItem(ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
       