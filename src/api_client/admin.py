from django.contrib import admin

from api_client.models import Course


@admin.register(Course)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields]
