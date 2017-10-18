from django import forms

class NameForm(forms.Form):
    company_name = forms.CharField(label="Company Name", max_length= 100)
    employee_count = forms.IntegerField(label="Number of Empoyees")
    score = forms.IntegerField(label = "Total Score")

class SearchForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    ranking_company_name = forms.CharField(max_length=100)

