# Generated by Django 2.2.12 on 2021-03-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reportsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('date', models.CharField(max_length=20)),
                ('response', models.CharField(max_length=20)),
                ('resolve', models.CharField(max_length=20)),
            ],
        ),
    ]