from rest_framework import serializers
from .models import News, NewsImage, Teacher

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['id', 'image']

class NewsSerializer(serializers.ModelSerializer):
    # Підключаємо галерею. many=True означає, що фото може бути кілька
    images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'date_posted', 'is_pinned', 'order', 'images']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'degree', 'position', 'bio', 'photo', 'github', 'linkedin']