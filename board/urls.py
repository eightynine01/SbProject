from django.urls import path

from board import views

urlpatterns = [
    # path('', views.IndexView, name='index'),
    path('add', views.board_write, name='add'),
    path('<int:pk>', views.board_detail),
    # path('<int:board_id>/')
    # path('<int:board_id>/')

]
