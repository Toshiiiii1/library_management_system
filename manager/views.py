from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from .form import SignUpForm
from .models import *
from django.views import generic
from .form import *

# view cho trang chủ
def home(request):
    num_books = Book.objects.all().count()
    num_member = Member.objects.all().count()
    num_visit = request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit + 1

    context = {
        'num_books': num_books,
        'num_members': num_member,
        'num_visits': num_visit,
    }
    
    # người dùng thực hiện đăng nhập
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        
        # xác thực username và password
        user = authenticate(request, username=username, password = password)
        if (user is not None):
            # nếu người dùng là admin
            if (user.is_staff):
                login(request, user)
                messages.success(request, "Successful")
                # chuyển hướng đến trang "home"
                return redirect('home')
            # nếu người dùng ko là admin
            else:
                login(request, user)
                messages.success(request, "Successful")
                return render(request, 'temp.html') # chuyển hướng người dùng
        else:
            messages.error(request, "Fail")
            return redirect('home')
    # người dùng đã đăng nhập
    else:
        return render(request, "home.html", context=context)

# view đăng xuất
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

# view đăng ký
def register_user(request):
    # nếu người dùng ấn "Register"
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "Successful")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form': form})

# view liệt kê danh sách các quyển sách
class BookList(generic.ListView):
    model = Book
    # đặt tên biến để book_list để chứa danh sách các sách
    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'books.html'

# view hiển thị chi tiết quyển sách
class BookDetail(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    # giới hạn 10 phần tử vào 1 trang hiển thị
    paginate_by = 10

# view thêm sách
class AddBook(generic.CreateView):
    model = Book
    # sử dụng form AddBook
    form_class = AddBookForm
    template_name = 'addbook.html'
    
# view xóa sách
class DeleteBook(generic.DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('books')
    
# view cập nhật sách
class UpdateBook(generic.UpdateView):
    model = Book
    form_class = UpdateBookForm
    template_name = 'update_book.html'
    success_url = reverse_lazy('books')

# view liệt kê danh sách các thành viên
class MemberList(generic.ListView):
    model = Member
    context_object_name = 'member_list'
    queryset = Member.objects.all()
    template_name = 'member.html'

# view hiển thị chi tiết thành viên
class MemberDetail(generic.DetailView):
    model = Member
    template_name = 'member_detail.html'
    paginate_by = 10
    
class BorrowList(generic.ListView):
    model = Borrow
    context_object_name = 'borrow_list'
    queryset = Borrow.objects.all()
    template_name = 'borrow.html'
    
class BorrowDetail(generic.DetailView):
    model = Borrow
    template_name = 'borrow_detail.html'
    paginate_by = 10