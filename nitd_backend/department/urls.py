from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NewsViewSet, TeacherViewSet, ScheduleViewSet, ConferenceViewSet,
    OlympiadViewSet, TextbookViewSet, CuratorViewSet, EduSectionList,
    ProgramFeedbackCreateView, GalleryItemListView
)

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'schedule', ScheduleViewSet)
router.register(r'conferences', ConferenceViewSet)
router.register(r'olympiads', OlympiadViewSet)
router.register(r'textbooks', TextbookViewSet)
router.register(r'curators', CuratorViewSet)

urlpatterns = [
    path('education/', EduSectionList.as_view()),
    path('', include(router.urls)),
    path('edu-sections/', EduSectionList.as_view(), name='edu-sections'),
    path('feedback/', ProgramFeedbackCreateView.as_view(), name='program-feedback'),
    path('gallery/', GalleryItemListView.as_view(), name='gallery-items'),
]