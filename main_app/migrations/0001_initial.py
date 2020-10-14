<<<<<<< HEAD
# Generated by Django 3.1 on 2020-10-02 02:50
=======
# Generated by Django 3.1 on 2020-10-03 01:32
>>>>>>> d27f02ac8edd00d03b4e519c519f639c59d06477

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_s3_storage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=1000)),
                ('avatar', models.CharField(blank=True, max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('tag', models.CharField(choices=[('A', 'Animals'), ('B', 'Books'), ('C', 'Clothes'), ('E', 'Electronics'), ('F', 'Furniture'), ('H', 'Household Goods'), ('J', 'Jewelry'), ('M', 'Makeup'), ('S', 'Sports'), ('V', 'Vehicles')], default='A', max_length=1)),
                ('photo', models.ImageField(upload_to=django_s3_storage.storage.S3Storage(aws_s3_bucket_name='exchange-2'))),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('exp_date', models.DateField(default='2020-11-01')),
=======
                ('exp_date', models.DateField(default='2020-11-02')),
>>>>>>> d27f02ac8edd00d03b4e519c519f639c59d06477
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.post')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ManyToManyField(to='main_app.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]