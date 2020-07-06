from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def userExist(request):
	context = {
		'pageTitle':'DAFTAR',
	}
	return render(request, 'user/user_exist.html', context)

def registerView(request):
	check_password = False
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		check_username = User.objects.filter(username=username)
		check_email = User.objects.filter(email=email)
		if check_username or email:
			return userExist(request)

		if password1 != password2:
			check_password = True
		else:
			user = User.objects.create_user(username=username, email=email, password=password1)
			return redirect('/')

	context = {
		'pageTitle':'DAFTAR',
		'check_password':check_password
	}

	return render(request, 'user/register.html', context)