# Generated by Django 4.0.5 on 2022-06-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('about', models.TextField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='shop/images/')),
            ],
        ),
    ]
