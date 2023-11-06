from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='books-detail'),
    path('addbook/', views.AddBook.as_view(), name='addbook'),
    path('deletebook/<int:pk>', views.DeleteBook.as_view(), name='delete-book'),
    path('updatebook/<int:pk>', views.UpdateBook.as_view(), name='update-book'),
    
    path('member/', views.MemberList.as_view(), name='member'),
    path('member/<int:pk>', views.MemberDetail.as_view(), name='member-detail'),
    
    path('borrow/', views.BorrowList.as_view(), name='borrow'),
    path('borrow/<int:pk>', views.borrow_detail, name='borrow-detail'),
    path('addborrow/', views.AddBorrow.as_view(), name='addborrow'),
    path('deleteborrow/<int:pk>', views.DeleteBorrow.as_view(), name='delete-borrow'),
    path('updateborrow/<int:pk>', views.UpdateBorrow.as_view(), name='update-borrow'),
    
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]