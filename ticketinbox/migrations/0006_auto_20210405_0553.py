# Generated by Django 2.2.12 on 2021-04-05 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0005_auto_20210403_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='solution',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_rating',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 5, 5, 53, 32, 107004), null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 5, 5, 53, 32, 107168), null=True),
        ),
    ]