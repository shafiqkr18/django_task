from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.DashboardView.as_view(),name='dashboard'),
    url(r'^companylist/$',views.CompanyListView.as_view(),name='company_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^company/(?P<pk>\d+)$', views.CompanyDetailView.as_view(), name='company_detail'),
    url(r'^company/new/$', views.CreateCompanyView.as_view(), name='company_new'),
    url(r'^company/(?P<pk>\d+)/remove/$', views.CompanyDeleteView.as_view(), name='company_remove'),
    url(r'^company/(?P<pk>\d+)/publish/$', views.company_publish, name='company_publish'),
    url(r'^company/(?P<pk>\d+)/department/$', views.add_department_to_company, name='add_department_to_company'),
    url(r'^department/(?P<pk>\d+)/approve/$', views.department_approve, name='department_approve'),
    url(r'^department/(?P<pk>\d+)/remove/$', views.department_remove, name='department_remove'),
]
