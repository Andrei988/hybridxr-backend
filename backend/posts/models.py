from django.db import models


# Create your models here.

class CompanyData(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.TextField(blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    contact_title = models.TextField(blank=True, null=True)
    contact_address = models.TextField(blank=True, null=True)
    contact_address_array = models.TextField(blank=True, null=True)
    contact_email = models.TextField(blank=True, null=True)
    contact_number = models.TextField(blank=True, null=True)
    footer_title = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-id']


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='media/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    isRelated = models.BooleanField(null=False, default=False)

    class Meta:
        ordering = ['-id']
