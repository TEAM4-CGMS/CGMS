# Generated by Django 2.2.12 on 2021-04-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0014_auto_20210407_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
