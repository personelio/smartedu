from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True) #many-to-one relationships ilişkisi kullanıyoruz.
    slug = models.SlugField(max_length=50, unique=True, null=True)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Kurs Adı", help_text="Kurs Adını Yazınız")
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True, help_text="Kurs Açıklamasını Giriniz")
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default ="courses/pic01.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)


    
    def __str__(self):
        return self.name



# null tabloda ki sutun boş olsa bile hata vermeden devam et. örnek kursun kategorisi yoksa sorun çıkarma