# Generated by Django 2.2.12 on 2021-04-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_remove_executive_ticket_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='executive_username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
