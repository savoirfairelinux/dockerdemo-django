from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.NoteCreateView.as_view(), name='create'),
]
