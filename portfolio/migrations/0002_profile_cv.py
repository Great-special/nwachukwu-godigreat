# Generated by Django 4.0.6 on 2022-12-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]