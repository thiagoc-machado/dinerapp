# Generated by Django 5.0.2 on 2024-02-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentos',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movimentos',
            name='descr',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
