# Generated by Django 3.0.6 on 2020-08-20 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_reviews_review_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='review_slug',
        ),
    ]
