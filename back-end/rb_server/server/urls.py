from django.conf.urls import include, url
from django.contrib import admin
import settings
from misa import views as rb_views
from misa.views import login, register, register21
from misa.views import register22
from misa.views import run, Farest, public, publicd, Mine, resetPassword
from misa.views import search, up
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', rb_views.home, name='Home'),
    url(r'^Introduction/', rb_views.introduction),
    url(r'^News/', rb_views.news),
    url(r'^Resources/', rb_views.resources),
    url(r'^Sponsor/', rb_views.sponsor),
    url(r'^Login/',rb_views.loginpage),
    url(r'^Upload/',rb_views.uploadpage),
    url(r'^up', up),
    url(r'^search', search),
#    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),   # database admin
    url(r'^log/', login),                       # user login
    url(r'^register/', register),            # user register
    url(r'^register21/', register21),
    url(r'^register22/', register22),
#    url(r'^forgetpassword/', forgetpassword),
#    url(r'^runworld/', runworld),
 #   url(r'^setappointmentrun/', setAppointmentRun),
 #   url(r'^run/', run),
    url(r'^farest/', Farest),
#    url(r'^public/', public),
#    url(r'^public2/', publicd),
    url(r'^mine/', Mine),
#    url(r'^addfriends/', addFriends),
#    url(r'^addfriends2/', addFriends2),
#    url(r'^addfriends3/', addFriends3),
#    url(r'^addfriends4/', addFriends4),
    url(r'^resetPassword/', resetPassword),
#    url(r'^updateinfo/', update),
#    url(r'^myfriends/', MyFriends),
#    url(r'^getcount/', getCount),
#    url(r'^getTotalTime/', getTotalTime),
#    url(r'^getAvgSpeed/', getAvgSpeed),
#    url(r'^run/',run),
#    url(r'^sendtodo/',sendtodo),
#    url(r'^runrecord/', RunRecord),
#    url(r'^track/', track),

#    url(r'^setappointmentrun/', setAppointmentRun),
]

