# Generated by Django 5.1 on 2024-09-29 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LCHIS', '0024_rename_children_guardianmodel_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardianmodel',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LCHIS.childmodel'),
        ),
    ]