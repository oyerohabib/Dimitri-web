from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
    
def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)] 

class Driver(models.Model):

	STATUS = (
	        ("pending", "pending"),
	        ("hired", "hired"),
	        ("terminated", "terminated"),
	    )

	EVR = (
	        ("done", "done"),
	        ("partial", "partial"),
	        ("not started", "not started"),
	    )

	Name = models.CharField(max_length=50)
	Hire_Date = models.DateTimeField()
	Term_Date = models.DateTimeField()
	Status = models.CharField(default="pending", choices=STATUS, max_length=14)
	EVR = models.CharField(default="not started", choices=EVR, max_length=14)
	Notes = models.TextField()
	Phone = models.IntegerField()
	DOB = models.DateField()
	City = models.CharField(max_length=24)
	Address = models.TextField()
	State = models.CharField(max_length=36)
	Zip = models.CharField(max_length=14)
	License = models.CharField(max_length=24)
	License_State = models.CharField(max_length=14)
	SSN = models.CharField(max_length=24)

	def __str__(self):
		return self.Name

class Equipment(models.Model):

	def year_choices():
	    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

	def current_year():
	    return datetime.date.today().year

	STATUS = (
	        ("active", "active"),
	        ("inactive", "inactive")
	    )

	OWNERSHIP_TYPE = (
	        ("leased", "leased"),
	        ("owned", "owned")
	    )

	IFTA = models.IntegerField()
	Date_placed = models.DateField()
	Truck = models.IntegerField()
	Status = models.CharField(default="inactive", choices=STATUS, max_length=14)
	Year = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year])
	Make = models.CharField(max_length=24)
	Model = models.CharField(max_length=24)
	GVWR = models.IntegerField()
	VIN = models.CharField(max_length=24)
	License_Plate = models.IntegerField()
	License_Plate_State = models.CharField(max_length=9)
	Leased_or_Owned = models.CharField(default="leased", choices=OWNERSHIP_TYPE, max_length=14)
	ELD = models.CharField(max_length=24)

	def __str__(self):
		return str(self.IFTA)