# Generated by Django 4.1.5 on 2023-10-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_entry_select'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='choose',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]