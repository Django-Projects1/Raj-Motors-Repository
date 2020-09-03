"""Raj_Motors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from testapp import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.list_view),
    url(r'contact/$',views.contact_view),
    url(r'founder/$',views.founder_view),
    url(r'^detail/(?P<id>\d+)/$',views.detail_view),
    url(r'^specifications/(?P<id>\d+)/$',views.specifications_view),
    url(r'^variants/(?P<id>\d+)/$',views.variants_view),
    url(r'^emi/(?P<id>\d+)/$',views.calculate_emi_view),
    url(r'^features/(?P<id>\d+)/$',views.features_view),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url('^accounts/logout',views.logout_view),
    url(r'^signup/',views.signup_view),
    url(r'^send_mail/',views.send_mail_view),
    url(r'^genuine/$',views.genuine_view),
    url(r'^other/(?P<id>\d+)/$',views.other_relate_parts_view),
    url(r'^genuine_relate/(?P<id>\d+)/$',views.genuine_relate_view),
    url(r'info/(?P<id>\d+)/$',views.genuine_relate_info_view),
    url(r'hel_floorinfos/(?P<id>\d+)/$',views.Hel_floor_parts_info_view),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
