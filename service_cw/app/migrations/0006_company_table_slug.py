# Generated by Django 4.0.5 on 2022-07-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_offers_table_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_table',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]