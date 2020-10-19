from django.shortcuts import render,redirect
from accounts.models import Reports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST['gender']
        age = request.POST['age']
        crimetype = request.POST['crimetype']
        describecrime = request.POST['describecrime']
        crimelocation = request.POST['crimelocation']
        youraddress = request.POST['youraddress']
        reports.objects.create(name=name,mobile=mobile,email=email,dob=dob,gender=gender,age=age,crimetype=crimetype,crimelocation=crimelocation,describecrime=describecrime,youraddress=youraddress)
        return redirect('dashboard.html')
    else:
        return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()       
    return render(request,'registration/register.html',{'form':form})








