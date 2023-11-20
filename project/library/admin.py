from django.contrib import admin
from .models import Book
from .forms import BookAdminForm
import requests
from django.http import HttpResponse #テスト

class BookAdmin(admin.ModelAdmin):
    change_form_template = 'library/admin/change_form.html'
    form = BookAdminForm
    list_display = ["title", "author", "publisher", "pub_date", "category", "location"]

    def add_view(self, request, form_url="", extra_context=None):
        if request.method == "POST" and "get_info_btn" in request.POST:
            isbn = str(request.POST["isbn"])
            result  = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn)
            data = result.json()
            title = data["items"][0]["volumeInfo"]["title"]
            return HttpResponse("書籍情報取得ボタンが押されました<br>" + "取得した書籍名：" + title)
        else:
            return self.changeform_view(request, None, form_url, extra_context)
    
    def change_view(self, request, object_id, form_url="", extra_context=None):
        return self.changeform_view(request, object_id, form_url, extra_context)



admin.site.register(Book, BookAdmin)
