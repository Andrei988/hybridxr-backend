# Generated by Django 3.1.3 on 2020-11-20 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20201120_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydata',
            name='contact_address_array',
        ),
    ]