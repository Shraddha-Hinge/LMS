# Generated by Django 5.1.4 on 2024-12-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0002_addstudent_delete_geeksmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstudent',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
