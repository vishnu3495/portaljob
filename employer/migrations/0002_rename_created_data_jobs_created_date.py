# Generated by Django 4.0.4 on 2022-06-17 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='created_data',
            new_name='created_date',
        ),
    ]
