from rest_framework import serializers
from acomApp.models.user import Supervisorpsm


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisorpsm
        fields = ['type', 'username', 'email', 'first_names', 'last_names', 'birth_date', 'type_identification', 'identification_num', 'password', 'testResult', 'isActive']
    
    def create(self, validated_data):
        userInstance = Supervisorpsm.objects.create(**validated_data)
        return userInstance
    
    def to_representation(self, obj):
        user = Supervisorpsm.objects.get(id=obj.username)
        return {
                    'id': user.id,            
                    'type': user.type,
                    'username': user.username,
                    'email': user.email,
                    'first_names': user.first_names,
                    'last_names': user.last_names,
                    'type_identification': user.type_identification, 
                    'identification_num': user.identification_num,
                    'birth_date': user.birth_date, 
                    'password': user.password,
                    'testResult': user.testResult,
                    'isActive': user.isActive
                }