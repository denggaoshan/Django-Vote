
from django.conf.urls import url
from django.contrib import admin


from base import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^login.html$', views.login, name = 'login'),
    url(r'^logout.html$', views.logout, name = 'logout'),
    url(r'^register.html$', views.register , name = 'register'),
    url(r'^polls/votes.html$', views.votes, name = 'polls'),
    url(r'^polls/(?P<vote_id>[0-9]+)/detail$', views.vote_detail, name = 'voteDetail'),
    url(r'^admin/', admin.site.urls),
]
