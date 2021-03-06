# Generated by Django 2.2.12 on 2021-03-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('quetionstype', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=400)),
                ('images', models.ImageField(upload_to='images')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
