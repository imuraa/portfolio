from django import forms
from .models import Book, Location, Rental

#管理画面-保管場所登録フォーム
class LocationAdminForm(forms.ModelForm):

    class Meta:
        model   = Location
        fields  = "__all__"

#管理画面-書籍登録フォーム
class BookAdminForm(forms.ModelForm):

    class Meta:
        model   = Book
        fields  = "__all__"

#書籍検索フォーム
class SearchForm(forms.Form):
    search = forms.CharField(label='', required=False)


#貸出期間設定フォーム
class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['book_id', 'user_id', 'start', 'end', 'return_date']
        widgets = {
                   'book_id': forms.HiddenInput(),
                   'user_id': forms.HiddenInput(),
                   'return_date': forms.HiddenInput(),
                  }



