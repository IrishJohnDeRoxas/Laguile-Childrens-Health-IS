# Generated by Django 5.1 on 2024-09-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LCHIS', '0013_alter_childmodel_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='childmodel',
            name='remarks',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='childmodel',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
