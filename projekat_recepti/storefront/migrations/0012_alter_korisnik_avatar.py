# Generated by Django 4.0.3 on 2022-04-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0011_alter_korisnik_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korisnik',
            name='avatar',
            field=models.ImageField(upload_to='profile_avatar'),
        ),
    ]
