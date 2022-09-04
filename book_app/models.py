
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length =100)
    code = models.CharField(max_length=3)
    def full_country(self):
            return f'{self.name} {self.code}'


    def __str__(self):
        return self.full_country()
    class Meta:
        verbose_name_plural = ' publishing countries'




class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


    def full_address(self):
        return f'{self.street} {self.city}'


    def __str__(self):
        return self.full_address()
    class Meta:
        verbose_name_plural = 'author addresses'
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def __str__(self):
        return self.full_name()

class BOOK(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling =  models.BooleanField(default=False)
    slug  = models.SlugField(default='', blank=True,  null=False, db_index=True)
    country = models.ManyToManyField(Country)


    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
