# Generated by Django 4.0.1 on 2022-01-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='title',
            new_name='name',
        ),
    ]
