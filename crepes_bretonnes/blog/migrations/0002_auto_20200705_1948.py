# Generated by Django 3.0.7 on 2020-07-05 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Arcticle',
            new_name='Article',
        ),
    ]
