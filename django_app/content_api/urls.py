from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from content_api import views
from content_api.bookmark_views import BookmarkCreateView, BookmarkDeleteView, BookmarkListView
from . import open_api

# 뷰셋 라우터 설정 - 김도경
router = DefaultRouter()
router.register(r'_content', views.ContentViewSet)
router.register(r'_comment', views.CommentViweSet)

urlpatterns = [
    # 지역별 검색 DB 추가 - 김도경
    url(r'db_save_area/', open_api.Area.as_view()),
    # 분야별 검색 DB 추가 - 김도경
    url(r'db_save_genre/', open_api.Genre.as_view()),
    # 라우터 루트 - 김도경
    url(r'^', include(router.urls)),

    # 아래 url은 user쪽으로 옮김 - 최영민
    url(r'bookmark/list', BookmarkListView.as_view()),

    # Bookmark 관련 url 설정 - 최영민
    url(r'bookmark/create', BookmarkCreateView.as_view()),
    url(r'bookmark/delete', BookmarkDeleteView.as_view()),
]

# 테스트시 임시 로그인 경로
urlpatterns += [
    url(r'^_auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]