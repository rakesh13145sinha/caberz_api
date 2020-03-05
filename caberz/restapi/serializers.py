from accounts.models import Profiles
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profiles
        fields='__all__'