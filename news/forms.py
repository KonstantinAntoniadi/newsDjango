from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'fullt_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of article'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of article'
            }),
            "fullt_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of article'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-con  trol',
                'placeholder': 'Date of publication'
            })
        }