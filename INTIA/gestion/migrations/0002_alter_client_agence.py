# Generated by Django 5.1.6 on 2025-04-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='agence',
            field=models.CharField(max_length=100),
        ),
    ]
