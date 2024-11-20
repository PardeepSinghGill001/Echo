from django.shortcuts import render
from .models import Buzz
from .forms import BuzzForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request, 'index.html')

def buzz_list(request):
    buzzes=Buzz.objects.all().order_by('-created_at')
    return render(request,'buzz_list.html',{'buzzes':buzzes})

@login_required
def buzz_create(request):
    if request.method == "POST":
        form = BuzzForm(request.POST, request.FILES)
        if form.is_valid():
            buzz = form.save(commit=False)
            buzz.user = request.user
            buzz.save()
            return redirect('buzz_list')
    else:
        form = BuzzForm()
    return render(request,'buzz_form.html',{'form':form})

@login_required
def buzz_edit(request,buzz_id):
    buzz = get_object_or_404(Buzz, pk=buzz_id, user = request.user)
    if request.method == "POST":
        form = BuzzForm(request.POST, request.FILES, instance = buzz)
        if form.is_valid():
            buzz = form.save(commit=False)
            buzz.user = request.user
            buzz.save()
            return redirect('buzz_list')
    else:
        form = BuzzForm(instance=buzz)
    return render(request,'buzz_form.html',{'form':form})

@login_required
def buzz_delete(request, buzz_id):
    buzz = get_object_or_404(Buzz, pk=buzz_id, user=request.user)
    if request.method == "POST":
        buzz.delete()
        return redirect('buzz_list')
    return render(request,'buzz_confirm_delete.html',{'buzz':buzz})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('buzz_list')

    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

    
