from rest_framework import viewsets
from .models import News, Teacher
from .serializers import NewsSerializer, TeacherSerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    # ReadOnlyModelViewSet означає, що через API можна тільки читати новини, 
    # а створювати - тільки через адмінку (безпека!)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer