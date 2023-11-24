from django.db import models

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
    isbn = models.CharField(max_length=13,verbose_name="ISBNコード")
    title = models.CharField(max_length=255,verbose_name="タイトル")
    author = models.CharField(max_length=60,verbose_name="著者")
    publisher = models.CharField(max_length=50,verbose_name="出版社")
    pub_date = models.DateField(verbose_name="出版日")
    image_url = models.URLField(verbose_name="画像リンク")
    price = models.IntegerField(verbose_name="価格")
    purchase_date = models.DateField(verbose_name="購入日")
    version = models.IntegerField(verbose_name="版数")
    category = models.CharField(max_length=50,verbose_name="カテゴリ")
    #location = models.CharField(max_length=50,verbose_name="保管場所")
    location = models.ForeignKey(Location, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return '<Book:id=' + str(self.id) + ',' + self.title + '>'