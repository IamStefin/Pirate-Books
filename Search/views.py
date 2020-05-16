from django.shortcuts import render
from . import forms
from Submit.models import SubmitBook
from django.db.models import Q
# Create your views here.

def search(request):
    form = forms.SearchForm()
    if request.method == 'POST':
        queryset = SubmitBook.objects.filter(Q(title__icontains=request.POST['term'])| Q(author__icontains=request.POST['term']),approved=True)
        return render(request,'search.html',{'form':form,'books':queryset,'search':'True'})
    return render(request,'search.html',{'form':form,'books':SubmitBook.objects.all().filter(approved=True).order_by('-uploaded_at')[:10:1]})