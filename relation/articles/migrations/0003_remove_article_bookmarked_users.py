# Generated by Django 4.2 on 2024-03-19 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_bookmarked_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='bookmarked_users',
        ),
    ]
