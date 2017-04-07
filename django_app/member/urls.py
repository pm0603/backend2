from django.conf.urls import url

from member import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^signup/$', views.SignUp.as_view()),
    url(r'^logout/$', views.Logout.as_view()),
    url(r'^fblogin/$', views.FacebookLogin.as_view()),
    url(r'^activate/(?P<hash>.*)/$', views.UserActivate.as_view()),

]
