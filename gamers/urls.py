from django.conf.urls import url, include
import views
from django.utils.translation import ugettext

urlpatterns = [
    url(r'^Games/$', views.GamesList.as_view(), name=views.GamesList.name),
    url(r'^Games/(?P<pk>[0-9]+)$', views.GamesDetail.as_view(), name=views.GamesDetail.name),
    url(r'^Members/$', views.MembersList.as_view(), name=views.MembersList.name),
    url(r'^Members/(?P<pk>[0-9]+)$', views.MembersDetail.as_view(), name=views.MembersDetail.name),

    url(r'$', views.GameAdministration.as_view(), name=views.GameAdministration.name)
]
