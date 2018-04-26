from __future__ import unicode_literals

from django import forms

from todo.models import Todo

class DeleteTodo(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'