from django.db import models


# Create your models here.

class CompanyData(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, default='HybridXR')
    company_description = models.TextField(blank=True, null=True)
    contact_title = models.CharField(max_length=100, null=True)
    contact_address = models.CharField(max_length=100, null=True)
    contact_email = models.EmailField(max_length=100, null=True)
    contact_number = models.CharField(max_length=20, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='assets/images', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    isRelated = models.BooleanField(null=False, default=False)

    class Meta:
        ordering = ['-id']
