from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<str:pk>', views.BookDetail.as_view(), name='books-detail'),
    path('addbook/', views.AddBook.as_view(), name='addbook'),
    path('member/', views.MemberList.as_view(), name='member'),
    path('member/<str:pk>', views.MemberDetail.as_view(), name='member-detail'),
    path('borrow/', views.BorrowList.as_view(), name='borrow'),
    path('borrow/<str:pk>', views.BorrowDetail.as_view(), name='borrow-detail'),
    
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('report/', views.report, name='report'),
]