# Generated by Django 5.1.4 on 2024-12-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='GeeksModel',
        ),
    ]
