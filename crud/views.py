from urllib import request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders, Users

# CRUD feature for Gender
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
 
def editGender(request, genderId):
   try:
        if request.method=='POST':
           genderObj = Genders.objects.get(pk=genderId)
           gender = request.POST.get('gender')

           genderObj.gender = gender
           genderObj.save()

           messages.success(request,'Gender updated succesfully! ')

           data = {
                'gender': genderObj
            }
           
           return render(request, 'gender/editGender.html', data)

        else:
            genderObj = Genders.objects.get(pk=genderId)

            data = {
                'gender': genderObj
            }
       
            return render(request, 'gender/editGender.html', data)
        
   except Exception as e:
        return HttpResponse(f' Error Occured during edit gender: {e}')
def delete_gender(request, genderId):
    try:
        if request.method=='POST':
            genderObj = Genders.objects.get(pk=genderId)
            genderObj.delete()

            messages.success(request,'Gender deleted succesfully! ')
            return redirect('/gender/list')
        else:
         
         genderObj = Genders.objects.get(pk=genderId)

         data = {
                'gender': genderObj
            }
       
        return render(request, 'gender/DeleteGender.html', data)
    except Exception as e:
         return HttpResponse(f' Error Occured during deleteGender: {e}')
    

#CRUD feature for USERS

def add_user(request):
   try:
        if request.method=='POST':
            fullName = request.POST.get('full_name')
            gender = request.POST.get('gender')
            birthDate = request.POST.get('birth_date')
            address = request.POST.get('address')
            contactNumber = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirm_password')

            Users.objects.create(
               full_name=fullName,
               gender=Genders.objects.get(pk=gender),
               birthdate=birthDate,
               address=address,
               contact_number=contactNumber,
               email=email,
               username=username,
               password=password
            ).save()

            messages.success(request,'User added succesfully! ')
            return redirect('/users/add')
        else:
            gender_list = Genders.objects.all()
            data = {
                'genders': gender_list
            }
            return render(request, 'users/addUser.html', data)
      
   except Exception as e:
        return HttpResponse(f' Error Occured during add user: {e}')
   
def userList(request):
    try:
        userObj = Users.objects.select_related('gender')
        data = {
            'users': userObj
        }
        return render(request, 'users/usersList.html', data)
    except Exception as e:
        return HttpResponse(f' Error Occured during load users: {e}')
   