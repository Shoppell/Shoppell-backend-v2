# Generated by Django 2.2.28 on 2022-05-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20220520_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]
