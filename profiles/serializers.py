from rest_framework import serializers
from .models import Profile 

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user



    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'profile_picture', 'name', 'bio', 'location', 'created_at', 'updated_at', 'is_user'
        ]