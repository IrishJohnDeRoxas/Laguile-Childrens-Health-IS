# Generated by Django 5.1 on 2024-09-03 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LCHIS', '0010_alter_gallerymodel_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerymodel',
            name='description',
        ),
    ]
