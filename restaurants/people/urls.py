from django.urls import path, re_path
from .views import createPerson, personDetail

urlpatterns = [
    path('people/', createPerson),
    re_path(r'^people/(?P<iin>([0-9]){12})?/', personDetail), 
]
