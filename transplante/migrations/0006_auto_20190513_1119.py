# Generated by Django 2.1.7 on 2019-05-13 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transplante', '0005_clinicos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clinicos',
            new_name='Clinico',
        ),
        migrations.RenameModel(
            old_name='Secretarios',
            new_name='Secretario',
        ),
    ]
