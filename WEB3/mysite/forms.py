from django import forms



class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )


    fname = forms.CharField(
        required = True,
        label = 'FirstName',
        max_length = 32,
    )

    lname = forms.CharField(
        required = True,
        label = 'Last Name',
        max_length = 32,
    )

    Gender = forms.CharField(
        required = True,
        label = 'Gender',
        max_length = 32,
    )
    DOB = forms.CharField(
        required = True,
        label = 'DOB',
        max_length = 32,
    )




