# Generated by Django 3.1.5 on 2023-02-21 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20230221_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='egitmen_adi',
        ),
    ]
