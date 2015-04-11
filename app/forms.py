from django import forms
from models import Point


class PointsForm(forms.ModelForm):

    class Meta:
        model = Point
        exclude = ('ref_number', )


        widgets = {
            #'email': forms.TextInput(attrs={'class': 'form-control transparent', 'placeholder': 'Email address here..'})
        }
