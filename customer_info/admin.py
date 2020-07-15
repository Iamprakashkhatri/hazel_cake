from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer,Department,Package,Organization

admin.site.register(Customer)
admin.site.register(Department)
admin.site.register(Package)
admin.site.register(Organization)

