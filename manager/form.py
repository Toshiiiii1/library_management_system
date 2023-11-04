from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# form đăng ký
class SignUpForm(UserCreationForm):
    # UserCreationForm mặc định các trường: username, password1 va password2
    # Định nghĩa thêm các trường: email, first_name, last_name cho form đăng ký
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email Address"
        }
    ))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "First Name"
        }
    ))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        }
    ))
    
    class Meta:
        model = User # định nghĩa model áp dụng form
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    
    # override phương thức __init__ cua lop UserCreationForm để customize 3 trường mặc định
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# form thêm sách
class AddBookForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Title',
                'class':'form-control'
            }
        )
    )
    
    published_year = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(
            attrs={
                'placeholder':'Published year',
                'class':'form-control'
            }
        )
    )
    
    publisher = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Publisher',
                'class':'form-control'
            }
        )
    )
    
    price = forms.IntegerField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                'placeholder':'Price',
                'class':'form-control'
            }
        )
    )
    
    remaining = forms.IntegerField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                'placeholder':'Remaining',
                'class':'form-control'
            }
        )
    )
    
    author = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Author',
                'class':'form-control'
            }
        )
    )
    
    categories = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Thriller', 'Thriller'),
        ('Self-Help', 'Self-Help'),
        ('History', 'History'),
        ('Science', 'Science'),
    ]
    
    category = forms.ChoiceField(
        choices=categories,
        widget=forms.widgets.Select(
            attrs={
                'class':'form-control'
            }
        )
    )
    
    class Meta:
        model = Book # định nghĩa model áp dụng form
        exclude = ("temp",)
        
class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("temp",)
        
    def __init__(self, *args, **kwargs):
        super(UpdateBookForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['published_year'].widget.attrs['class'] = 'form-control'
        self.fields['publisher'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['remaining'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        