# Generated by Django 4.1.5 on 2023-11-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_entry_choose'),
    ]

    operations = [
        migrations.CreateModel(
            name='chosse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
            ],
        ),
    ]