from django import forms

class NameForm(forms.Form):
    rankingCompanyName = forms.CharField(max_length= 100)
    sourceOfData = forms.CharField(max_length=100)
    numberOfCompaniesRanked = forms.IntegerField()

class CompanyRankForm(forms.Form):
    name = forms.CharField(max_length=100)
    rank = forms.IntegerField()
    employeeCount = forms.IntegerField()


class SearchForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    ranking_company_name = forms.CharField(max_length=100)

