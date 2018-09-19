from django.urls import path
from django.conf.urls import url

from .djangoapps.sample import views as SampleViews
from .djangoapps.login import views as LoginViews
from .djangoapps.logout import views as LogoutViews
from .djangoapps.test import views as TestViews

urlpatterns = [
    # main-url
    url('sample$', SampleViews.sample, name='sample'),

    url('login$', LoginViews.login, name='login'),
    url('logout$', LogoutViews.logout, name='logout'),

    url('test$', TestViews.test, name='test'),
    url('api_bat$', TestViews.api_bat, name='api_bat'),
]
