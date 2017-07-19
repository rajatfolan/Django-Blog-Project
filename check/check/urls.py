"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blogapp.views import *
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import password_reset , password_reset_done,password_reset_confirm,password_reset_complete
#from django.contrib.auth.views import login , logout

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$',home,name='home'),
    url(r'^accounts/login/$',login,name='login'),
    url(r'^accounts/auth/$',auth_view,name='check'),
    url(r'^accounts/logout/$',logout,name='logout'),
    url(r'^accounts/loggedin/$',loggedin,name='loggedin'),
    url(r'^accounts/invalid/$',invalid_login,name='invalid'),
    url(r'^accounts/register/$',register,name='register'),
    url(r'^accounts/loggedin/blogs/$',blog_post,name='blog'),
    url(r'^accounts/loggedin/blogs/delete/(\d+)/$',delete,name='delete'),
    url(r'^accounts/loggedin/blogs/edit/(\d+)/$',edit,name='edit'),
    url(r'^accounts/loggedin/detail/$',detail,name='detail'),
    url(r'^reset-password/$',password_reset,name='reset_password'),
    url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,name='password_reset_confirm'),
    url(r'^reset-password/complete/$',password_reset_complete,name='password_reset_complete'),
    url(r'^accounts/loggedin/detail/password-change$',password_change,name='password-change'),

]


#urlpatterns +=staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
