from django.conf.urls import url
from .views import MovieRentCreateApiView,MovieRentUpdateApiView

urlpatterns = [
    url(r'^$', MovieRentCreateApiView.as_view(), name="movies-rent-createlist"),
    url(r'^(?P<id>\d+)/$', MovieRentUpdateApiView.as_view(), name="movies-rent-update"),
]