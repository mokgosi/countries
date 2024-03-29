# Generated by Django 4.0.1 on 2022-03-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'Currencies'},
        ),
        migrations.AddField(
            model_name='country',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
