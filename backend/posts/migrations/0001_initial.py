# Generated by Django 3.1.3 on 2020-11-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.TextField(blank=True, null=True)),
                ('company_description', models.TextField(blank=True, null=True)),
                ('contact_title', models.TextField(blank=True, null=True)),
                ('contact_address', models.TextField(blank=True, null=True)),
                ('contact_address_array', models.TextField(blank=True, null=True)),
                ('contact_email', models.TextField(blank=True, null=True)),
                ('contact_number', models.TextField(blank=True, null=True)),
                ('footer_title', models.TextField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='media/')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('isRelated', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
