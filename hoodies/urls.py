from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns= [
    url(r'^$',views.location, name="location"),
    url(r'(\d+)$',views.homm, name="home"),
    url(r'^register/', views.register, name="register"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^hoodies/', views.hood, name="hood"),
    url(r'^post',views.post,name="post"),
    url(r'^profile', views.profile, name ='profile'),
    url(r'^search/', views.search_business, name='search_results'),
    url(r'^profile/(?P<pk>\d+)', views.profile, name='profile'),
    url(r'^edit/',views.editprofile, name='edit'),
    url(r'^new/',views.update_index, name='new'),
    url(r'^biz/',views.biz, name='biz'),
    url(r'^activ',views.activ,name='activ')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
