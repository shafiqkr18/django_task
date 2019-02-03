from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from company.models import Company, Department
from django.utils import timezone
from company.forms import CompanyForm, DepartmentForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(TemplateView):
    template_name = 'about.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'


class CompanyListView(ListView):
    model = Company

    def get_queryset(self):
        return Company.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class CompanyDetailView(DetailView):
    model = Company


class CreateCompanyView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'company/company_detail.html'

    form_class = CompanyForm

    model = Company


class CompanyDeleteView(LoginRequiredMixin,DeleteView):
    model = Company
    success_url = reverse_lazy('company_list')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def company_publish(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.publish()
    return redirect('company_detail', pk=pk)

@login_required
def add_department_to_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.company = company
            department.save()
            return redirect('company_detail', pk=company.pk)
    else:
        form = DepartmentForm()
    return render(request, 'company/department_form.html', {'form': form})


@login_required
def department_approve(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.approve()
    return redirect('company_detail', pk=department.company.pk)

@login_required
def department_remove(request, pk):
    department = get_object_or_404(Department, pk=pk)
    company_pk = department.company.pk
    department.delete()
    return redirect('company_detail', pk=company.pk)
