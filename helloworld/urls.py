# helloworld/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from helloworld import views

urlpatterns = [
    url(r'^$', views.homePage,name="index"),
    url(r'^contact/$', views.contactPage,name="contact"),
    url(r'^account/$', views.accountPage,name="account"),
    url(r'^login/$', views.loginPage,name="login"),
    url(r'^register/$', views.registerPage,name="login"),
    url(r'^meds/$', views.medsPage,name="medicamentos"),
    url(r'^request/$', views.requestPage,name="solicitud"),
    url(r'^login/iniciar/$',views.login_iniciar,name="iniciar"),
    url(r'^register/createUser/$',views.createUser, name="create_user"),
    url(r'^register/editUser/$',views.editUser, name="edit_user"),
    url(r'^register/creditCard/$',views.card_register, name="credit_card_register"),
    url(r'^register/editCard/$',views.card_edit, name="credit_card_edit"),
    url(r'^cerrarsesion/$',views.cerrar_session,name="cerrar_session"),
    url(r'^delete/meds/(?P<pk>\d+)/$',views.delete_meds,name="delete_meds"),
    url(r'^delete/cards/(?P<pk>\d+)/$',views.delete_card,name="delete_card"),

]
