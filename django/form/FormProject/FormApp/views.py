from django.shortcuts import render
from django.forms import formset_factory

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