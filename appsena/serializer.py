from rest_framework import serializers
from .models import report

class reportSerializers(serializers.ModelSerializer):
    class Meta:
        model = report
        fields = '__all__'