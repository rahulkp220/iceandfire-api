from django.contrib import admin

# Register your models here.
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book


class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)