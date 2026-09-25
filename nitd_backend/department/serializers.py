from rest_framework import serializers
from .models import (
    News, NewsImage, Teacher, Schedule, Course, 
    Conference, Olympiad, Textbook, Curator, 
    EduSection, EduGroup, EduLink, EduImage,
    ProgramFeedback, GalleryItem
)

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
        fields = ['id', 'first_name', 'last_name', 'patronymic', 'degree', 'position', 'bio', 'photo', 'github', 'linkedin']

class ScheduleSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ['id', 'course_id', 'status', 'day', 'timeStart', 'timeEnd', 'subject', 'type', 'teacher', 'room', 'link', 'subgroup']

    def get_teacher(self, obj):
        if obj.teacher:
            return f"{obj.teacher.last_name} {obj.teacher.first_name}"
        if obj.external_teacher:
            return obj.external_teacher
        return "Викладач не вказаний"

# --- НОВІ СЕРІАЛІЗАТОРИ ---

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ['id', 'title', 'content', 'photo', 'link', 'date_held']

class OlympiadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olympiad
        fields = ['id', 'title', 'content', 'photo', 'link', 'date_held']

class TextbookSerializer(serializers.ModelSerializer):
    # Створюємо зручне поле, яке об'єднає авторів з кафедри і сторонніх
    authors_list = serializers.SerializerMethodField()

    class Meta:
        model = Textbook
        fields = ['id', 'title', 'description', 'cover_image', 'link', 'publication_year', 'authors_list']

    def get_authors_list(self, obj):
        # Збираємо прізвища викладачів кафедри (напр. "Герасименко О.Ю.")
        authors = [f"{t.last_name} {t.first_name[0]}." for t in obj.teachers.all()]
        
        # Додаємо зовнішніх авторів, якщо вони є
        if obj.external_authors:
            authors.append(obj.external_authors)
            
        return ", ".join(authors) if authors else "Автори не вказані"

class CuratorSerializer(serializers.ModelSerializer):
    # Витягуємо людську назву курсу (напр. "1 Курс" замість "c1")
    course_name = serializers.CharField(source='get_course_display', read_only=True)
    # Зручне форматування ПІБ викладача
    teacher_name = serializers.SerializerMethodField()
    # Можемо також передати фото куратора
    teacher_photo = serializers.ImageField(source='teacher.photo', read_only=True)

    class Meta:
        model = Curator
        fields = ['id', 'course', 'course_name', 'group_name', 'teacher_name', 'teacher_photo']

    def get_teacher_name(self, obj):
        return f"{obj.teacher.last_name} {obj.teacher.first_name} {obj.teacher.patronymic}".strip()

class LinkSer(serializers.ModelSerializer):
    href = serializers.SerializerMethodField()
    class Meta:
        model = EduLink
        fields = ("id", "title", "note", "href")
    def get_href(self, o):
        if o.file:
            return self.context["request"].build_absolute_uri(o.file.url)
        return o.url

class GroupSer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = EduGroup
        fields = ("id", "title", "links")
    def get_links(self, o):
        qs = o.links.filter(is_published=True)
        return LinkSer(qs, many=True, context=self.context).data

class ImageSer(serializers.ModelSerializer):
    class Meta:
        model = EduImage
        fields = ("id", "image", "caption")

class SectionSer(serializers.ModelSerializer):
    groups = GroupSer(many=True)
    images = ImageSer(many=True)
    class Meta:
        model = EduSection
        fields = ("id", "title", "slug", "intro", "show_in_menu", "groups", "images")

class ProgramFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramFeedback
        fields = ['name', 'email', 'message']

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        # Віддаємо тільки потрібні поля (is_published фронтенду знати не обов'язково)
        fields = ['id', 'title', 'image', 'category', 'created_at']