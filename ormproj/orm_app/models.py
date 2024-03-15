from django.db import models
from django.contrib import admin
# Create your models here.
class Book(models.Model):
    book_id= models.IntegerField(primary_key=True)
    book_name= models.CharField(max_length=50)
    publisher_name= models.CharField(max_length=50)
    author_name= models.CharField(max_length=50)
    publish_year= models.DateField()

class BookAdmin(admin.ModelAdmin):
    list_display= ('book_id','book_name','publisher_name','author_name','publish_year')

