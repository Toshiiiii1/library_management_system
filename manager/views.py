from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm
from .models import Book, Author, Member, Borrow
from django.views import generic
from .form import AddBook

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
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password = password)
        if (user is not None):
            if (user.is_staff):
                login(request, user)
                messages.success(request, "You have been logged in")
                return redirect('home')
            else:
                login(request, user)
                messages.success(request, "You have been logged in")
                return render(request, 'temp.html')
        else:
            messages.error(request, "Fail")
            return redirect('home')
    else:
        return render(request, "home.html", context=context)

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
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
    
    return render(request, "register.html", {'form': form})

class BookList(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'books.html'
    
class BookDetail(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    paginate_by = 10
    
class AddBook(generic.CreateView):
    model = Book
    form_class = AddBook
    template_name = 'addbook.html'

class MemberList(generic.ListView):
    model = Member
    context_object_name = 'member_list'
    queryset = Member.objects.all()
    template_name = 'member.html'
    
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