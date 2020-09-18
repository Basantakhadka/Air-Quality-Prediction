from django.contrib import admin

# Register your models here.
from .models import Dataset,Dataset1,Dataset2,Dataset3,whole_dataset
from import_export.admin import ImportExportModelAdmin

@admin.register(Dataset,Dataset1,Dataset2,Dataset3,whole_dataset)
class ViewAdmin( ImportExportModelAdmin):
	pass