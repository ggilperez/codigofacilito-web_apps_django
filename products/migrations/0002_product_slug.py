# Generated by Django 2.2.3 on 2021-11-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=False,
        ),
    ]