from django.conf.urls import url
from .views import BetList

urlpatterns = [
    url(r'^$', BetList.as_view(), name='bets_list'),
]
