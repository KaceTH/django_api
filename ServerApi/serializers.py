from rest_framework import serializers

from .models import StudentUser

class StudentUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentUser
        fields = [
            'user_id',
            'user_pw',
            'name',
            'phone_number',
            'email',
            'grade_number',
            'class_number',
            'student_number'
        ]