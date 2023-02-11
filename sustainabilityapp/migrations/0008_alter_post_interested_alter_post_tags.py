# Generated by Django 4.1.6 on 2023-02-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustainabilityapp', '0007_alter_post_interested_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='interested',
            field=models.ManyToManyField(blank=True, related_name='interested', to='sustainabilityapp.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='sustainabilityapp.tags'),
        ),
    ]
