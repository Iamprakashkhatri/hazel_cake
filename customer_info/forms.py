from django import forms
from .models import Department,Organization,Customer
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


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
    




    
        
