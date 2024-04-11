from django.shortcuts import render

# Create your views here.
from . import forms

def index(request):
    return render(request, 'formapp/index.html')

def form_page(request):
    form = forms.UserInfo()
    if request.method == 'POST':
        form = forms.UserInfo(request.POST)
        if form.is_valid():
            print('success')
            print("{form.cleaned_data}['name'],{form.cleaned_data}['mail'],{form.cleaned_data}['age']")
    return render(
        request, 'formapp/form_page.html', context={
            'form':form
        }
    )