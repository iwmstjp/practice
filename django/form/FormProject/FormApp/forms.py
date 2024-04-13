from django import forms


class UserInfo(forms.Form):
    name = forms.CharField(label='Na', max_length=10, min_length=5)
    age = forms.IntegerField()
    mail = forms.EmailField(widget=forms.TextInput(
        attrs={'class':'mail-class', 'placeholder':'@mail.com'})
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
    memo = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        self.fields['job'].widget.attrs['id'] = 'id_job'
        self.fields['hobbies'].widget.attrs['class'] = 'hobbies_class'

