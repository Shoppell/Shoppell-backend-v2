# Generated by Django 3.2.12 on 2022-05-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='payment_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]