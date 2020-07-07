from django.shortcuts import render, redirect

from .forms import *
from .models import *
# Create your views here.
def upload(request):
    output = ImgUpload.objects.all()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UserForm()

    context = {
        'form':form, 
        'output':output,
    }

    return render(request, 'img_upload.html', context)