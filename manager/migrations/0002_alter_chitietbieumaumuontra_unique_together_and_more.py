# Generated by Django 4.2.6 on 2023-10-19 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chitietbieumaumuontra',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='bieumaumuontra',
            name='ma_the',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.thethanhvien'),
        ),
        migrations.AlterField(
            model_name='chitietbieumaumuontra',
            name='ma_bieu_mau',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.bieumaumuontra'),
        ),
        migrations.AlterField(
            model_name='chitietbieumaumuontra',
            name='ma_the',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.thethanhvien'),
        ),
    ]
