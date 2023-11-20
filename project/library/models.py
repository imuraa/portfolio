from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=60)
    publisher = models.CharField(max_length=50)
    pub_date = models.DateField()
    image_url = models.URLField()
    price = models.IntegerField()
    purchase_date = models.DateField()
    version = models.IntegerField()
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return '<Book:id=' + str(self.id) + ',' + self.title + '>'