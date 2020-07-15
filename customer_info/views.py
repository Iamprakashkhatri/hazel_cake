from django.shortcuts import render,redirect,reverse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, JsonResponse
from dateutil import parser

from .models import Organization,Department,Package,Customer
from .forms import OrganizationForm,OrganizationUpdateForm,DepartmentForm,DepartmentUpdateForm,EmployeeForm

import datetime
from datetime import date, timedelta



class testing(TemplateView):

    def get (self,request):
        context = {}
        return render(request, 'testing.html',{})

class DashboardView(TemplateView):
    def get(self,request):
        current_week = (datetime.date.today())
        current_week_max = (datetime.date.today()+timedelta(days=7))
        current_month=datetime.datetime.now().month

        today_employee= Customer.objects.filter(birthdate=date.today()).order_by('birthdate')
        tomorrow_employee=Customer.objects.filter(birthdate=date.today()+timedelta(1)).order_by('birthdate')
        this_week_employee=Customer.objects.filter(birthdate__gte=current_week,birthdate__lte=current_week_max).order_by('birthdate')
        this_month_employee=Customer.objects.filter(birthdate__month=current_month).order_by('birthdate')
        all_employee=Customer.objects.all().order_by('birthdate')

        today_anniversary = Organization.objects.filter(anniversary=date.today()).order_by('anniversary')
        print('todays_anniversary',today_anniversary)
        tomorrow_anniversary = Organization.objects.filter(anniversary=date.today() + timedelta(1)).order_by(
            'anniversary')
        print('tomorrow_anniversary',tomorrow_anniversary)
        this_week_anniversary = Organization.objects.filter(anniversary__gte=current_week,anniversary__lte=current_week_max).order_by('anniversary')
        this_month_anniversary = Organization.objects.filter(anniversary__month=current_month).order_by('anniversary')
        all_org_anniversary = Organization.objects.all().order_by('anniversary')
        print('all_org_anniversary',all_org_anniversary)

        context= {
        'today_employees':today_employee,
        'tomorrow_employees':tomorrow_employee,
        'this_week_employees':this_week_employee,
        'this_month_employees':this_month_employee,
        'all_employees':all_employee,

        'today_anniversary':today_anniversary,
        'tomorrow_anniversary':tomorrow_anniversary,
        'this_week_anniversary':this_week_anniversary,
        'this_month_anniversary':this_month_anniversary,
        'all_org_anniversary':all_org_anniversary,
        }
        return render(request,'login/dashboard.html',context)


class DashboardView1(TemplateView):
    login_url = ('employeerecord:login-view')

    def get(self, request):
        # current_week = date.today().isocalendar()[2]
        current_week = (datetime.date.today())
        current_week_max = (datetime.date.today()+timedelta(days=7))

        # print(current_week)
        current_month = datetime.datetime.now().month

        today_user = DepartmentUsers.objects.filter(birthdate=date.today()).order_by('birthdate')
        tomorrow_user = DepartmentUsers.objects.filter(birthdate=date.today() + timedelta(1)).order_by('birthdate')
        this_week_user = DepartmentUsers.objects.filter(birthdate__gte=current_week,birthdate__lte=current_week_max).order_by('birthdate')
        this_month_user = DepartmentUsers.objects.filter(birthdate__month=current_month).order_by('birthdate')
        all_user = DepartmentUsers.objects.all().order_by('birthdate')

        # today_anniversary = Organization.objects.filter(anniversary=date.today()).order_by('anniversary')
        # tomorrow_anniversary = Organization.objects.filter(anniversary=date.today() + timedelta(1)).order_by(
        #     'anniversary')
        # this_week_anniversary = Organization.objects.filter(anniversary__gte=current_week,anniversary__lte=current_week_max).order_by('anniversary')
        # this_month_anniversary = Organization.objects.filter(anniversary__month=current_month).order_by('anniversary')
        # all_org_anniversary = Organization.objects.all().order_by('anniversary')

        daterangeform = DateRangeForm()
        anniversary_daterangeform = AnniversaryDateRangeForm()

        return render(request, 'login/dashboard.html',
                      {'today_user': today_user, 'tomorrow_user': tomorrow_user, 'this_week_user':
                          this_week_user, 'this_month_user': this_month_user, 'all_user': all_user,
                       'form': daterangeform,
                       'form1': anniversary_daterangeform,
                       'today_anniversary': today_anniversary, 'tomorrow_anniversary': tomorrow_anniversary,
                       'this_week_anniversary': this_week_anniversary, 'this_month_anniversary': this_month_anniversary,
                       'all_org_anniversary': all_org_anniversary})


