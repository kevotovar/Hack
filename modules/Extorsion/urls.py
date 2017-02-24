from django.conf.urls import url,include
from .views import ExtorsionList

urlpatterns = [
    url(r'^extorsion/$', ExtorsionList.as_view()),
]