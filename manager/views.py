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
    template_name = 'books.html'
    
    # xử lý tìm kiếm
    def get_queryset(self):
        # lấy giá trị truy vấn từ form
        search_query = self.request.GET.get('search_query', '')
        # tìm kiếm giá trị đó trong title không phân biệt hoa - thường
        queryset = Book.objects.filter(title__icontains=search_query)
        print(type(self.request.GET))
        return queryset
    
    # truyền nhiều biến đến template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # gửi đến form rỗng cho template sau khi submit, reload trang
        context['search_form'] = SearchForm()
        return context

# view hiển thị chi tiết quyển sách
class BookDetail(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

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
    
def borrow_detail(request, pk):
    borrow = Borrow.objects.get(id=pk)
    detail_list = Detail.objects.filter(borrow_id=borrow.id)
    
    fine = 0
    expire = 0
    flag = 1
    for detail in detail_list:
        if (detail.returned is None):
            flag = 0
            continue
        book_instance = Book.objects.get(id=detail.book_id_id)
        late_days = date.today() - borrow.return_day
        expire = 10000*(late_days.days) if (late_days.days > 0) else 0
        fine += book_instance.price*(detail.borrowed - detail.returned)
    total = fine + expire
    
    if (flag == 1):
        borrow.status = True
        borrow.save()
    
    context = {
        'borrow': borrow,
        'detail_list': detail_list,
        'fine': fine,
        'expire': expire,
        'total': total,
    }
    
    # xac thuc nguoi dung da dang nhap
    if (request.user.is_authenticated):
        return render(request, "borrow_detail.html", context=context)
    else:
        messages.success(request, "You must be login")
        return redirect('home')
    
class AddBorrow(generic.CreateView):
    model = Borrow
    form_class = AddBorrow
    template_name = 'add_borrow.html'
    success_url = reverse_lazy('adddetail')
    
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
    
# view thêm chi tiết
class AddDetail(generic.CreateView):
    model = Detail
    form_class = AddDetailForm
    template_name = 'add_detail.html'
    success_url = reverse_lazy('adddetail')
    
class UpdateDetail(generic.UpdateView):
    model = Detail
    form_class = UpdateDetail
    template_name = 'update_detail.html'
    
    def get_success_url(self):
        return reverse('borrow-detail', args=[str(self.object.borrow_id.id)])
    
class DeleteDetail(generic.DeleteView):
    model = Detail
    template_name = 'delete_detail.html'
    def get_success_url(self):
        return reverse('borrow-detail', args=[str(self.object.borrow_id.id)])