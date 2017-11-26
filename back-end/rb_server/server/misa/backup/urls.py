from django.conf.urls import include, url
from django.contrib import admin
import settings
from runningbear import views as rb_views
from runningbear.views import login, register_new_user, register2, forget_pwd, runworld, set_apt_run
from runningbear.views import myrun, farest, public, competition, tips, mine
from runningbear.views import history, add_friends, reset_pwd, update_info, myfriends
from runningbear.views import upload_user_photo,search, get_account_info
from runningbear.views import logout,public_act, edit_sex, edit_user_label
from runningbear.views import push, reset_all_image, getact, getCompleted
from runningbear.views import getUnCompleted,join_act, unjoin_act, com_act
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', rb_views.home, name='home'),
#    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),   # database admin
    url(r'^login/', login),                       # user login
    url(r'^register/', register_new_user),            # user register
    url(r'^register2/', register2),
    url(r'^forgetpassword/', forget_pwd),
    url(r'^runworld/', runworld),
    url(r'^setappointmentrun/', set_apt_run),
    url(r'^myrun/', myrun),
    url(r'^farest', farest),
    url(r'^public', public),
    url(r'^competition', competition),
    url(r'^tips', tips),
    url(r'^mine', mine),
    url(r'^history', history),
    url(r'^addfriends', add_friends),
    url(r'^resetpassword', reset_pwd),
    url(r'^updateinfo', update_info),
    url(r'^myfriends', myfriends),
	
	
#    url(r'^push', push),                         # user push data
    url(r'^photo_upload/', upload_user_photo),   #user upload photo
    url(r'^media/(?P<path>.*)$', serve, {
                'document_root': settings.MEDIA_ROOT }),
    url(r'^getinfo/', get_account_info),
    url(r'^logout/', logout),
    url(r'^public/', public_act),
    url(r'^edit_sex/', edit_sex),
    url(r'^edit_label/', edit_user_label),
    url(r'^push/', push),
    url(r'^reset/', reset_all_image),
    url(r'^query/',search),
    url(r'^getact/', getact),
    url(r'^complete/', getCompleted),
    url(r'^uncomplete', getUnCompleted),
    url(r'^join',join_act),
    url(r'^unjoin',unjoin_act),
    url(r'^comact',com_act),
]