def get_package_detail(request):
    package_name_request = request.GET.get("package_name", None)
    print('package',package_name_request)
    package_name = Package.objects.get(name__exact=package_name_request)
    context = {
        'name': package_name.name,
        'flavour': package_name.cake_flavour,
        'quantity': package_name.quantity,
        'knife': package_name.knife,
        'candle': package_name.candle,
        'tissue': package_name.tissue,
        'card': package_name.card,
        'flower': package_name.flower,
        'chocolates': package_name.chocolates
    }

    print("this is", package_name.cake_flavour)
    return JsonResponse(context)

class OrganizationList(ListView):
    model = Organization
    template_name = 'organizations/organization-list.html'
    context_object_name = 'organizations'

class OrganizationDetail(DetailView):
    model = Organization
    template_name = 'organizations/organization-detail.html'

    def get_context_data(self, **kwargs):
        context = super(OrganizationDetail, self).get_context_data(**kwargs)
        context['departments'] = Department.objects.filter(organization=self.kwargs['pk'])
        context['organization_id'] = self.kwargs['pk']
        return context

class OrganizationCreate(TemplateView):
    # model=Organization
    # template_name = 'organizations/organization-create.html'
    # form_class = OrganizationForm
    # success_url = '/organization-list/'

    # def get_context_data(self, **kwargs):
    #     context = super(OrganizationCreate, self).get_context_data(**kwargs)
    #     context['packages'] = Package.objects.all()
    #     return context

    template_name = 'organizations/organization-create.html'
    def get(self, request):
        context = {}
        context['form'] = OrganizationForm
        context['packages'] = Package.objects.all()
        return render(request, self.template_name, context)


    def post(self, request):
        form = OrganizationForm(request.POST, request.FILES or None)
        anniversary = request.POST.get('Anniversary',None)
        print('anniversary',anniversary)
        if anniversary:
            parsed_date1 = parser.parse(anniversary)
        else:
            parsed_date1=None
        print("this is parsed date", parsed_date1)
        if parsed_date1 is not None:
            parse_date1 = parsed_date1.strftime("%Y-%m-%d")
        else:
            parse_date1=None
        package1=request.POST.get("package", None)
        print(package1)
        try:
            package = Package.objects.get(name=package1)
        except:
            package=None


        if form.is_valid():
            name = form.cleaned_data['name']
            contact_person=form.cleaned_data['contact_person']
            location=form.cleaned_data['location']
            contact_number=form.cleaned_data['contact_number']
            anniversary=parse_date1
            package=package
            email=form.cleaned_data['email']


            Organization.objects.create(

                name=name,
                contact_person=contact_person,
                location=location,
                contact_number=contact_number,
                anniversary=anniversary,
                package=package,
                email=email,
            )
            return redirect(reverse('customer_info:organization-list'))
        
        packages = Package.objects.all()
        return render(request, 'organizations/organization-create.html', {'form':form,'packages':packages})

# class OrganizationUpdate(UpdateView):
# 	model=Organization
# 	template_name='organizations/organization-update.html'
# 	form_class = OrganizationUpdateForm
# 	success_url='/organization-list/'

class OrganizationUpdate(TemplateView):
    # model=Organization
    template_name='organizations/organization-update.html'
    # form_class = OrganizationUpdateForm
    # success_url='/organization-list/'

    def get(self, request, *args, **kwargs):

        organization = Organization.objects.get(id=self.kwargs['pk'])
        form = OrganizationUpdateForm(instance=organization)
        if (Package.objects.filter(organization_package=self.kwargs['pk'])).order_by('id'):
            packages = Package.objects.all()
            package=Package.objects.get(organization_package=self.kwargs['pk'])
            store_package=[]
            for package1 in packages:
                if package1!=package:
                    store_package.append(package1)
            context={
            'form':form,
            'package':package,
            'store_package':store_package,
            }
            return render(request, self.template_name, context)
        else:
            context={
            'form':form,
            'package':None,
            'store_package':Package.objects.all()
            }
            return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = OrganizationUpdateForm(request.POST, request.FILES or None)
        package1 = request.POST.get('package',None)
        anniversary = request.POST.get('anniversary',None)
        obj = Organization.objects.get(id=self.kwargs['pk'])
        package = Package.objects.get(name=package1)
        if anniversary:
            parsed_date1 = parser.parse(anniversary)
        else:
            parsed_date1 = None
        print("this is parsed date", parsed_date1)
        if parsed_date1 is not None:
            parse_date1 = parsed_date1.strftime("%Y-%m-%d")
        else:
            parse_date1 = None

        if form.is_valid():
            Organization.objects.filter(id=obj.id).update(
                name=form.cleaned_data['name'],
                contact_person=form.cleaned_data['contact_person'],
                location=form.cleaned_data['location'],
                contact_number=form.cleaned_data['contact_number'],
                anniversary=parse_date1,
                package=package,
                email=form.cleaned_data['email'],
            )
            return redirect(reverse('customer_info:organization-list'))

