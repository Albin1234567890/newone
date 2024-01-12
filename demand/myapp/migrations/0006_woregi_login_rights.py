# Generated by Django 4.1.5 on 2023-10-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_login_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='woregi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='rights',
            field=models.IntegerField(default=2),
        ),
    ]