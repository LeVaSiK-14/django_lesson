from rest_framework.viewsets import ModelViewSet

from mainapp.models import (
    School, Clas, Student,
)

from mainapp.serializers import(
    SchoolSerializer,
    ClasSerializer,
    StudentSerializer
)


class SchoolView(ModelViewSet):
    queryset = School.objects.all() # select * from school;
    serializer_class = SchoolSerializer


class ClasView(ModelViewSet):
    queryset = Clas.objects.all() # select * from school;
    serializer_class = ClasSerializer


class StudentView(ModelViewSet):
    queryset = Student.objects.all() # select * from school;
    serializer_class = StudentSerializer








    