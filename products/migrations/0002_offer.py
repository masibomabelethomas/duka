# Generated by Django 4.2.1 on 2023-05-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
                ('description', models.CharField(max_length=2300)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
