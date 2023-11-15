from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('books/', views.book_list, name='books'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='books-detail'),
    path('addbook/', views.AddBook.as_view(), name='addbook'),
    path('deletebook/<int:pk>', views.DeleteBook.as_view(), name='delete-book'),
    path('updatebook/<int:pk>', views.UpdateBook.as_view(), name='update-book'),
    
    path('member/', views.member_list, name='member'),
    path('member/<int:pk>', views.MemberDetail.as_view(), name='member-detail'),
    path('addmember/', views.AddMember.as_view(), name='addmember'),
    path('deletemember/<int:pk>', views.DeleteMember.as_view(), name='delete-member'),
    path('updatemember/<int:pk>', views.UpdateMember.as_view(), name='update-member'),
    
    path('borrow/', views.borrow_list, name='borrow'),
    path('borrow/<int:pk>', views.borrow_detail, name='borrow-detail'),
    path('addborrow/', views.AddBorrow.as_view(), name='addborrow'),
    path('deleteborrow/<int:pk>', views.DeleteBorrow.as_view(), name='delete-borrow'),
    path('updateborrow/<int:pk>', views.UpdateBorrow.as_view(), name='update-borrow'),
    
    # path('detail/<int:pk>', views.borrow_detail, name='detail'),
    path('adddetail/', views.AddDetail.as_view(), name='adddetail'),
    path('deletedetail/<int:pk>', views.DeleteDetail.as_view(), name='delete-detail'),
    path('updatedetail/<int:pk>', views.UpdateDetail.as_view(), name='update-detail'),
    
    path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    path('register<int:pk>/', views.create_account, name='register'),
]