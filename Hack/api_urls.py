from django.conf.urls import url,include
from rest_framework_swagger.views import get_swagger_view

api_docs = get_swagger_view('Extorsion API')

urlpatterns = [
    url(r'^extorsion/', include('modules.Publicaciones.urls_api')),
    url(r'^docs/', api_docs),
]