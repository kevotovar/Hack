from rest_framework import serializers
from .models import Extorsion

class ExtorsionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Extorsion
        fields = '__all__'