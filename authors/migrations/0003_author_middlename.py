# Generated by Django 3.2 on 2021-08-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_rename_authors_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='middlename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
