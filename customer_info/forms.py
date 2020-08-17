from django import forms
from .models import Department,Organization,Customer
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email id'}
    ), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    ), required=True, max_length=50)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        email=self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Email Doesnot Exist.'))
        return email
    # def clean_password_and_email(self):
    #     password=self.cleaned_data['password']
    #     email=self.cleaned_data['email']
    #     users = User.objects.filter(email=email)
    #     if not authenticate(username=users.first().username, password=password):
    #         raise forms.ValidationError(_('Password Doesnot Exist.'))
    #     return password,email


class OrganizationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Name Of Organization'}
    ), required=True, max_length=100)
    contact_person = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Person Name'}
    ), required=False, max_length=50)
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter  location'}
    ), required=False, max_length=50)
    contact_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}
    ), required=False)
    anniversary = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter anniversary date'}
    ), required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email Id'}
    ), required=False, max_length=50)


    class Meta:
        model = Organization
        fields = ['name', 'contact_person', 'location', 'contact_number', 'anniversary', 'email']

    def clean_name(self):
        name=self.cleaned_data['name']
        if Organization.objects.filter(name=name).exists():
            raise forms.ValidationError(_('User name already exist.'))
        return name

class OrganizationUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Name Of Organization'}
    ), required=True, max_length=100)
    contact_person = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Person Name'}
    ), required=False, max_length=50)
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter  location'}
    ), required=False, max_length=50)
    contact_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}
    ), required=False)
    anniversary = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter anniversary date', 'id': 'Anniversary'}
    ), required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email Id'}
    ), required=False, max_length=50)


    class Meta:
        model = Organization
        fields = ['name', 'contact_person', 'location', 'contact_number', 'anniversary', 'email']

class DepartmentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Name Of Organization'}
    ), required=True, max_length=100)
    contact_person = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Person Name'}
    ), required=False, max_length=50)
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter  location'}
    ), required=False, max_length=50)
    contact_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}
    ), required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email Id'}
    ), required=False, max_length=50)


    class Meta:
        model = Department
        fields = ['name', 'contact_person', 'location', 'contact_number','email']

    def clean_name(self):
        name=self.cleaned_data['name']
        if Department.objects.filter(name=name).exists():
            raise forms.ValidationError(_('User name already exist.'))
        return name


class DepartmentUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Name Of Organization'}
    ), required=True, max_length=100)
    contact_person = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Person Name'}
    ), required=False, max_length=50)
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter  location'}
    ), required=False, max_length=50)
    contact_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}
    ), required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email Id'}
    ), required=False, max_length=50)


    class Meta:
        model = Department
        fields = ['name', 'contact_person', 'location', 'contact_number','email']

class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter first name'}
    ), required=True, max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter last name '}
    ), required=True, max_length=100)
    birthdate = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter birthdate', 'id': 'birthdate'}
    ), required=True)
    designation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter designation'}
    ), required=False, max_length=100)
    contact_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}
    ), required=False)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email Id'}
    ), required=False, max_length=50)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birthdate', 'designation', 'contact_number','email']

    # def clean_first_name(self):
    #     first_name=self.cleaned_data['first_name']
    #     if Customer.objects.filter(first_name=first_name).exists():
    #         raise forms.ValidationError(_('User first name already exist.'))
    #     return first_name

    # def clean_last_name(self):
    #     last_name=self.cleaned_data['last_name']
    #     if Customer.objects.filter(last_name=last_name).exists():
    #         raise forms.ValidationError(_('User first name already exist.'))
    #     return last_name

class DateRangeForm(forms.Form):
    date_start = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter start date', 'id': 'date1', 'input_format': '%d-%m-%Y'}
    ), required=True)
    date_end = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter end date', 'id': 'date2'}
    ), required=True)

    # date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=BootstrapDateTimePickerInput()
    # )


class AnniversaryDateRangeForm(forms.Form):
    anniversary_date_start = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter start date', 'id': 'date3'}
    ), required=True)
    anniversary_date_end = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter end date', 'id': 'date4'}
    ), required=True)

    




    
        
