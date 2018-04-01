from django.conf.urls import url
from .views import MovieRentCreateApiView

urlpatterns = [
    url(r'^$', MovieRentCreateApiView.as_view(), name="movies-rent"),
]