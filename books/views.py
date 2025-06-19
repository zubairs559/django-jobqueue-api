from django.db import transaction
from rest_framework import viewsets
from .models import Book, BookLog
from .serializers import BookSerializer
from .permissions import IsStaffOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStaffOrReadOnly]  # ✅ Updated to role-based permission

    def perform_create(self, serializer):
        with transaction.atomic():
            book = serializer.save()
            BookLog.objects.create(book=book, action="created")
