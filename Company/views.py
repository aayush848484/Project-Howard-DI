from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from Company.models import Company, CompanyRanking, RankingCompany
from Company.forms import NameForm

# Create your views here.

def index(request):
    number_of_companies = Company.objects.all().count()
    for company in Company.objects.all():
        company.score = 0
        company.save()
        for company_ranking in CompanyRanking.objects.filter(company = company):
            if company_ranking.rank != 0:
                company.score += ((number_of_companies + 1) - company_ranking.rank)
                company.save()
    company_rankings_final = sorted(Company.objects.all(), key=lambda company: company.score)[::-1]
    for individual_company in company_rankings_final:
        individual_company.final_rank = company_rankings_final.index(individual_company)+1
        individual_company.save()
    context = {'company_rankings_final': company_rankings_final}
    return render(request, 'Company/templates/index.html', context)

def readRecord(request):
    return render(request, 'Company/templates/read_record.html')

def record(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            Company.objects.create(
                name = request.POST.get('company_name'),
                employee_count = request.POST.get('employee_count'),
                score = request.POST.get('score')
            )
            #  Process the data.
            return HttpResponseRedirect('company/thank_you/')
        #  Use the data returned back from the user and store it in the database.
    else:
        form = NameForm()
    return render(request, 'Company/templates/add_record.html', {'form': form})

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

def thank_you(request):
    return render(request, 'Company/templates/thank_you.html')

"""
def rankingCompany_details(request, ranking_company_name):
    ranking_company_details = get_object_or_404(RankingCompany, name = ranking_company_name)
    ranking_company_details.companies.all()
    context = {'ranking_company_details': ranking_company_details}
    return render(request, 'Company/templates/ranking_company_details.html', context)
"""
