from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from django.conf import settings
# Create your views here.

def submit(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            content = form.cleaned_data['document']
            if content.size > int(settings.MAX_UPLOAD_SIZE):
                return(render(request,'submit.html',{'form':form,'message':'File Too Big :('}))
            if not content.name.endswith(('.pdf','.epub','.txt')):
                return(render(request,'submit.html',{'form':form,'message':'Invalid Format :('}))
            form.save()
            form = UploadForm()
            return render(request,'submit.html',{'form':form,'message':'Thanks For Uploading :)'})
    else:
        form = UploadForm()
        return render(request,'submit.html',{'form':form})