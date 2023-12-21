from django.contrib import admin
from .models import Book, Location, Category, Rental
from .forms import BookAdminForm, LocationAdminForm
import requests
from django.utils.safestring import mark_safe
from django.templatetags.static import static
#from django.http import HttpResponse

class LocationAdmin(admin.ModelAdmin):
    list_display = ["location"]


class BookAdmin(admin.ModelAdmin):
    change_form_template = 'library/admin/change_form.html'
    form = BookAdminForm
    list_display = ["thumbnail_preview", "title", "author", "publisher", "pub_date", "price", "category", "version", "purchase_date", "location"]
    list_display_links = ("thumbnail_preview", "title")
    #fields = ["isbn","title","author","publisher", "pub_date", "image_url", "price", "category", "version", "purchase_date", "location"]

    fieldsets = (
        ("自動入力", {"fields": ("isbn","title","author","publisher", "pub_date", "image_url", "price")}),
        ("手動入力", {"fields": ("category", "version", "purchase_date", "location")}),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if (db_field.name == 'category') or (db_field.name == 'location'):
            kwargs['empty_label'] = '----------'  # 未選択の場合の表示文字列
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    def thumbnail_preview(self, obj):
        no_image_path = 'library/images/no_image.jpg'
        no_image_url = static(no_image_path)
        if obj.image_url:
            return mark_safe('<img src="{}" style="width:50px; height:75px;">'.format(obj.image_url))
        else:
            return mark_safe(f'<img src="{no_image_url}" style="width:50px; height:75px;">')

    thumbnail_preview.short_description = '画像'

    def add_view(self, request, form_url="", extra_context=None):
        if request.method == "POST" and "get_info_btn" in request.POST:
            isbn = str(request.POST["isbn"])
            result  = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn)
            data = result.json()
            #BookAdmin.initial_dict["title"] = data["items"][0]["volumeInfo"]["title"]
            return super().add_view(request, form_url, extra_context=extra_context)
        else:
            return self.changeform_view(request, None, form_url, extra_context)
    
    def change_view(self, request, object_id, form_url="", extra_context=None):
        return self.changeform_view(request, object_id, form_url, extra_context)
    
class RentalAdmin(admin.ModelAdmin):
    list_display = ["id", "book_id", "user_id", "start", "end", "return_date", "cancel_date"]



admin.site.register(Book, BookAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category)
admin.site.register(Rental, RentalAdmin)
