# Generated by Django 4.2.7 on 2024-01-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_description_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url3',
            field=models.URLField(blank=True),
        ),
    ]
