# Generated by Django 4.2.3 on 2023-07-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_catalog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='content',
            field=models.CharField(default='', help_text='Через зяпятую', max_length=300, verbose_name='Габариты'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title',
            field=models.CharField(default='', max_length=300, verbose_name='Заголовок'),
        ),
    ]
