from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders

# Create your views here.
def gender_list(request):
 try:
    genders=Genders.objects.all()
    data={
        'genders':genders
    }
    return render(request, 'gender/genderlist.html', data)
 except Exception as e:
    return HttpResponse(f'Error occurred during load genders: {e}')


def add_gender(request):
    
 try:
     if request.method=='POST':
         gender = request.POST.get('gender')
         Genders.objects.create(gender=gender).save()
         messages.success(request,'Gender added succesfully! ')
         return redirect('/gender/list')
     else:    
      return render(request, 'gender/addgender.html')
 except Exception as e:
    return HttpResponse(f' Error Occured during add gender: {e}')