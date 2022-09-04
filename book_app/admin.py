from django.contrib import admin

# Register your models here.
from .models import BOOK, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('title',)}
    list_filter =  ('author', 'rating')
    list_display = ('title', 'author')


admin.site.register(BOOK, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)