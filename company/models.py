from django.db import models
from django.utils import timezone
from django.urls import reverse

class Company(models.Model):
    INDUSTRY_CHOICES = (
        ('it','IT'),
        ('construction', 'CONSTRUCTION'),
        )
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING,)
    title = models.CharField(max_length=200)
    contact = models.CharField(max_length=12)
    email = models.EmailField()
    industrytype = models.CharField(max_length=50, choices=INDUSTRY_CHOICES,
                                    default='it')
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def get_absolute_url(self):
        return reverse("company_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title




class Department(models.Model):
    company = models.ForeignKey('company.Company', related_name='departments',on_delete=models.DO_NOTHING,)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def get_absolute_url(self):
        return reverse("company_list")

    def __str__(self):
        return self.text
