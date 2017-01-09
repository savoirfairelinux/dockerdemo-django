from django.conf.urls import include
from django.conf.urls import url


urlpatterns = [
    url('^', include('demo.public.note.urls', namespace='note')),
]
