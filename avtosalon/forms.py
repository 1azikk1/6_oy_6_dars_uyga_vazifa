from django import forms
from .models import Brand


class BrandForm(forms.Form):
    brand_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Brend nomini kiriting'
    }), label='Brend nomi')
    brand_country = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Brend davlatini kiriting'
    }), label='Brend davlati')


class CarForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Avtomobil nomini kiriting'
    }), label='Avtomobil nomi')
    color = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Avtomobil rangini kiriting'
    }), label='Avtomobil rangi')
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }), label='Avtomobil rasmi')
    year = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Avtomobil yilini kiriting'
    }), label='Avtomobil yili')
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Avtomobil narxini kiriting'
    }), label='Avtomobil narxi')
    horsepower = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Avtomobil ot-kuchini kiriting'
    }), label='Avtomobil ot-kuchi')
    is_available = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-checkbox-input',
        'placeholder': "Mavjud yoki yo'q",
        'checked': 'checked'
    }), label="Avtomobil mavjud yoki yo'q")
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), label='Avtomobil brendi')
