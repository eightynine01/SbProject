from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('$', IndexView.as_view(), name='index'),
    path('accounts/login/', auth_views.login),
    # , name='login', kwargs={'template_name': 'login.html'}
    path('accounts/logout/', auth_views.logout),
    # , name='logout', kwargs={ 'next_page': settings.LOGIN_URL, }
]
