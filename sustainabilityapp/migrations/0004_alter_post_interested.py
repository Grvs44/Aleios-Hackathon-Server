# Generated by Django 4.1.6 on 2023-02-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustainabilityapp', '0003_image_post_remove_eventpost_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='interested',
            field=models.ManyToManyField(related_name='interested', to='sustainabilityapp.profile'),
        ),
    ]