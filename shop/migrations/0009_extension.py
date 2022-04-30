from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0008_auto_20220430_1450'),
    ]

    operations = [
        TrigramExtension(),
    ]