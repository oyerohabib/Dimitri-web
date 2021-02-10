from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

@admin.register(Driver)
class MemberAdminDriver(ImportExportModelAdmin):
	list_display = ("Name", "Status", "EVR", "Notes", "License", "License_State")
	pass

@admin.register(Equipment)
class MemberAdminEquipment(ImportExportModelAdmin):
	list_display = ("IFTA", "Truck", "Status", "Year", "Make", "Model")
	pass