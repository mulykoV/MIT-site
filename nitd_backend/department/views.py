from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import News, Teacher, Schedule, Conference, Olympiad, Textbook, Curator, EduSection
from .serializers import (NewsSerializer, TeacherSerializer, ScheduleSerializer, ConferenceSerializer,
                          OlympiadSerializer, TextbookSerializer, CuratorSerializer, SectionSer)


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    # ReadOnlyModelViewSet означає, що через API можна тільки читати новини, 
    # а створювати - тільки через адмінку (безпека!)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ConferenceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class OlympiadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Olympiad.objects.all()
    serializer_class = OlympiadSerializer

class TextbookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer

class CuratorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer

class EduSectionList(ListAPIView):
    serializer_class = SectionSer
    pagination_class = None

    def get_queryset(self):
        return (EduSection.objects.filter(is_published=True)
                .prefetch_related("groups__links", "images"))