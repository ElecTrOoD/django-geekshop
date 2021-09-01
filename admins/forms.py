from django import forms
from django.forms import ModelForm

from products.models import Product, ProductCategory
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name')


class ProductAdminForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите название продукта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Введите описание продукта'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите цену продукта'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите количество продуктов'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control', 'title': 'Выберите категорию'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'category', 'image',)


class CategoryAdminForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название категории'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите описание категории'}))
    discount = forms.IntegerField(required=False, min_value=0, max_value=90, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите скидку категории'}))

    class Meta:
        model = Product
        fields = ('name', 'description')
