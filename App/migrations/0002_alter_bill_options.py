# Generated by Django 4.2.3 on 2023-07-10 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'ordering': ['-date']},
        ),
    ]
