# Generated by Django 3.2.4 on 2021-07-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
