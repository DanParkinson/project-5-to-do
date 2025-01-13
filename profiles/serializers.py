from rest_framework import serializers
from .models import Profile 

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'profile_picture', 'name', 'bio', 'location', 'created_at', 'updated_at'
        ]