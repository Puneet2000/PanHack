# Generated by Django 2.0.1 on 2018-08-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='images/'),
        ),
    ]
