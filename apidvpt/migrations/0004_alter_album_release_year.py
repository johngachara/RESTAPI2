# Generated by Django 4.2.7 on 2023-11-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apidvpt', '0003_alter_artist_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_year',
            field=models.DateField(),
        ),
    ]
