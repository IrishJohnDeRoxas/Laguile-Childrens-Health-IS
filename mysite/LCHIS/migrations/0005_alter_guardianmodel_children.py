# Generated by Django 5.1 on 2024-08-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LCHIS', '0004_guardianmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardianmodel',
            name='children',
            field=models.ManyToManyField(null=True, to='LCHIS.childmodel'),
        ),
    ]
