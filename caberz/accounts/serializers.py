from accounts.models import Profiles,Driver,Journey
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profiles
        fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profiles
        fields=('mobile',)

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profiles
        fields=('otp',)


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model=Journey
        fields='__all__'

        
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driver
        #fields='__all__'
        fields=('first_name','last_name','mobile','car','license_no','ownership_no')

class DriverMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driver
        fields=('mobile',)

class DriverOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driver
        fields=('otp',)
        
