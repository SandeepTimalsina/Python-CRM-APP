from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm,AddRecordForm,UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Record

# Create your views here.

#-------Homepage------
def index(request):
    return render(request,'webapp/index.html')

#--------Register--------
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,'webapp/register.html', {
        "form":form,
    })
#----------Login-------

def login_view(request):
    form =LoginForm()
    if request.method =="POST":
        form = LoginForm(request,data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username ,password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    return render(request,'webapp/login.html',{
        'form':form,
    })   

#--------Dashboard view-------
@login_required(login_url='login')
def dashboard(request):

    my_records = Record.objects.all()
    context = {'records' : my_records}

    return render(request,'webapp/dashboard.html', context = context) 



#----------Log out-------------
def logout_view(request):
    logout(request)
    return render(request,'webapp/index.html',{
        "message":"Logged Out"
    })  

# -------Create a Record-------
@login_required(login_url ='login')
def create_record(request):
    form = AddRecordForm()
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {'form' : form}
    return render(request,'webapp/create-record.html',context = context)

#-----Update a Record-------
@login_required(login_url = 'login')
def update_record(request, pk):
    record = Record.objects.get(id = pk)
    form = UpdateRecordForm(instance = record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST , instance = record)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {'form' :form}

    return render(request,'webapp/update-record.html',context = context)

#-------View Single Record-------
@login_required(login_url = 'login')
def singular_record(request, pk):
    all_records = Record.objects.get(id = pk)
    context = {'record': all_records}
    return render(request,'webapp/view-record.html',context = context)


        




