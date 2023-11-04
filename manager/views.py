from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm
from .models import Book, Author, Member, Borrow
from django.views import generic
from .form import AddAuthor, AddBook, AddCategory, UpdateBook

# view cho trang chủ
def home(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_member = Member.objects.all().count()
    num_visit = request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit + 1

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
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
            login(request, user)
            messages.success(request, "Successful")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form': form})

def add_author(request):
    # nếu người dùng đã đăng nhập
    if (request.user.is_authenticated):
        # request la POST -> thực hiện thêm tác giả
        if (request.method == 'POST'):
            # load form
            form = AddAuthor(request.POST)
            # xác thực form
            if (form.is_valid()):
                form.save()
                messages.success(request, "Successful")
                return redirect('addauthor')
        else:
            form = AddAuthor()
            return render(request, "add_author.html", {"form": form})
    # nếu người dùng chưa đăng nhập
    else:
        messages.success(request, "You must be login")
        return redirect('home')
    
class AddAuthor(generic.CreateView):
    model = Author
    form_class = AddAuthor
    template_name = 'add_author.html'
    
    
def add_category(request):
    # nếu người dùng đã đăng nhập
    if (request.user.is_authenticated):
        # request la POST -> thực hiện thêm thể loại
        if (request.method == 'POST'):
            # load form
            form = AddCategory(request.POST)
            # xác thực form
            if (form.is_valid()):
                form.save()
                messages.success(request, "Successful")
                return redirect('books')
        else:
            form = AddCategory()
            return render(request, "add_category.html", {"form": form})
    # nếu người dùng chưa đăng nhập
    else:
        messages.success(request, "You must be login")
        return redirect('home')

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
    form_class = AddBook
    template_name = 'addbook.html'

# view xóa sách
class DeleteBook(generic.DeleteView):
    model = Book
    
class UpdateBook(generic.UpdateView):
    model = Book
    template_name = "update_book.html"
    form_class = UpdateBook
    
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

def report(request):
    return render(request, 'report.html')