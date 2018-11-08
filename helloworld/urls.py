# helloworld/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from helloworld import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view()),
    url(r'^account/$', views.AccountPageView.as_view()),
    url(r'^login/$', views.LoginPageView.as_view()),
    url(r'^meds/$', views.MedsPageView.as_view()),
    url(r'^request/$', views.RequestPageView.as_view()),
]
