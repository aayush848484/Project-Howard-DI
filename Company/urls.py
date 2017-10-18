from django.conf.urls import url

from Company import views

urlpatterns = [
    url(r'thank_you/$', views.thank_you, name= "Thank You"),
    url(r'^add_record/$', views.record, name='Record'),
    url(r'^read_records/$', views.readRecord, name='Read Record'),
    url(r'^(?P<company_id>[0-9]+)/$', views.readCompany, name='Read Company'),
    url(r'^$', views.index, name='Index'),
    url(r'^ranking_company/$', views.rankingCompany_details, name = "Ranking Company Details"),
    url(r'^company_and_ranking_company/$', views.companyAndRankingCompany, name= "Company And Ranking Company"),
    url(r'^search_result/(?P<rank_object>[0-9]+)/$', views.search_result, name = "Search Result")
]
