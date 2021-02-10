from django.urls import path
from . import views

urlpatterns = [
	path('', views.Landing_Page, name='landing-page'),
	path('dashboard/', views.Index, name='index'),
	path('drivers-list/', views.Drivers_list, name='drivers-list'),
	path('equipment-list/', views.Equipment_list, name='equipment-list'),
	path('create-driver/', views.Create_driver, name='create-driver'),
	path('create-equipment/', views.Create_equipment, name='create-equipment'),
    path('editdriver/<int:pk>/', views.EditDriver, name="editdriver"),
    path('editequipment/<int:pk>/', views.EditEquipment, name="editequipment"),
    path('delete-driver/<int:pk>/', views.DeleteDriver, name="delete-driver"),
    path('delete-equipment/<int:pk>/', views.DeleteEquipment, name="delete-equipment"),
    path('export-csv/', views.Export, name="export"),
	path('login/', views.Login, name='login'),
	path('register/', views.Register, name='register'),
	path('logout/', views.Logout, name='logout'),
]