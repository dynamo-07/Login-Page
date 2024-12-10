from django.contrib import messages
from django.shortcuts import render,redirect
user_data=[]
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username1')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('confirm-password1')
        if password == confirm_password:
            user_data.append({'username': username, 'email': email, 'password': password})
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('index') 
        else:
            return render(request, 'signup.html', {'message': 'Passwords do not match!'})

    return render(request, 'signup.html')

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        for user in user_data:
            if user['username'] == username and user['password'] == password:
                mess = "Welcome, " + username
                return render(request, 'index.html', {'message1': mess})
        return render(request, 'index.html', {'message1': 'Invalid username or password!'})

    return render(request, 'index.html')
