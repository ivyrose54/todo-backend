from django.contrib import admin
from .models import TodoItem  # Import your model

# Register the ToDoItem model
admin.site.register(TodoItem)