# Generated by Django 4.2.3 on 2023-07-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_catalogsizes_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='content',
            field=models.CharField(default='', max_length=300, unique=True, verbose_name='Габариты'),
        ),
        migrations.DeleteModel(
            name='CatalogSizes',
        ),
    ]
