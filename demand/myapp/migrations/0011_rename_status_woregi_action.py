# Generated by Django 4.1.5 on 2023-10-17 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_entry_status_woregi_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='woregi',
            old_name='status',
            new_name='action',
        ),
    ]