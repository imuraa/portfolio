from django.contrib import admin
from .models import Book, Location, Category, Rental
from .forms import BookAdminForm
from django.utils.safestring import mark_safe
from django.templatetags.static import static


#保管場所管理画面
class LocationAdmin(admin.ModelAdmin):
    list_display = ["location"]

#書籍管理画面
class BookAdmin(admin.ModelAdmin):
    change_form_template = 'library/admin/change_form.html'
    form = BookAdminForm
    list_display = ["thumbnail_preview", "title", "author", "publisher", "pub_date", "price", "category", "version", "purchase_date", "location"]
    list_display_links = ("thumbnail_preview", "title",)
    list_per_page = 10


    fieldsets = (
        ("自動入力", {"fields": ("isbn", "title", "author", "publisher", "pub_date", "image_url", "price")}),
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


#貸出予約管理画面
class RentalAdmin(admin.ModelAdmin):
    list_display = ["id", "book_id", "user_id", "start", "end", "return_date", "cancel_date"]


admin.site.register(Book, BookAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category)
admin.site.register(Rental, RentalAdmin)
