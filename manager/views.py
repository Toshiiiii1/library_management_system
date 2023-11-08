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
    
    def get_success_url(self):
        return reverse('books-detail', args=[str(self.object.pk)])

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

# view thêm thành viên
class AddMember(generic.CreateView):
    model = Member
    # sử dụng form AddMember
    form_class = AddMemberForm
    template_name = 'addmember.html'
    
# view xóa thành viên
class DeleteMember(generic.DeleteView):
    model = Member
    template_name = 'delete_member.html'
    success_url = reverse_lazy('member')
    
# view cập nhật thành viên
class UpdateMember(generic.UpdateView):
    model = Member
    form_class = UpdateMemberForm
    template_name = 'update_member.html'
    
    def get_success_url(self):
        return reverse('member-detail', args=[str(self.object.pk)])
    
class BorrowList(generic.ListView):
    model = Borrow
    context_object_name = 'borrow_list'
    queryset = Borrow.objects.all()
    template_name = 'borrow.html'
    
class BorrowDetail(generic.DetailView):
    model = Borrow
    template_name = 'borrow_detail.html'
    paginate_by = 10
    
def borrow_detail(request, pk):
    borrow = Borrow.objects.get(id=pk)
    detail_list = Detail.objects.all()
    
    context = {
        'borrow': borrow,
        'detail_list': detail_list
    }
    
    # xac thuc nguoi dung da dang nhap
    if (request.user.is_authenticated):
        return render(request, "borrow_detail.html", {'context': context})
    else:
        messages.success(request, "You must be login")
        return redirect('home')
    
class AddBorrow(generic.CreateView):
    model = Borrow
    form_class = AddBorrow
    template_name = 'add_borrow.html'
    
# view xóa mượn - trả
class DeleteBorrow(generic.DeleteView):
    model = Borrow
    template_name = 'delete_borrow.html'
    success_url = reverse_lazy('borrow')
    
# view cập nhật mượn - trả
class UpdateBorrow(generic.UpdateView):
    model = Borrow
    form_class = UpdateBorrowForm
    template_name = 'update_borrow.html'
    
    def get_success_url(self):
        return reverse('borrow-detail', args=[str(self.object.pk)])