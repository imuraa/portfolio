from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import datetime

def validate_blank_category(value):
    if value == 17:
        raise ValidationError( "カテゴリを選択して下さい" ,params={'value': value})
    
def validate_blank_location(value):
    if value == 6:
        raise ValidationError( "保管場所を選択して下さい" ,params={'value': value})
        

class Category(models.Model):
    class Meta:
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'
    category = models.CharField(max_length=50, verbose_name="カテゴリ")

    def __str__(self):
        return self.category
    

class Location(models.Model):
    class Meta:
        verbose_name = '保管場所'
        verbose_name_plural = '保管場所'
    location = models.CharField(max_length=50,verbose_name="保管場所")

    def __str__(self):
        return self.location

class Book(models.Model):
    class Meta:
        verbose_name = '書籍'
        verbose_name_plural = '書籍'
    isbn = models.CharField(max_length=13,verbose_name="ISBNコード", help_text='13桁の数字（ハイフン抜き）を入力して下さい')
    title = models.CharField(max_length=255,verbose_name="タイトル")
    author = models.CharField(max_length=60,verbose_name="著者")
    publisher = models.CharField(max_length=50,verbose_name="出版社")
    pub_date = models.DateField(verbose_name="出版日")
    image_url = models.URLField(verbose_name="画像リンク", blank=True, null=True)
    price = models.IntegerField(verbose_name="価格")
    purchase_date = models.DateField(verbose_name="購入日")
    version = models.IntegerField(verbose_name="版数")
    category = models.ForeignKey(Category,on_delete=models.PROTECT, default=17, verbose_name="カテゴリ", validators=[validate_blank_category])
    #location = models.CharField(max_length=50,verbose_name="保管場所")
    location = models.ForeignKey(Location, on_delete=models.PROTECT, default=6, verbose_name="保管場所", validators=[validate_blank_location])

    def __str__(self):
        return '<Book:id=' + str(self.id) + ',' + self.title + '>'
    

def validate_past_date(value):
    today = datetime.datetime.today().date()
    if value < today:
        raise ValidationError("過去の日付は入力できません", params={'value': value},)

class Rental(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    start = models.DateField(validators=[validate_past_date])
    end = models.DateField(validators=[validate_past_date])
    return_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return '<Rental:id=' + str(self.id) + '>'