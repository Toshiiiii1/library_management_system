from django.db import models
from django.urls import reverse

# define Author model
class Author(models.Model):
    # fields
    author_id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    
    # define metadata
    class Meta:
        # order by author_id
        ordering = ['author_id']
    
    def __str__(self):
        return f'{self.author_id}, {self.name}'
    
# define Category model
class Category(models.Model):
    # fields
    cate_id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    
    # define metadata
    class Meta:
        # order by cate_id
        ordering = ['cate_id']
    
    def __str__(self):
        return f'{self.cate_id}, {self.name}'

# define Book model
class Book(models.Model):
    # fields
    book_id = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=50)
    published_year = models.DateField()
    publisher = models.CharField(max_length=50)
    price = models.IntegerField()
    remaining = models.IntegerField()
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    
    class Meta:
        # sắp xếp record theo thứ tự book_id
        ordering = ['book_id']
        
    # hàm lấy danh sách thể loại của cuốn sách
    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])
    
    # hàm lấy danh sách tác giả của cuốn sách
    def display_author(self):
        return ', '.join(author.name for author in self.author.all()[:3])
    
    # hàm tạo url liên kết đến trang chi tiết cuốn sách
    def get_absolute_url(self):
        return reverse('books-detail', args=[str(self.book_id)])

    # định nghĩa tên cột khi hiển thị trên trang admin
    display_category.short_description = 'Categories'
    display_author.short_description = 'Authors'
    
    def __str__(self):
        return f'{self.book_id}, {self.title}, {self.published_year}, {self.publisher}, {self.price}, {self.remaining}, {self.author}, {self.category}'
    
# define Member model
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
        
    def get_absolute_url(self):
        return reverse("member-detail", args=[str(self.member_id)])
    
    def __str__(self):
        return f'{self.member_id}, {self.name}, {self.address}, {self.phone_num}, {self.created_at}'
    
# define Term model
class Term(models.Model):
    term = models.CharField(max_length=20, primary_key=True)
    days = models.IntegerField()
    fee = models.IntegerField()
    
    # order by term
    class Meta:
        ordering = ['term']
        
    def __str__(self):
        return f'{self.term}, {self.days}, {self.fee}'
    
# define Borrow model
class Borrow(models.Model):
    # fields
    borrow_id = models.CharField(max_length=8, primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    borrowed_day = models.DateField(auto_now_add=True)
    term = models.ForeignKey(Term, on_delete=models.DO_NOTHING)
    return_day = models.DateField(null=True, blank=True)
    status = models.BooleanField()
    
    class Meta:
        # sắp xếp các record theo thứ tự borrow_id
        ordering = ['borrow_id']
        
    def get_absolute_url(self):
        return reverse("borrow-detail", args=[str(self.borrow_id)])
    
    
    def __str__(self):
        return f'{self.borrow_id}, {self.member_id}, {self.borrowed_day}, {self.term}, {self.return_day},  {self.status}'
    
# define Detail model
class Detail(models.Model):
    # fields
    borrow_id = models.ForeignKey(Borrow, on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    borrowed = models.IntegerField()
    returned = models.IntegerField()
    
    # define metadata
    class Meta:
        ordering = ['borrow_id', 'book_id']
        # set borrow_id and book_id are unique
        constraints = [
            models.UniqueConstraint(
                fields=['borrow_id', 'book_id'], name='unique_borrow_id_book_id_combination'
            )
        ]
        # unique_together = [['borrow_id', 'book_id']]
    
    def __str__(self):
        return f'{self.borrow_id}, {self.book_id}, {self.borrowed}, {self.returned}'