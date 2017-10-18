from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    employee_count = models.IntegerField()
    score = models.IntegerField(default=0)
    final_rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class RankingCompany(models.Model):
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=200)
    count = models.IntegerField()
    companies = models.ManyToManyField(
        Company,
        through='CompanyRanking'
    )

    def __str__(self):
        return self.name


class CompanyRanking(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    rankingCompany = models.ForeignKey(RankingCompany, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)


