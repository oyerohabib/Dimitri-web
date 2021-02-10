from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .resources import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def Landing_Page(request):
	return render(request, "core/landing-page.html")

@login_required
def Index(request):

	pending = Driver.objects.filter(Status="pending").count()
	hired = Driver.objects.filter(Status="hired").count()
	terminated = Driver.objects.filter(Status="terminated").count()

	done = Driver.objects.filter(EVR="done").count()
	partial = Driver.objects.filter(EVR="partial").count()
	not_started = Driver.objects.filter(EVR="not started").count()

	active = Equipment.objects.filter(Status="active").count()
	inactive = Equipment.objects.filter(Status="inactive").count()

	leased = Equipment.objects.filter(Leased_or_Owned="leased").count()
	owned = Equipment.objects.filter(Leased_or_Owned="owned").count()

	drivers_list = Driver.objects.all().order_by('-id')
	equipments_list = Equipment.objects.all().order_by('-id')

	title = "Welcome to the Dashboard"

	context = {"drivers_list":drivers_list, "equipments_list":equipments_list, 
	"pending":pending, "hired":hired, "terminated":terminated, "active":active, 
	"done":done, "partial":partial, "not_started":not_started, 
	"inactive":inactive, "leased":leased, "owned":owned, "title":title}

	return render(request, 'core/index.html', context)

@login_required
def Drivers_list(request):

	title = "Drivers List"

	drivers_list = Driver.objects.all().order_by('-id')

	context = {"drivers_list":drivers_list, "title":title}
	return render(request, 'core/drivers-list.html', context)

@login_required
def Equipment_list(request):

	title = "Equipment List"
	equipments_list = Equipment.objects.all().order_by('-id')

	context = {"equipments_list":equipments_list, "title":title}
	return render(request, 'core/equipment-list.html', context)

@login_required
def Create_equipment(request):
	title = "Create a New Equipment"
	form = EquipmentForm()
	if request.method == 'POST':
		form = EquipmentForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Equipment Added Successfully")
			return redirect('create-equipment')
	context = {"form":form, "title":title}
	return render(request, 'core/create-equipment.html', context)

@login_required
def Create_driver(request):
    title = "Add a New Driver"
    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Driver Added Successfully")
            return redirect('create-driver')

    context = {"form":form, "title":title}
    return render(request, 'core/create-driver.html', context)

@login_required
def EditDriver(request, pk):

    title = "Edit Driver's Information"
    driver = Driver.objects.get(id=pk)
    form = DriverForm(instance=driver)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            messages.success(request, "Driver details Edited Successfully")
            return redirect("drivers-list")

    context = {"form":form, "title":title}

    return render(request, "core/editdriver.html", context)

@login_required
def DeleteDriver(request, pk):

    title = "Delete Driver"
    driver = Driver.objects.get(id=pk)
    driver.delete()
    messages.error(request, "Driver Deleted Successfully")
    return redirect("drivers-list")

    context = {"driver":driver, "title":title}

    return render(request, "core/drivers-list.html", context)

@login_required
def EditEquipment(request, pk):

    title = "Edit Equipment"
    equipment = Equipment.objects.get(id=pk)
    form = EquipmentForm(instance=equipment)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipment Edited Successfully")
            return redirect("equipment-list")

    context = {"form":form, "title":title}

    return render(request, "core/editequipment.html", context)

@login_required
def DeleteEquipment(request, pk):

    title = "Delete Equipment"
    equipment = Equipment.objects.get(id=pk)
    equipment.delete()
    messages.error(request, "Equipment Deleted Successfully")
    return redirect("equipment-list")

    context = {"equipment":equipment, "title":title}

    return render(request, "core/equipment-list.html", context)

@login_required
def Export(request):
	driver_resource = DriverResources()
	dataset = driver_resource.export()
	response = HttpResponse(dataset.csv, content_type="text/csv")
	response['Content-Disposition'] = 'attachment/ filename="driver.csv"'
	return response

def Register(request):
	title = "Create a new Account"
	if request.user.is_authenticated:
		return redirect('index')

	elif request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if User.objects.filter(username=username).exists():
			messages.info(request, "Username Taken, try a new Username")
			return redirect('register')
		elif User.objects.filter(email=email).exists():
			messages.info(request, "Email Taken, try a new Email")
			return redirect('register')
		else:
			user = User.objects.create_user(username=username, password=password1, email=email)
			user.save()
			messages.success(request, "You have successfully created an account")
			return redirect('login')

	return render(request, 'auth/sign-up.html', {"title":title})

def Login(request):

	title = "Login to the Dashboard"

	if request.user.is_authenticated:
		return redirect('index')

	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username or Password is incorrect')

		return render(request, 'auth/login.html', {"title":title})

def Logout(request):
	logout(request)
	return redirect('login')