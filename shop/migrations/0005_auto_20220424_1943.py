# Generated by Django 2.2.28 on 2022-04-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20220424_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
