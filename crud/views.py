from urllib import request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders, Users
from django.shortcuts import render, get_object_or_404
from .models import Users # Ensure your User model is imported
from django.contrib.auth.hashers import make_password

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
        n
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
            profilePic = request.FILES.get('profile_pic')
            confirmPassword = request.POST.get('confirm_password')
                
            if password != confirmPassword:
                messages.error(request, 'Passwords do not match!')
                return redirect('/users/add')

            if len(password) < 8:
                messages.error(request, 'Password must be at least 8 characters!')
                return redirect('/users/add')

            Users.objects.create(
               full_name=fullName,
               gender=Genders.objects.get(pk=gender),
               birthdate=birthDate,
               address=address,
               contact_number=contactNumber,
               email=email,
               username=username,
               profile_pic=profilePic if profilePic else 'profile_pics/default_profile_pic.png',
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
       
def delete_user(request, userId):
    try:
        if request.method == 'POST':
            userObj = Users.objects.get(pk=userId)
            userObj.delete()

            messages.success(request, 'User deleted successfully!')
            return redirect('/users/list')
        else:

            userObj = Users.objects.get(pk=userId)

            data = {
                'user': userObj
            }

        return render(request, 'users/DeleteUser.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during deleteUser: {e}')    
    

def editUser(request, userId):
   try:
        if request.method=='POST':
            userObj = Users.objects.get(pk=userId)
            

            if request.FILES.get('profile_pic'):
                userObj.profile_pic = request.FILES.get('profile_pic')
                userObj.save()

            messages.success(request,'User updated succesfully! ')

            data = {
                'user': userObj
            }
           
            return render(request, 'users/editUser.html', data)

        else:
            userObj = Users.objects.get(pk=userId)

            data = {
                'user': userObj
            }
       
            return render(request, 'users/editUser.html', data)
        
   except Exception as e:
        return HttpResponse(f' Error Occured during edit user: {e}')

# additional features
# 1. search the query for specific item
def searchUser(request):
    searched = request.GET.get('searched', "")
    if searched:
        items = Users.objects.filter(name__icontains=searched)
    else:
        items = Users.objects.none()
    return render(request, 'usersList.html', {
        'user': items,
        'searched': searched
    })