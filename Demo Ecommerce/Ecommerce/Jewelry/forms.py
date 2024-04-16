from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price','color','purity','weight', 'thumnail_image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'purity': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'weight': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'thumnail_image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class  EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price','color','purity','weight', 'thumnail_image', 'is_sold')
        widgets = {
            'thumnail_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'purity': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'weight': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

