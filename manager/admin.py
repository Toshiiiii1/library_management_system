from django.contrib import admin
from .models import Author, Category, Book, Member, Term, Borrow, Detail

# define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cate_id', 'name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'title', 'published_year', 'publisher', 'price', 'remaining', 'display_author', 'display_category')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    pass


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    pass

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    pass

# Register your models here.
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Category)
# admin.site.register(Book)
# admin.site.register(Member)
# admin.site.register(Term)
# admin.site.register(Borrow)
# admin.site.register(Detail)