# Generated by Django 5.1.1 on 2024-10-23 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
