from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Kurs Adı", help_text="Kurs Adını Yazınız")
    description = models.TextField(blank=True, null=True, help_text="Kurs Açıklamasını Giriniz")
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default ="courses/pic01.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
   # egitmen_adi = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name