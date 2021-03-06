# Generated by Django 2.0.4 on 2018-04-18 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bno', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=40)),
                ('press', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('author', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'borrow',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('cno', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=40)),
                ('type', models.CharField(choices=[('T', 'Teacher'), ('G', 'Graduate'), ('U', 'Undergraduate'), ('O', 'Others')], default='U', max_length=2)),
            ],
            options={
                'db_table': 'card',
            },
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('admin_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=15)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '图书管理员',
                'verbose_name_plural': '图书管理员',
                'db_table': 'Librarian',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AddField(
            model_name='borrow',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mylibrary.Librarian'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='bno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mylibrary.Book'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='cno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.Card'),
        ),
    ]
