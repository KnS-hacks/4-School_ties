# Generated by Django 3.2.9 on 2021-11-17 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Club_title', models.CharField(max_length=2000)),
                ('Club_author', models.CharField(max_length=50)),
                ('Club_pub_date', models.DateField()),
                ('Club_body', models.TextField()),
                ('Club_image', models.ImageField(blank=True, null=True, upload_to='Graduate_board/')),
            ],
        ),
        migrations.CreateModel(
            name='Contest_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contest_title', models.CharField(max_length=2000)),
                ('Contest_author', models.CharField(max_length=50)),
                ('Contest_pub_date', models.DateField()),
                ('Contest_body', models.TextField()),
                ('Contest_image', models.ImageField(blank=True, null=True, upload_to='Contest_board/')),
            ],
        ),
        migrations.CreateModel(
            name='Free_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Free_title', models.CharField(max_length=2000)),
                ('Free_author', models.CharField(max_length=50)),
                ('Free_pub_date', models.DateField()),
                ('Free_body', models.TextField()),
                ('Free_image', models.ImageField(blank=True, null=True, upload_to='Free_board/')),
            ],
        ),
        migrations.CreateModel(
            name='Graduate_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Graduate_title', models.CharField(max_length=2000)),
                ('Graduate_author', models.CharField(max_length=50)),
                ('Graduate_pub_date', models.DateField()),
                ('Graduate_body', models.TextField()),
                ('Graduate_image', models.ImageField(blank=True, null=True, upload_to='Graduate_board/')),
            ],
        ),
        migrations.CreateModel(
            name='Market_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Market_title', models.CharField(max_length=2000)),
                ('Market_author', models.CharField(max_length=50)),
                ('Market_pub_date', models.DateField()),
                ('Market_body', models.TextField()),
                ('Market_image', models.ImageField(blank=True, null=True, upload_to='Graduate_board/')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice_title', models.CharField(max_length=2000)),
                ('Notice_author', models.CharField(max_length=50)),
                ('Notice_pub_date', models.DateField()),
                ('Notice_body', models.TextField()),
                ('Notice_image', models.ImageField(blank=True, null=True, upload_to='notice/')),
            ],
        ),
        migrations.CreateModel(
            name='Study_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Study_title', models.CharField(max_length=2000)),
                ('Study_author', models.CharField(max_length=50)),
                ('Study_pub_date', models.DateField()),
                ('Study_body', models.TextField()),
                ('Study_image', models.ImageField(blank=True, null=True, upload_to='Study_board/')),
            ],
        ),
    ]
