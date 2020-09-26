# Generated by Django 3.1.1 on 2020-09-24 18:34

from django.db import migrations, models
import django_s3_storage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20200924_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='', storage=django_s3_storage.storage.S3Storage(aws_s3_bucket_name='exchange-2'), upload_to=''),
            preserve_default=False,
        ),
    ]