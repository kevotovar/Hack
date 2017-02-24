from django.conf.urls import url,include
from rest_framework_swagger.views import get_swagger_view

api_docs = get_swagger_view('Extorsion API')

urlpatterns = [
    url(r'^extorsion/', include('modules.Extorsion.urls')),
    url(r'^docs/', api_docs),
]