# Generated by Django 3.2.7 on 2021-09-28 05:40

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', tinymce.models.HTMLField()),
                ('blog_publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='BlogImages')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=80)),
                ('job_description', tinymce.models.HTMLField()),
                ('job_experience', models.CharField(blank=True, max_length=80, null=True)),
                ('job_publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=200)),
                ('Qualification', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('job_type', models.CharField(default='Full Time', max_length=80)),
                ('No_of_openings', models.CharField(default='1', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to='CourseImages')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=80)),
                ('Email', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='CareerResume')),
                ('Apply_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
    ]