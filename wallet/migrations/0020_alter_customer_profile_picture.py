# Generated by Django 4.1 on 2022-09-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0019_card_delete_cards_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
