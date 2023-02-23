# Generated by Django 3.1.5 on 2023-02-23 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kurs Adını Yazınız', max_length=200, unique=True, verbose_name='Kurs Adı')),
                ('description', models.TextField(blank=True, help_text='Kurs Açıklamasını Giriniz', null=True)),
                ('image', models.ImageField(default='courses/pic01.jpg', upload_to='courses/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.category')),
            ],
        ),
    ]
