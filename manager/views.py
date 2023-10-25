from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm

def home(request):
    if (request.method == 'POST'):
        # lay username va password tu nguoi dung
        username = request.POST['username']
        password = request.POST['password']
        
        # xac thuc nguoi dung
        user = authenticate(request, username=username, password = password)
        # xac thuc thanh cong -> dang nhap va hien thi thong bao dang nhap thanh cong
        if (user is not None):
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('dashboard')
        # xac thuc that bai -> hien thi thong bao dang nhap that bai
        else:
            messages.error(request, "Fail")
            return redirect('home')
    else:
        # quay ve trang chinh
        return render(request, "home.html")
    
# tao view cho hanh dong dang xuat o template navbar.html
def logout_user(request):
    # thuc hien dang xuat va hien thi thong bao
    logout(request)
    messages.success(request, "You have been logged out")
    # quay ve trang chinh
    return redirect('home')

# tao view cho hanh dong dang ki o template register.html 
def register_user(request):
    # request la POST -> thuc hien dang ky
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        # xac thuc form
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # xac thuc nguoi dung
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successful")
            return redirect('home')
    # request la cac phuong thuc HTTP con lai -> load trang dang ky
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form': form})
    
    # neu form khong chinh xac thi load lai trang dang ky
    return render(request, "register.html", {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def books(request):
    return render(request, 'books.html')

def borrow(request):
    return render(request, 'borrow.html')

def report(request):
    return render(request, 'report.html')