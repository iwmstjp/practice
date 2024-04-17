from django import forms
from django.core import validators
from .models import Post

class UserInfo(forms.Form):
    name = forms.CharField(label='Na', max_length=10, min_length=5)
    age = forms.IntegerField(validators=[validators.MinValueValidator(20, message='More than 20')])
    mail = forms.EmailField(widget=forms.TextInput(
        attrs={'class':'mail-class', 'placeholder': '@mail.com'})
    )
    verify_mail = forms.EmailField(
        label='confirm email',
        widget=forms.TextInput(
        attrs={'class': 'mail-class', 'placeholder': '@mail.com'})
    )
    is_married = forms.BooleanField(required=False)
    birthday = forms.DateField(initial='1990-01-01')
    salary = forms.IntegerField()
    job = forms.ChoiceField(choices=(
        (1, 'full-time'),
        (2, 'self-employed'),
        (3, 'student'),
        (4, 'unemployed')
    ))
    hobbies = forms.MultipleChoiceField(choices=(
        (1, 'sports'),
        (2, 'reading'),
        (3, 'movies'),
        (4, 'etc')
    ),widget=forms.CheckboxSelectMultiple)
    homepage = forms.URLField(required=False)
    memo = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        self.fields['job'].widget.attrs['id'] = 'id_job'
        self.fields['hobbies'].widget.attrs['class'] = 'hobbies_class'

    def clean_homepage(self):
        homepage = self.cleaned_data['homepage']
        if not homepage.startswith('https'):
            raise forms.ValidationError('Only https')

    def clean(self):
        cleaned_data = super().clean()
        mail = cleaned_data['mail']
        verify_mail = cleaned_data['verify_mail']
        if mail != verify_mail:
            raise forms.ValidationError('Type same email address')


class BaseForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        print(f'Form: {self.__class__.__name__}')
        return super(BaseForm, self).save(*args, **kwargs)


class PostModelForm(BaseForm):
    name = forms.CharField(label='Na')
    title = forms.CharField(label='title')
    memo = forms.CharField(
        label='memo',
        widget=forms.Textarea(attrs={'rows':6, 'cols':15})
    )
    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ["title"]

    def save(self, *args, **kwargs):
        obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
        obj.name = obj.name.upper()
        print(type(obj))
        print('save done')
        obj.save()
        return obj

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'aa':
            raise validators.ValidationError('Invalid name')
        return name

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == 'aa':
            raise validators.ValidationError('Invalid title')
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        is_exists = Post.objects.filter(title=title).first()
        if is_exists:
            raise validators.ValidationError('The title already exits')

class FormSetPost(forms.Form):
    title = forms.CharField(label='title')
    memo = forms.CharField(label='memo')