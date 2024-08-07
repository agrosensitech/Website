# Generated by Django 5.0.1 on 2024-01-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=50, verbose_name='Common Name')),
                ('scientific_name', models.CharField(max_length=50, verbose_name='Scientific Name')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('description', models.TextField(verbose_name='Description')),
                ('table_data', models.JSONField()),
                ('references', models.TextField(verbose_name='Reference')),
            ],
        ),
    ]
