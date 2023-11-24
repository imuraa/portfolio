from django import forms
from .models import Book, Location

class LocationAdminForm(forms.ModelForm):

    class Meta:
        model   = Location
        fields  = "__all__"


class BookAdminForm(forms.ModelForm):

    class Meta:
        model   = Book
        fields  = "__all__"

