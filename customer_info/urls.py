from django.urls import path
from .views import testing,OrganizationList,OrganizationDetail,OrganizationCreate,OrganizationUpdate,OrganizationDelete
from .views import (
    LoginView,
	get_package_detail,
	DepartmentDetail,
	DepartmentCreate,
    DepartmentUpdate,
    DepartmentDelete,
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeDelete,
    DashboardView,
    DateRange,
    AnniversaryDateRange,
	)

app_name='customer_info'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login-view'),
    path('testing',testing.as_view(),name='testing'),

    path('dashboard/',DashboardView.as_view(),name='dashboard'),

    path('organization-list/', OrganizationList.as_view(), name='organization-list'),
    path('organization/department/<int:pk>/', OrganizationDetail.as_view(), name='organization-detail'),
    path('organization-create/',OrganizationCreate.as_view(),name='organization-create'),
    path('organization-update/<int:pk>/', OrganizationUpdate.as_view(), name='organization-update'),
    path('organization-delete/<int:pk>/', OrganizationDelete.as_view(),name='organization-delete'),

    path('department/employee/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),
    path('department-create/<int:pk>/', DepartmentCreate.as_view(), name='department-create'),
    path('department-update/<int:pk>/',DepartmentUpdate.as_view(),name='department-update'),
    path('department-delete/<int:pk>/',DepartmentDelete.as_view(),name='department-delete'),

    path('employee-create/<int:pk>/',EmployeeCreate.as_view(),name='employee-create'),
    path('employee-update/<int:pk>/',EmployeeUpdate.as_view(),name='employee-update'),
    path('employee-delete/<int:pk>/',EmployeeDelete.as_view(),name='employee-delete'),

    path('date-range/', DateRange.as_view(), name='date-range'),
    path('anniversary-date-range/', AnniversaryDateRange.as_view(),name='anniversary-date-range'),

    path('package-detail/', get_package_detail, name='package-request'),

]
