from django.contrib import admin
from .models import Book, Location, Category, Rental
from .forms import BookAdminForm
import requests
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from io import BytesIO
from PIL import Image
import os
from django.conf import settings
from django.core.files.base import ContentFile
import uuid


class LocationAdmin(admin.ModelAdmin):
    list_display = ["location"]


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
    
    # def save_model(self, request, obj, form, change):
    #     #画像URLを基に画像形式で書影を保存、imageフィールドに登録

    #     #画像URLを取得
    #     image_url = form.cleaned_data['image_url']

    #     #画像を取得
    #     if (image_url):
    #         response = requests.get(image_url)
    #         image_data = BytesIO(response.content)

    #         #画像をPillowで開く
    #         temp_image = Image.open(image_data)

    #         #一時保存する画像のファイル名
    #         temp_filename = "temp_image.png"

    #         # 画像を一時保存
    #         temp_image.save(os.path.join(settings.MEDIA_ROOT, temp_filename))

    #         #ユニークなファイル名を生成 (32文字のUUID)
    #         filename = uuid.uuid4().hex

    #         #imageに画像を登録
    #         with open(os.path.join(settings.MEDIA_ROOT, temp_filename), 'rb') as image_file:
    #             obj.image.save(filename, ContentFile(image_file.read()), save=True)


    #         #一時保存した画像ファイルを削除する
    #         os.remove(os.path.join(settings.MEDIA_ROOT, temp_filename))

    #     #save_model関数をオーバーライドしてデータベースに変更を反映
    #     super(BookAdmin, self).save_model(request, obj, form, change)


class RentalAdmin(admin.ModelAdmin):
    list_display = ["id", "book_id", "user_id", "start", "end", "return_date", "cancel_date"]



admin.site.register(Book, BookAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category)
admin.site.register(Rental, RentalAdmin)
