# Generated by Django 4.1.5 on 2023-12-04 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_entry_gender_entry_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_working_days', models.IntegerField()),
                ('total_amount', models.IntegerField()),
            ],
        ),
    ]
