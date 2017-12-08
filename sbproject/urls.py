from django.contrib import admin

from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from sb.views import IndexView

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('boards/', include('board.urls')),
    path('/', include('sb.urls')),
    path('swag/', schema_view),
    path('admin/', admin.site.urls),
]
