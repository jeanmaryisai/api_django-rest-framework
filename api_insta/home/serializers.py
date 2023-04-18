from rest_framework.serializers import ModelSerializer
from .models import Stats

class StatsSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'
        read_only_fields = ('id',)