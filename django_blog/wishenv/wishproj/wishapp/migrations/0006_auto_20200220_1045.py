# Generated by Django 3.0.3 on 2020-02-20 10:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0005_auto_20200220_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitems',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
