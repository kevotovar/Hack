from .models import Extorsion
from .serializer import ExtorsionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# Create your views here.
class ExtorsionList(generics.ListCreateAPIView):
    queryset = Extorsion.objects.all()
    serializer_class = ExtorsionSerializer