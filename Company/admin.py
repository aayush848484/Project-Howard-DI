from django.contrib import admin
from .models import Company, CompanyRanking, RankingCompany

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyRanking)
admin.site.register(RankingCompany)
