from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Company, CompanyRanking, RankingCompany, CompanyForm, RankingCompanyForm, CompanyRankingForm
from django.views.generic.base import TemplateView


def index(request):
    number_of_companies = Company.objects.all().count()
    for company in Company.objects.all():
        company.score = 0
        company.save()
        for company_ranking in CompanyRanking.objects.filter(company=company):
            if company_ranking.rank != 0:
                company.score += ((number_of_companies + 1) - company_ranking.rank)
                company.save()
    company_rankings_final = sorted(Company.objects.all(), key=lambda company: company.score)[::-1]
    for individual_company in company_rankings_final:
        individual_company.final_rank = company_rankings_final.index(individual_company) + 1
        individual_company.save()
    context = {'company_rankings_final': company_rankings_final}
    return render(request, 'Company/templates/index.html', context)


def readRecord(request):
    return render(request, 'Company/templates/read_record.html')

def record(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            newRankingCompany = RankingCompany(form)
            newRankingCompany.save()
    else:
        form = CompanyForm()
    return render(request, 'Company/templates/add_record.html', {'form': form})


def readCompany(request, company_id):
    company_details = dict()
    a = CompanyRanking.objects.filter(company=company_id)
    company_name = Company.objects.get(id = company_id).name
    for each_record in a:
        company_details[each_record.rankingCompany.name] = (each_record.rankingCompany.id, each_record.rank)
    context = {'company_name': company_name,
               'company_details': company_details}
    return render(request, 'Company/templates/company_details.html', context)

def rankingCompany_details(request):
    rankings_company = RankingCompany.objects.all()
    context = {'rankings_company': rankings_company}
    return render(request, 'Company/templates/ranking_company_details.html', context)

def rankingCompanyIndividualRankings(request, ranking_company_id):
    companies_ranked = CompanyRanking.objects.filter(rankingCompany__id=ranking_company_id)
    return_dict = dict()
    ranking_company_name = RankingCompany.objects.get(id = ranking_company_id).name
    for individual_companies in companies_ranked:
        return_dict[Company.objects.get(id=individual_companies.company_id)] = individual_companies.rank
    context = {
        'ranking_company_name': ranking_company_name,
        'return_dict': return_dict
    }
    return render(request, 'Company/templates/ranking_company_ranking.html', context)

def search_result(request, rank_object):
    return render(request, 'Company/templates/search_result.html', {'rank_object': rank_object})

def companyAndRankingCompany(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            a = CompanyRanking.objects.filter(company__name=form.cleaned_data['company_name'],
                                              rankingCompany__name=form.cleaned_data['ranking_company_name'])
            if not a:
                return render(request, 'Company/templates/invalid_search.html')
        for x in a:
            rank_object = x.rank
        return HttpResponseRedirect('/company/search_result/' + str(rank_object) + '/')
    else:
        form = SearchForm()
    return render(request, 'Company/templates/company_and_ranking_company.html', {'form': form})

class ConfirmationPage(TemplateView):
    template_name = 'Company/templates/thank_you.html'