from django.db import models
from django.forms.models import ModelForm
from django.urls.base import reverse


class Company(models.Model):
    name = models.CharField(max_length=100,
                            help_text= 'Enter the name of the company',
                            verbose_name= 'Company Name')
    employee_count = models.IntegerField(blank=False,
                                         help_text='Total Employees in the company',
                                         verbose_name='Employee Count')
    score = models.IntegerField(blank=True,
                                default=0)
    final_rank = models.IntegerField(blank=True,
                                     default=0)
    """
    image = models.ImageField(verbose_name='Logo of the company',
                              width_field=600,
                              height_field=600,
                              help_text= 'Upload a 600x600 pixel logo of the company.',
                              blank=True,
                              default=None)
    """

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Read Company', args=[str(self.id)])


class RankingCompany(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Enter the name of the Ranking Company',
                            verbose_name='Ranking Company Name')
    source = models.CharField(max_length=200,
                              default='Anonymous',
                              verbose_name='Source of Data')
    count = models.IntegerField(verbose_name= 'Number of Companies Ranked',
                                help_text='Equal to lowest company ranked.')
    """
    image = models.ImageField(verbose_name='Logo of the Ranking Company',
                              width_field=600,
                              height_field=600,
                              help_text= 'Upload a 600x600 pixel logo of the Ranking Company.',
                              blank=True,
                              default=None)
    """
    companies = models.ManyToManyField(
        Company,
        through='CompanyRanking'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Ranking Company Details', args = [str(self.id)])


class CompanyRanking(models.Model):
    company = models.ForeignKey(Company,
                                on_delete= models.CASCADE)
    rankingCompany = models.ForeignKey(RankingCompany,
                                       on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.company.name + "_" + self.rankingCompany.name

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'employee_count']

class RankingCompanyForm(ModelForm):
    class Meta:
        model = RankingCompany
        fields = ['name', 'count', 'source', 'companies']

class CompanyRankingForm(ModelForm):
    class Meta:
        models = CompanyRanking
        fields = ['company', 'rankingCompany']
