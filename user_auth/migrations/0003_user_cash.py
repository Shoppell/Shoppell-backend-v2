# Generated by Django 2.2.28 on 2022-04-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_auto_20220424_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cash',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
