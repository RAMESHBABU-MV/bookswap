from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Book, Category

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_creator')

class BookSearchForm(forms.Form):
    search_query = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search books...',
            'class': 'w-full pl-10 pr-4 py-2 bg-gray-100 border-transparent focus:bg-white focus:ring-0 focus:border-primary-500 rounded-lg transition-all duration-200'
        })
    )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover_image',
                 'book_type', 'file', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full pl-10 pr-4 py-3 rounded-xl border-gray-200 dark:border-gray-600 bg-gray-50 dark:bg-gray-700/50 focus:bg-white dark:focus:bg-gray-700 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all outline-none',
                'placeholder': 'e.g. The Great Gatsby'
            }),
            'author': forms.TextInput(attrs={
                'class': 'w-full pl-10 pr-4 py-3 rounded-xl border-gray-200 dark:border-gray-600 bg-gray-50 dark:bg-gray-700/50 focus:bg-white dark:focus:bg-gray-700 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all outline-none',
                'placeholder': 'e.g. F. Scott Fitzgerald'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full p-4 rounded-xl border-gray-200 dark:border-gray-600 bg-gray-50 dark:bg-gray-700/50 focus:bg-white dark:focus:bg-gray-700 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all outline-none resize-none',
                'placeholder': 'Write a brief summary...'
            }),
            'book_type': forms.Select(attrs={
                'class': 'w-full pl-10 pr-4 py-3 rounded-xl border-gray-200 dark:border-gray-600 bg-gray-50 dark:bg-gray-700/50 focus:bg-white dark:focus:bg-gray-700 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all outline-none cursor-pointer appearance-none'
            }),
            'categories': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-checkbox h-4 w-4 text-primary-600 transition duration-150 ease-in-out'
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary-50 file:text-primary-700 hover:file:bg-primary-100 cursor-pointer'
            }),
            'file': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary-50 file:text-primary-700 hover:file:bg-primary-100 cursor-pointer'
            })
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
