from django.contrib import admin

# Register your models here.
from .models import Post, CompanyData


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['content']

    class Meta:
        model = Post


class CompanyDataAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = CompanyData


admin.site.register(Post, PostAdmin)
admin.site.register(CompanyData, CompanyDataAdmin)
