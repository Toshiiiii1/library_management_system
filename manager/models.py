from django.db import models
from django.urls import reverse

# định nghĩa model Book
class Book(models.Model):
    categories = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Thriller', 'Thriller'),
        ('Self-Help', 'Self-Help'),
        ('History', 'History'),
        ('Science', 'Science'),
    ]
    # fields
    title = models.CharField(max_length=50)
    published_year = models.DateField()
    publisher = models.CharField(max_length=50)
    price = models.IntegerField()
    remaining = models.IntegerField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=categories)
    
    class Meta:
        pass
    
    # hàm tạo url liên kết đến trang chi tiết cuốn sách
    def get_absolute_url(self):
        return reverse('books-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.title}, {self.author}'
    
# định nghĩa model Member
class Member(models.Model):
    # fields
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        pass
    
    # hàm tạo url liên kết đến trang chi tiết thành viên
    def get_absolute_url(self):
        return reverse("member-detail", args=[str(self.id)])
    
    def __str__(self):
        return f'{self.name}'
    
# định nghĩa model Borrow
class Borrow(models.Model):
    # fields
    member_id = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    borrowed_day = models.DateField(auto_now_add=True)
    return_day = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        pass
        
    # hàm tạo url liên kết đến trang chi tiết biểu mẫu
    def get_absolute_url(self):
        return reverse("borrow-detail", args=[str(self.id)])
    
    def __str__(self):
        return f'{self.id}, {self.member_id}'
    
# định nghĩa model Detail
class Detail(models.Model):
    # fields
    borrow_id = models.ForeignKey(Borrow, on_delete=models.SET_NULL, null=True)
    book_id = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    borrowed = models.IntegerField()
    returned = models.IntegerField(null=True)
    
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
    
    def get_absolute_url(self):
        return reverse("update-detail", args=[str(self.id)])