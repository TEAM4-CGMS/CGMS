# Generated by Django 3.2 on 2021-04-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='images',
        ),
        migrations.AddField(
            model_name='contact',
            name='orderid',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
