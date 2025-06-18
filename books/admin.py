from django.contrib import admin
from .models import Book  # ✅ import the model

admin.site.register(Book)  # ✅ register it with admin
