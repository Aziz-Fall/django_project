# Generated by Django 3.0.7 on 2020-07-05 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200705_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
    ]