class OrganizationDelete(DeleteView):
    template_name = 'organizations/organization-delete.html'
    model = Organization
    success_url = '/organization-list'

class DepartmentDetail(DetailView):
    model = Department
    template_name = 'departments/department-detail.html'
    context_object_name = 'departments'

    # context_object_name = 'object_list'
    # queryset = Project.objects.filter(id=[])
    def test_func(self):
        return self.request.user.is_authenticated

    def get_object(self, queryset=None):
        return Customer.objects.filter(department__id=self.kwargs['pk']).order_by('birthdate')

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetail, self).get_context_data(**kwargs)
        context['users'] = self.get_object()
        context['department'] = Department.objects.get(id=self.kwargs['pk'])

        return context

class DepartmentCreate(TemplateView):
    template_name = 'departments/department-create.html'

    def get(self, request, *args, **kwargs):
        content = {}
        form = DepartmentForm
        packages = Package.objects.all()

        if Package.objects.filter(organization_package=self.kwargs['pk']).order_by('id'):
            organization_package = Organization.objects.values('package').get(id=self.kwargs['pk'])
            print('organization_package',organization_package)
            package_object = Package.objects.get(id=organization_package['package'])
            print('package_object',package_object)
            package = package_object

            store_package = []
            for package1 in packages:
                if package1 != package:
                    store_package.append(package1)
            context = {
            'form':form,
            'package':package,
            'store_package': store_package,
            }
            return render(request, 'departments/department-create.html', context)
        else:
            context={
            'form':form,
            'package':None,
            'store_package':Package.objects.all()
            }
            return render(request,self.template_name, context)


    def post(self, request, **kwargs):
        content = {}
        form = DepartmentForm(request.POST, request.FILES or None)
        # anniversary = request.POST['Anniversary']
        organization = Organization.objects.get(id=self.kwargs['pk'])
        

        package1=request.POST.get("package", None)
        print(package1)
        # if package1 != None:
        #     package = Package.objects.get(name=package1)
        # else:
        #     package=None
        try:
            package=Package.objects.get(name=package1)
        except:
            package=None

        # organization_package = Organization.objects.values('package').get(id=self.kwargs['pk'])
        # package_object = Package.objects.get(id=organization_package['package'])

        # try:
        #     package = Package.objects.get(id=form['package'].value())
        # except:
        #     package = package_object


        if form.is_valid():
            name=form.cleaned_data['name']
            contact_person=form.cleaned_data['contact_person']
            location=form.cleaned_data['location']
            contact_number=form.cleaned_data['contact_number']
            email=form.cleaned_data['email']

            Department.objects.create(name=name,
                                      contact_person=contact_person,
                                      location=location,
                                      contact_number=contact_number,
                                      organization=organization,
                                      package=package,
                                      email=email,
                                      )

            return HttpResponseRedirect('/organization/department/' + str(self.kwargs['pk']) + '/')
        else:
            content = {}
            form = form
            packages = Package.objects.all()

            if Package.objects.filter(organization_package=self.kwargs['pk']).order_by('id'):
                organization_package = Organization.objects.values('package').get(id=self.kwargs['pk'])
                print('organization_package',organization_package)
                package_object = Package.objects.get(id=organization_package['package'])
                print('package_object',package_object)
                package = package_object

                store_package = []
                for package1 in packages:
                    if package1 != package:
                        store_package.append(package1)
                context = {
                'form':form,
                'package':package,
                'store_package': store_package,
                }
                return render(request, 'departments/department-create.html', context)
            else:
                context={
                'form':form,
                'package':None,
                'store_package':Package.objects.all()
                }
                return render(request,self.template_name, context)


class DepartmentUpdate(TemplateView):
    template_name = 'departments/department-update.html'

    def get(self, request, *args, **kwargs):
        department = Department.objects.get(id=self.kwargs['pk'])
        form = DepartmentUpdateForm(instance=department)
        # organization = Organization.objects.get(department_organization=self.kwargs['pk'])
        store_package = []
        try:
            packages = Package.objects.all()
            package=Package.objects.get(department_package=self.kwargs['pk'])
            
            for package1 in packages:
                if package1 != package:
                    store_package.append(package1)
            context = {
            'form': form,
            
            'package':package,
            'store_package': store_package,
            }
            return render(request, self.template_name, context)
        except:
            context = {
            'form': form,
            'package':None,
            'store_package': Package.objects.all(),
            }
            return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = DepartmentUpdateForm(request.POST, request.FILES or None)
        # anniversary = request.POST['anniversary']
        package1 = request.POST['package']
        obj = Department.objects.get(id=self.kwargs['pk'])
        package = Package.objects.get(name=package1)
        try: 
            package1=package
        except:
            package1=None
        organization_id = Organization.objects.get(department_organization=self.kwargs['pk'])
        if form.is_valid():
            Department.objects.filter(id=obj.id).update(name=form.cleaned_data['name'],
                                                        contact_person=form.cleaned_data['contact_person'],
                                                        location=form.cleaned_data['location'],
                                                        contact_number=form.cleaned_data['contact_number'],
                                                        package=package1,
                                                        email=form.cleaned_data['email'],
                                                        )
            return HttpResponseRedirect('/organization/department/' + str(organization_id.id) + '/')

