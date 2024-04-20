from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory

# Create your views here.
from . import forms
from .models import ModelSetPost

from django.core.files.storage import FileSystemStorage
import os


def index(request):
    return render(request, 'formapp/index.html')


def form_page(request):
    form = forms.UserInfo()
    if request.method == 'POST':
        form = forms.UserInfo(request.POST)
        if form.is_valid():
            print('success')
            # print(f"{form.cleaned_data['name']},{form.cleaned_data['mail']},{form.cleaned_data['age']}")
            print(form.cleaned_data)

    return render(
        request, 'formapp/form_page.html', context={
            'form': form
        }
    )


def form_post(request):
    form = forms.PostModelForm()
    if request.method =='POST':
        form = forms.PostModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(
        request, 'formapp/form_post.html', context={'form': form}
    )


def form_set_post(request):
    TestFormset = formset_factory(forms.FormSetPost, extra=3)
    formset = TestFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    return render(
        request, 'formapp/form_set_post.html',
        context={'formset': formset}
    )


def modelform_set_post(request):
    # TestFormSet = modelformset_factory(ModelSetPost, fields='__all__', extra=3)
    TestFormSet = modelformset_factory(ModelSetPost, form=forms.ModelFormSetPost, extra=3)
    formset = TestFormSet(request.POST or None)
    if formset.is_valid():
        formset.save()
    return render(request, 'formapp/modelform_set_post.html',
                  context={'formset': formset})

def upload_sample(request):
    if request.method == 'POST' and request.FILES['upload_file']:
        upload_file = request.FILES['upload_file']
        fs = FileSystemStorage()
        path = os.path.join('upload', upload_file.name)
        file = fs.save(path, upload_file)
        uploaded_file_url = fs.url(file)
        return render(request, 'formapp/upload_file.html',
                      context={'uploaded_file_url': uploaded_file_url}
                      )
    return render(request, 'formapp/upload_file.html')
