# Generated by Django 3.2.5 on 2021-08-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
