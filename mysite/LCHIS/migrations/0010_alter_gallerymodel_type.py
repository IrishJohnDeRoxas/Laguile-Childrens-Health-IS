# Generated by Django 5.1 on 2024-09-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LCHIS', '0009_alter_gallerymodel_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerymodel',
            name='type',
            field=models.CharField(choices=[('health-center', 'Health Center'), ('barangay-hall', 'Barangay Hall'), ('school', 'School'), ('basketball-court', 'Basketball Court'), ('church', 'Church'), ('other', 'Other')], max_length=200, null=True),
        ),
    ]