class DepartmentDelete(DeleteView):
    template_name = 'departments/department-delete.html'
    model = Department

    def get_success_url(self):

        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
        else:
            try:
                organization_id = Organization.objects.get(department_organization=self.kwargs['pk'])
                url = '/organization/department/' + str(organization_id.id) + '/'
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url

class EmployeeCreate(TemplateView):
    template_name= 'employee/employee-create.html'
    def get(self,request,*args,**kwargs):
        form=EmployeeForm
        department=Department.objects.get(id=self.kwargs['pk'])
        return render(request,self.template_name,{'form':form,'department':department})

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES or None)
        birthdate = request.POST.get('birthdate',None)
        if birthdate:
            parsed_date=parser.parse(birthdate)
        else:
            parsed_date=None
        if parsed_date is not None:
            parsed_date = parsed_date.strftime("%Y-%m-%d")
        else:
            parsed_date = None

        department = Department.objects.get(id=self.kwargs['pk'])
        if Package.objects.filter(department_package=self.kwargs['pk']).order_by('id'):
            department_package1 = Department.objects.values('package').get(id=self.kwargs['pk'])
            package = Package.objects.get(id=department_package1['package'])
            print('package',package)
        else:
            package=None
        
        if form.is_valid():

            Customer.objects.create(first_name=form.cleaned_data['first_name'],
                                      last_name=form.cleaned_data['last_name'],
                                      birthdate=parsed_date,
                                      package=package,
                                      contact_number=form.cleaned_data['contact_number'],
                                      email=form.cleaned_data['email'],
                                      designation=form.cleaned_data['designation'],
                                      department=department)

            return HttpResponseRedirect('/department/employee/' + str(department.id) + '/')

        department=Department.objects.get(id=self.kwargs['pk'])
        return render(request,'employee/employee-create.html',{'form':form,'department':department})

class EmployeeUpdate(UpdateView):

    template_name = 'employee/employee-update.html'
    form_class = EmployeeForm

    def get(self, request, *args, **kwargs):
        department = Department.objects.get(department_user__id=self.kwargs['pk'])
        obj = Customer.objects.get(id=self.kwargs['pk'])
        departmentform = EmployeeForm(instance=obj)
        packages = Package.objects.all()
        # package = Package.objects.get(user_package=self.kwargs['pk'])
        if Package.objects.filter(user_package=self.kwargs['pk']).order_by('id'):
            package = Package.objects.get(user_package=self.kwargs['pk'])
            package2=package
        else:
            package2=None
        store_package = []
        for package1 in packages:
            if package1 != package2:
                store_package.append(package1)
        return render(request, self.template_name, {'form': departmentform, 'department': department,
                                                    'user': obj,'store_package':store_package,'package':package2})

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES or None)
        birthdate = request.POST['birthdate']
        package1 = request.POST.get('package', None)
        print(package1)
        try:
            package = Package.objects.get(name=package1)
        except:
            package=None
        print("**************////",form['email'].value())
    
        parsed_date1 = parser.parse(birthdate)
        parse_date1 = parsed_date1.strftime("%Y-%m-%d")
        obj = Customer.objects.get(id=self.kwargs['pk'])
        department = Department.objects.get(department_user__id=self.kwargs['pk'])
        Customer.objects.filter(id=obj.id).update(first_name=form['first_name'].value(),
                                                         last_name=form['last_name'].value(),
                                                         birthdate=parse_date1,
                                                         package=package,
                                                         designation=form['designation'].value(),
                                                         department=department)
        return HttpResponseRedirect('/department/employee/' + str(department.id) + '/')

class EmployeeDelete(DeleteView):
    template_name = 'employee/employee-delete.html'
    model = Customer

    def get_success_url(self):

        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
        else:
            try:
                department = Department.objects.get(department_user__id=self.kwargs['pk'])
                url = '/department/employee/' + str(department.id) + '/'
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url

    















































	

