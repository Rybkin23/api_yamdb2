from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, SignUpView, TitleViewSet, TokenView,
                    UsersViewSet)

VERSION = 'v1'

v1_router = DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
v1_router.register(r'titles/(?P<title_id>\d+)\/reviews',
                   ReviewViewSet, basename='reviews')
v1_router.register(r'users', UsersViewSet)
v1_router.register(r'titles', TitleViewSet, basename='titles')
v1_router.register(r'categories', CategoryViewSet, basename='categories')
v1_router.register(r'genres', GenreViewSet, basename='genres')

auth_patterns = [
    path('signup/', SignUpView.as_view()),
    path('token/', TokenView.as_view()),

]

urlpatterns = [
    path(f'{VERSION}/', include(v1_router.urls)),
    path(f'{VERSION}/auth/', include(auth_patterns)),
]
