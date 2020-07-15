from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings

class Package(models.Model):
    name=models.CharField(max_length=300)
    cake_flavour=models.CharField(max_length=300)
    quantity=models.IntegerField()
    knife=models.BooleanField(default=False)
    candle = models.BooleanField(default=False)
    tissue = models.BooleanField(default=False)
    card = models.BooleanField(default=False)
    flower = models.BooleanField(default=False)
    chocolates = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Organization(models.Model):
    name = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=300,blank=True,null=True)
    location = models.CharField(max_length=300,blank=True,null=True)
    contact_number = models.IntegerField(blank=True,null=True)
    anniversary = models.DateTimeField(auto_now=False,blank=True,null=True)
    package = models.ForeignKey(Package, null=True,on_delete=models.SET_NULL,blank=False,related_name='organization_package')
    email = models.EmailField(max_length=80,blank=True,null=True)

    def __str__(self):
        return self.name



class Department(models.Model):
    name=models.CharField(max_length=300)
    contact_person=models.CharField(max_length=300,blank=True,null=True)
    location=models.CharField(max_length=300,blank=True,null=True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='department_organization')
    contact_number=models.IntegerField(blank=True,null=True)
    package=models.ForeignKey(Package, null=True, blank=True, on_delete=models.SET_NULL,related_name='department_package')
    email=models.EmailField(max_length=70,blank=True,null=True)


    def get_absolute_url_detail(self):
        return reverse("employeerecord:department-detail", kwargs={"pk": self.pk})
    def get_absolute_url_update(self):
        return reverse("employeerecord:department-update", kwargs={"pk": self.pk})
    def get_absolute_url_delete(self):
        return reverse("employeerecord:department-delete", kwargs={"pk": self.pk})


    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    birthdate = models.DateTimeField(auto_now=False)
    package= models.ForeignKey(Package, null=True, blank=True, on_delete=models.SET_NULL,related_name='user_package')
    designation = models.CharField(null=True,blank=True,max_length=200)
    contact_number = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=80,null=True,blank=True)
    department = models.ForeignKey(Department,related_name='department_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    def get_absolute_url_user_update(self):
        return reverse("employeerecord:user-update", kwargs={"pk": self.pk})
    def get_absolute_url_user_delete(self):
        return reverse("employeerecord:user-delete", kwargs={"pk": self.pk})



