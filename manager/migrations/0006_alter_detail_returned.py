# Generated by Django 4.2.6 on 2023-11-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='returned',
            field=models.IntegerField(default=0),
        ),
    ]