# Generated by Django 4.2.13 on 2024-06-06 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Ad')),
                ('last_name', models.CharField(max_length=30, verbose_name='Soyad')),
                ('father_name', models.CharField(max_length=30, verbose_name='Ata adı')),
                ('age', models.CharField(max_length=3, verbose_name='Yaş')),
                ('city', models.CharField(max_length=30, verbose_name='Şəhər')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('job', models.CharField(max_length=30, verbose_name='İş')),
                ('position', models.CharField(max_length=30, verbose_name='Vəzifə')),
                ('biography', models.TextField(verbose_name='Haqqında məlumat')),
                ('skills', models.TextField(verbose_name='Bacarıqları')),
            ],
        ),
    ]