# Generated by Django 3.1.5 on 2021-03-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executive_id', models.CharField(max_length=10, null=True)),
                ('executive_name', models.CharField(max_length=50, null=True)),
                ('executive_email', models.EmailField(max_length=254)),
                ('executive_pass', models.CharField(max_length=32, null=True)),
                ('executive_dep', models.CharField(max_length=100)),
            ],
        ),
    ]
