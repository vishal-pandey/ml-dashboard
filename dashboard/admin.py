from django.contrib import admin
from dashboard.models import Dataset


class DatasetAdmin(admin.ModelAdmin):
	model = Dataset
	list_display = ['id', 'user', 'dataset', 'name', 'size']

# Register your models here.

admin.site.register(Dataset, DatasetAdmin)