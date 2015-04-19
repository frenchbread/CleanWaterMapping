from django import forms
from models import Point
from random import randint


class PointsForm(forms.ModelForm):

    class Meta:
        model = Point

        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Title'}),
            'Description': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Description'}),
            'Address': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Address'}),
            'Latitude': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Latitude'}),
            'Longitude': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Longitude'}),
            'Arsenic': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Arsenic'}),
            'Barium': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Barium'}),
            'Boron': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Boron'}),
            'Chromium': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Chromium'}),
            'Fluoride': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Fluoride'}),
            'Selenium': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Selenium'}),
            'Uranium': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Uranium'}),
            'ref_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference number', 'value': str(randint(1000000000, 9999999999))}),
        }
