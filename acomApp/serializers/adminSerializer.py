from rest_framework import serializers
from acomApp.models.user import bossAdmin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = bossAdmin
        fields = ['username', 'password', 'is_staff']
    
    def create(self, validated_data):
        adminInstance = bossAdmin.objects.create(**validated_data)
        return adminInstance
    
    def to_representation(self, obj):
        admin = bossAdmin.objects.get(id=obj.username)
        return {
                    'username': admin.username,
                    'password': admin.password,
                    'is_staff': admin.is_staff,
                }