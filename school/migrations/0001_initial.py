# Generated by Django 3.2.9 on 2021-11-19 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Club_title', models.CharField(max_length=2000)),
                ('Club_pub_date', models.DateTimeField(auto_now=True)),
                ('Club_body', models.TextField()),
                ('Club_image', models.ImageField(blank=True, null=True, upload_to='Club_board/')),
                ('Club_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contest_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contest_title', models.CharField(max_length=2000)),
                ('Contest_pub_date', models.DateTimeField(auto_now=True)),
                ('Contest_body', models.TextField()),
                ('Contest_image', models.ImageField(blank=True, null=True, upload_to='Contest_board/')),
                ('Contest_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Free_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Free_title', models.CharField(max_length=2000)),
                ('Free_pub_date', models.DateTimeField(auto_now=True)),
                ('Free_body', models.TextField()),
                ('Free_image', models.ImageField(blank=True, null=True, upload_to='Free_board/')),
                ('Free_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Graduate_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Graduate_title', models.CharField(max_length=2000)),
                ('Graduate_pub_date', models.DateTimeField(auto_now=True)),
                ('Graduate_body', models.TextField()),
                ('Graduate_image', models.ImageField(blank=True, null=True, upload_to='Graduate_board/')),
                ('Graduate_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Market_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Market_title', models.CharField(max_length=2000)),
                ('Market_pub_date', models.DateTimeField(auto_now=True)),
                ('Market_body', models.TextField()),
                ('Market_image', models.ImageField(blank=True, null=True, upload_to='Market_board/')),
                ('Market_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice_title', models.CharField(max_length=2000)),
                ('Notice_pub_date', models.DateTimeField(auto_now=True)),
                ('Notice_body', models.TextField()),
                ('Notice_image', models.ImageField(blank=True, null=True, upload_to='notice/')),
                ('Notice_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sche_pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Study_title', models.CharField(max_length=2000)),
                ('Study_pub_date', models.DateTimeField(auto_now=True)),
                ('Study_body', models.TextField()),
                ('Study_image', models.ImageField(blank=True, null=True, upload_to='Study_board/')),
                ('Study_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Study_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_content', models.CharField(max_length=500)),
                ('study_at', models.DateTimeField(auto_now=True)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.study_board')),
                ('study_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notice_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_content', models.CharField(max_length=500)),
                ('notice_at', models.DateTimeField(auto_now=True)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.notice')),
                ('notice_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Market_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_content', models.CharField(max_length=500)),
                ('market_at', models.DateTimeField(auto_now=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.market_board')),
                ('market_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Graduate_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduate_content', models.CharField(max_length=500)),
                ('graduate_at', models.DateTimeField(auto_now=True)),
                ('graduate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.graduate_board')),
                ('graduate_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Free_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_content', models.CharField(max_length=500)),
                ('free_at', models.DateTimeField(auto_now=True)),
                ('free', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.free_board')),
                ('free_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contest_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_content', models.CharField(max_length=500)),
                ('contest_at', models.DateTimeField(auto_now=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.contest_board')),
                ('contest_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Club_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_content', models.CharField(max_length=500)),
                ('club_at', models.DateTimeField(auto_now=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.club_board')),
                ('club_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
