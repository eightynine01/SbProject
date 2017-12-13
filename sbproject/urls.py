from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from board import views


router = routers.DefaultRouter()
router.register('boardDetails', views.BoardDetailsViewSet)
router.register('boardList', views.BoardListViewSet)


urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('boards/', include('board.urls')),
    path('/', include('sb.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
