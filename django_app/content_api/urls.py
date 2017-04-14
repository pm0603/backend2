from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from content_api import views
from . import open_api

router = DefaultRouter()
router.register(r'api', views.ContentViewSet)
router.register(r'comment', views.CommentViweSet, base_name='com')

urlpatterns = [
    # 지역별 검색 DB 추가
    url(r'db_save_area/', open_api.Area.as_view()),
    # 분야별 검색 DB 추가
    url(r'db_save_genre/', open_api.Genre.as_view()),
    # 라우터 루트
    url(r'^', include(router.urls)),
]
