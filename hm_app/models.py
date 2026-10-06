from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    author = models.CharField(max_length=100, verbose_name="Автор")
    year = models.IntegerField(verbose_name="Рік видання")
    genre = models.CharField(max_length=50, verbose_name="Жанр")
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Ціна"
    )

    def __str__(self):
        return f"{self.title} — {self.author}"