# Generated by Django 2.1 on 2019-11-12 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('cat_desc', models.TextField(verbose_name='Category Description')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='uploads/events')),
                ('date_created', models.DateField(default=django.utils.timezone.now, verbose_name='Date Created')),
                ('time_created', models.TimeField(default=django.utils.timezone.now, verbose_name='Time Created')),
            ],
        ),
    ]