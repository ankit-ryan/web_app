from django import forms
# from django.core.validators import ValidationError

# # def validateEmail(value):
#     if value.find('@mytectra.com')<0:
#         raise ValidationError("invalid email")

# def validateName(name):
#
#     if name.isdigit():
#
#         raise ValidationError("Invalid Name")
#
#     elif name.find(' ') >= 0:
#
#         raise ValidationError("space not allowed in name")


class FormExample(forms.Form):

    cityValues = (
        ('', '_ _Select option_ _'),
        ('chennai', 'chennai'),
        ('Bangalore', 'Bangalore'),
        ('Hyderabad', 'Hyderabad'),
        ('Pune', 'Pune'),
        ('Mumbai', 'Mumbai')
    )
    gn=(

        ('f', 'female'),
        ('m', 'male')
    )
    is_active = forms.CharField(widget=forms.CheckboxInput)
    is_not_active = forms.CharField(widget=forms.CheckboxInput)
    is_active3 = forms.BooleanField()
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    city = forms.ChoiceField(choices=cityValues)

    username = forms.CharField(
        label='Employee Name',
        min_length=8,
        max_length=20,
        required=True,
        error_messages={
            'required':'Employee name cannot be blank!',
            'min_length':'new message'
        },
        help_text='<h3>please provide valid employee name</h3>',
        widget=forms.TextInput(attrs={
            'placeholder':'Employee name'
        }),
        # validators=[validateName]
    )
    email = forms.EmailField(
        # validators=[validateEmail]
    )
    address = forms.CharField(
        widget=forms.Textarea
    )

    password1= forms.CharField(widget = forms.PasswordInput)
    password2= forms.CharField(widget = forms.PasswordInput)
    def clean(self):
        formvalues=self.cleaned_data

        if 'username' in formvalues:

            if formvalues['username'].isdigit():
                self.errors['username']=['invalid username22']
        if 'email' in formvalues:

            if formvalues['email'].find('@mytectra.com')<0:

                self.errors['email']=['invalid email']

        if 'password1' in formvalues and 'password2' in formvalues:

            if formvalues['password1'] != formvalues['password2']:

                self.errors['password1'] = ['password mismatch']
                self.errors['password2'] = ['password mismatch']

        return formvalues


