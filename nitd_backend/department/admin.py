from django.contrib import admin
from .models import Teacher, Course, News, NewsImage

# Це дозволяє додавати фотографії прямо на сторінці створення новини
class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1 # Скільки порожніх полів для завантаження фото показувати за замовчуванням

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'is_pinned', 'order')
    list_editable = ('is_pinned', 'order') # Дозволяє ставити галочки і міняти порядок прямо зі списку
    inlines = [NewsImageInline]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position', 'order')
    list_editable = ('order',)
    search_fields = ('last_name', 'first_name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'study_year', 'semester')
    list_filter = ('study_year',)