# Generated by Django 4.1.5 on 2023-10-14 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_registration_copass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='status',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
