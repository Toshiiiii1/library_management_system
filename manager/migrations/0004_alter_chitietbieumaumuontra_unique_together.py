# Generated by Django 4.2.6 on 2023-10-24 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_chitietbieumaumuontra_ma_bieu_mau_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chitietbieumaumuontra',
            unique_together={('ma_bieu_mau', 'ma_the')},
        ),
    ]
