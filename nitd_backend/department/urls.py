from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]