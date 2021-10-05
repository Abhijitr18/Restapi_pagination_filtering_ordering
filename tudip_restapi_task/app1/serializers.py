from rest_framework import serializers
from .models import Candidate


class Candidate_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
