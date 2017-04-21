from django.conf.urls import url

from member import views
from rest_framework.authtoken import views as token_views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^signup/$', views.SignUp.as_view()),
    url(r'^logout/$', views.Logout.as_view()),
    url(r'^fblogin/$', views.FacebookLogin.as_view()),
    url(r'^activate/(?P<hash>.*)/$', views.UserActivate.as_view()),
    url(r'^password/change/$', views.PasswordChange.as_view()),
    url(r'^detail/(?P<username>[a-zA-Z0-9_.-]+)/$', views.UserDetail.as_view()),

    # user의 토큰 값을 확인하기 위한 url설정 - 최영민
    url(r'^api-token-auth/', token_views.obtain_auth_token),
]
