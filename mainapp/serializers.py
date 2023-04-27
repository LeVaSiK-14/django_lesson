from rest_framework import serializers

from mainapp.models import(
    School, Clas, Student,
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id', 'first_name', 'last_name', 'email',
            'age', 'clas',
        )


class ClasSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True) # nested serializer
    class Meta:
        model = Clas
        fields = (
            'id', 'room_number', 'teacher_name', 'student_amount',
            'grade', 'school', 'students', 
        )


class SchoolSerializer(serializers.ModelSerializer):
    classes = ClasSerializer(read_only=True, many=True) # nested serializer
    class Meta:
        model = School
        fields = (
            'clas_amount',
            'id', 'name', 'number', 'address', 'classes',
        )





