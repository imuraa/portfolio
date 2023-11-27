from django.db import models

# BOOK_CATEGORY_CHOICES = (
#     ("literature_novel", "文学、小説"),
#     ("magazine", "雑誌"),
#     ("comics", "漫画"),
#     ("non-fiction_culture", "ノンフィクション、教養")
#     ("map_travel", "地図、旅行ガイド"),
#     ("hobby_sports_practical", "趣味、スポーツ、実用"),
#     ("housing_living_childcare", "住まい、暮らし、育児"),
#     ("learning_education", "学習、教育"),
#     ("children's-book_picture-book", "児童書、絵本"),
#     ("computer_internet", "コンピュータとネット"),
#     ("natural-science_technology", "自然科学と技術"),
#     ("health_medicine", "健康と医学"),
#     ("art_entertainment", "アート、エンタメ"),
#     ("business_economy", "ビジネス、経済"),
#     ("humanities_society", "人文、社会"),
#     ("ancient-documents", "古書、古文書"),
# )
from django.core.exceptions import ValidationError

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
    isbn = models.CharField(max_length=13,verbose_name="ISBNコード")
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