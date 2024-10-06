from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
    Title = models.CharField(max_length=100)
    Book_Count = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    author = models.CharField(null=True,max_length=100)
    slug = models.SlugField(default="", blank=True, editable= False,null=False)#added this code for this tyhpe of urls Shashank-The-fucking-Legend
# when we open index def links we have declare def which is save
# blank = True we have added this code just because we are getting restriction in panel 
# while adding new book in admin portal after adding this in slug RR will not come.
# editable = False means slug column will not reflect anymore on the panel.
        
    def get_absolute_url(self):
        return reverse("Book", args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug = slugify(self.Title)
        super().save(*args,**kwargs)
        
    def __str__(self):
        return f"{self.Title} ({self.Book_Count})"