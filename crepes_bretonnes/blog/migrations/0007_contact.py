# Generated by Django 3.0.7 on 2020-07-08 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('adresse', models.TextField()),
                ('photo', models.ImageField(upload_to='photo/')),
            ],
            options={
                'verbose_name': 'contact',
            },
        ),
    ]
