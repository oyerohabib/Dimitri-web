from import_export import resources
from .models import Driver, Equipment

class DriverResources(resources.ModelResource):
	class Meta:
		model = Driver

class EquipmentResources(resources.ModelResource):
	class Meta:
		model = Equipment