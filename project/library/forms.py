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

    #image_url = forms.URLField(label='画像URL', required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['purchase_date'].error_messages['invalid']='日付は正しい形式（ハイフン区切り、年月日必須）で入力してください。\n（例:2019-11-25）'
        self.fields['pub_date'].error_messages['invalid'] = '日付は正しい形式（ハイフン区切り、年月日必須）で入力してください。\n（例:2019-11-25）'


#書籍検索フォーム
class SearchForm(forms.Form):
    search = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'タイトル、著者、ISBN'}))


#貸出期間設定フォーム
class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['book_id', 'user_id', 'start', 'end', 'return_date']
        widgets = {
                   'book_id': forms.HiddenInput(),
                   'user_id': forms.HiddenInput(),
                   'start': forms.DateInput(attrs={'class': 'datepicker', 'readonly':'readonly'}),
                   'end': forms.DateInput(attrs={'class': 'datepicker', 'readonly':'readonly'}),
                   'return_date': forms.HiddenInput(),
                  }
            
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")
        book_id = cleaned_data.get("book_id")
        if start and end:
            if start > end:
                raise forms.ValidationError("終了日は開始日より後の日付を設定してください")
            else:
                period = end - start
                period = period.days + 1
                if period > 14:
                    raise forms.ValidationError("最大貸出期間（2週間）を超えています")
                rentals = Rental.objects.filter(book_id=book_id)
                for rental in rentals:
                    if (start >= rental.start and start <= rental.end) or (end >= rental.start and end <= rental.end) or (start < rental.start and end > rental.end):
                        raise forms.ValidationError("設定した貸出期間に予約済みの日付が含まれています")
        return cleaned_data



