from django.contrib import admin
from .models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'title', 'published_year', 'publisher', 'price', 'remaining', 'author', 'category')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    pass

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    pass