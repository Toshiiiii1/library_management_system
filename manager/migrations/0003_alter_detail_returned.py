# Generated by Django 4.2.6 on 2023-11-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_book_category_alter_borrow_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='returned',
            field=models.IntegerField(null=True),
        ),
    ]