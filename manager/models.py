from django.db import models
from django.urls import reverse

# định nghĩa model Author
class Author(models.Model):
    # fields
    author_id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    
    class Meta:
        # sắp xếp record theo author_id
        ordering = ['author_id']
    
    def __str__(self):
        return f'{self.author_id}, {self.name}'
    
# định nghĩa model Category
class Category(models.Model):
    # fields
    cate_id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    
    class Meta:
        # sắp xếp record theo cate_id
        ordering = ['cate_id']
    
    def __str__(self):
        return f'{self.cate_id}, {self.name}'

# định nghĩa model Book
class Book(models.Model):
    # fields
    book_id = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=50)
    published_year = models.DateField()
    publisher = models.CharField(max_length=50)
    price = models.IntegerField()
    remaining = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        # sắp xếp record theo thứ tự book_id
        ordering = ['book_id']
    
    # hàm tạo url liên kết đến trang chi tiết cuốn sách
    def get_absolute_url(self):
        return reverse('books-detail', args=[str(self.book_id)])
    
    def __str__(self):
        return f'{self.book_id}, {self.title}, {self.published_year}, {self.publisher}, {self.price}, {self.remaining}, {self.author}, {self.category}'
    
# định nghĩa model Member
class Member(models.Model):
    # fields
    member_id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        # sắp xếp theo thứ tự member_id
        ordering = ['member_id']
    
    # hàm tạo url liên kết đến trang chi tiết thành viên
    def get_absolute_url(self):
        return reverse("member-detail", args=[str(self.member_id)])
    
    def __str__(self):
        return f'{self.member_id}, {self.name}'
    
# định nghĩa model Term
class Term(models.Model):
    term = models.CharField(max_length=20, primary_key=True)
    days = models.IntegerField()
    fee = models.IntegerField()
    
    class Meta:
        # sắp xếp theo thứ tự member_id
        ordering = ['term']
        
    def __str__(self):
        return f'{self.term}, {self.days}, {self.fee}'
    
# định nghĩa model Borrow
class Borrow(models.Model):
    # fields
    borrow_id = models.CharField(max_length=8, primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    borrowed_day = models.DateField(auto_now_add=True)
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True)
    return_day = models.DateField(null=True, blank=True)
    status = models.BooleanField()
    
    class Meta:
        # sắp xếp các record theo thứ tự borrow_id
        ordering = ['borrow_id']
        
    # hàm tạo url liên kết đến trang chi tiết biểu mẫu
    def get_absolute_url(self):
        return reverse("borrow-detail", args=[str(self.borrow_id)])
    
    
    def __str__(self):
        return f'{self.borrow_id}, {self.member_id}, {self.borrowed_day}, {self.term}, {self.return_day}, {self.status}'
    
# định nghĩa model Detail
class Detail(models.Model):
    # fields
    borrow_id = models.ForeignKey(Borrow, on_delete=models.SET_NULL, null=True)
    book_id = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    borrowed = models.IntegerField()
    returned = models.IntegerField(null=True, blank=True)
    
    class Meta:
        # sắp xếp các record theo thứ tự borrow_id và book_id
        ordering = ['borrow_id', 'book_id']
        # set borrow_id và book_id là unique
        constraints = [
            models.UniqueConstraint(
                fields=['borrow_id', 'book_id'], name='unique_borrow_id_book_id_combination'
            )
        ]
    
    def __str__(self):
        return f'{self.borrow_id}, {self.book_id}, {self.borrowed}, {self.returned}'