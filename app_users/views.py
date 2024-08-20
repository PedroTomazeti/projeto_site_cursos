from django.shortcuts import render

# Create your views here.
def add_users(request):
    return render(request, 'users/add_users.html')
