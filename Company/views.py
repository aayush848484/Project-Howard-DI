from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from Company.models import Company, CompanyRanking, RankingCompany


# Create your views here.

def index(request):
    company_rankings_final = Company.objects.all()
    context = {'company_rankings_final': company_rankings_final}
    return render(request, 'Company/templates/index.html', context)

def readRecord(request):
    return render(request, 'Company/templates/read_record.html')

def record(request):
    return render(request, 'Company/templates/add_record.html')

def readCompany(request, company_id):
    #  Retrieve all the records of the company useing the company ID.
    #  Send it to the html file which will render it.
    company_details = Company.objects.get(pk = company_id)
    context = {'company_details': company_details}
    return render(request, 'Company/templates/company_details.html', context)

def rankingCompany_details(request):
    return render(request, 'Company/templates/ranking_company_details.html')

def companyAndRankingCompany(request):
    return render(request , 'Company/templates/company_and_ranking_company.html')

"""
def rankingCompany_details(request, ranking_company_name):
    ranking_company_details = get_object_or_404(RankingCompany, name = ranking_company_name)
    ranking_company_details.companies.all()
    context = {'ranking_company_details': ranking_company_details}
    return render(request, 'Company/templates/ranking_company_details.html', context)
"""
