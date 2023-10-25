# Generated by Django 4.2.6 on 2023-10-25 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['author_id'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('published_year', models.DateField()),
                ('publisher', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('remaining', models.IntegerField()),
                ('author', models.ManyToManyField(to='manager.author')),
            ],
            options={
                'ordering': ['book_id'],
            },
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('borrow_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('borrowed_day', models.DateField(auto_now_add=True)),
                ('return_day', models.DateField()),
                ('status', models.BooleanField()),
            ],
            options={
                'ordering': ['borrow_id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['cate_id'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['member_id'],
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('term', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('days', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
            options={
                'ordering': ['term'],
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed', models.IntegerField()),
                ('returned', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manager.book')),
                ('borrow_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manager.borrow')),
            ],
            options={
                'ordering': ['borrow_id', 'book_id'],
            },
        ),
        migrations.AddField(
            model_name='borrow',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manager.member'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manager.term'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='manager.category'),
        ),
        migrations.AddConstraint(
            model_name='detail',
            constraint=models.UniqueConstraint(fields=('borrow_id', 'book_id'), name='unique_borrow_id_book_id_combination'),
        ),
    ]
