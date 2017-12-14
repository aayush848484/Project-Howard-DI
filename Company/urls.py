from django.conf.urls import url

from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'thank_you/$', views.ConfirmationPage.as_view(), name= "Thank You"),
    url(r'^add_record/$', views.record, name='Add Record'),
    url(r'^read_records/$', views.readRecord, name='Read Record'),
    url(r'^(?P<company_id>[0-9]+)/$', views.readCompany, name='Read Company'),
    url(r'^$', views.index, name='Index'), # Done
    url(r'^ranking_company/$', views.rankingCompany_details, name = "Ranking Company Details"),
    url(r'^ranking_company/(?P<ranking_company_id>[0-9]+)/$', views.rankingCompanyIndividualRankings,
        name="Ranking Company Details"),
    url(r'^company_and_ranking_company/$', views.companyAndRankingCompany, name= "Company And Ranking Company"),
    url(r'^search_result/(?P<rank_object>[0-9]+)/$', views.search_result, name = "Search Result")
]
