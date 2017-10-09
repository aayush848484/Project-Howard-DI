from django.conf.urls import url

from Company import views

urlpatterns = [
    url(r'^add_record/$', views.record, name='Record'),
    url(r'^read_records/$', views.readRecord, name='Read Record'),
    url(r'^(?P<company_id>[0-9]+)/$', views.readCompany, name='Read Company'),
    url(r'^$', views.index, name='Index'),
    url(r'^ranking_company/', views.rankingCompany_details, name = "Ranking Company Details"),
    url(r'^company_and_ranking_company', views.companyAndRankingCompany, name= "Company And Ranking Company")
]
