from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path, include, re_path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
#    re_path(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
#    re_path(r'^accounts/logout/$', LogoutView.as_view(), LogoutView.next_page, name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),

]
