# Generated by Django 5.1 on 2024-10-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LCHIS', '0043_vitaminmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_main', models.BooleanField(default=False)),
            ],
        ),
    ]