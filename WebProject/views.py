from django.shortcuts import render

from .models import TitleProfile
from .forms import InputForm, TitleProfileForm

# Create your views here.

def home(request):
    context = {'message': 'Success'}
    return render(request,'index.html',context)

def contact(request):
    context = {'info':'Hello'}
    return render(request,'contact.html',context)

def loginhome(request):
    context = {'message': 'Success'}
    return render(request,'home.html',context)

def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)

def profile(request):
    if request.method=='GET':
        context ={'message':'Success'}
        context['titleform']=TitleProfileForm()
        print(context)
        return render(request,'profile.html',context)

def updateProfile(request):
    if request.method=='GET':
        context = {'message':'Success'}
        try:
            formdata = TitleProfile.objects.get(pk=1)
            context['titleform']=TitleProfileForm(instance=formdata)
        except:
            context['titleform']=TitleProfileForm()
            print(context)
        return render(request,'profile-edit.html',context)
        
    elif request.method=='POST':
        print('request.POST',request.POST)
        newForm = TitleProfileForm(request.POST)
        if newForm.is_valid():
            context = {'message': 'Success'}
            newForm.save()
        formdata = TitleProfile.objects.get(pk=1)
        context['titleform']=TitleProfileForm(instance=formdata)
        print(context)
        return render(request,'profile-edit.html',context)
