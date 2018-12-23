from rest_framework import serializers
from .models import Pos_data

class PosdataSerializer(serializers.ModelSerializer):

	class Meta:
		model= Pos_data
		fields=['latpos','lonpos']