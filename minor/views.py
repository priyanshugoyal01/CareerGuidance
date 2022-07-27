from django.views.generic.list import ListView
from .models import Interest, Branch, College,Customer
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password , check_password
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def quiz(request):
    return render(request, 'minor/quiz_page.html')


class InterestList(ListView):
    model = Interest


class BranchList(ListView):
    model = Branch

    def get_queryset(self, *args, **kwargs):
        qs = super(BranchList, self).get_queryset(*args, **kwargs)
        qs = qs.filter(interest__id=self.request.GET.get('interest_id'))
        return qs


class CollegeList(ListView):
    model = College

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeList, self).get_queryset(*args, **kwargs)
        qs = qs.filter(branch__id=self.request.GET.get('branch_id'))
        return qs

def signup(request):
    if request.method == 'GET':
        return render(request, 'minor/signup.html')
    else:
         postData = request.POST
         first_name = postData.get('firstname')
         last_name = postData.get('lastname')
         email = postData.get('email')
         number = postData.get('number')
         password = postData.get('password')
         #validation
         value  = {
             'first_name' : first_name,
             'last_name'  : last_name,
             'number' : number,
             'email' : email
         }

         customer = Customer(first_name=first_name,
                             last_name=last_name,
                             email=email,
                             number=number,
                             password=password)

         error_message = None

         if (not first_name):
             error_message = "First Name Required !!"
         elif len(first_name) < 2 :
             error_message = "First name should be more than 2 letter"
         elif (not last_name):
             error_message = "last Name Required !!"
         elif (not email):
             error_message = "Email Required !!"
         elif (not number):
             error_message = "Phone Number Required !!"
         elif (not password):
             error_message = "Password Required !!"
         elif len(number) < 10:
             error_message = "Invalid Phone Number!!"
         elif len(password) < 6:
             error_message = "Password Must be 8 character!!"
         elif customer.isExists() :
             error_message = "Email already registered !!"

         #saving

         if not error_message:
             print(first_name , last_name ,email, number, password)
             customer.password = make_password(customer.password)

             customer.register()
             return redirect('index.html')
         else:
             data = {
                 'error': error_message,
                 'values': value
             }
             return render(request, 'minor/signup.html', data )


def register(request):
    return  render(request, 'minor/register.html')


def login(request):
    return render(request, 'minor/login.html')
