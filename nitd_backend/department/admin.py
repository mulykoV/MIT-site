from django.contrib import admin
import nested_admin
from .models import Teacher, Course, News, NewsImage, Schedule, ScheduleSync, Conference, Olympiad, Textbook, Curator, EduSection, EduGroup, EduLink, EduImage
from .parser import sync_pubhtml_schedule

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

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'course_id', 'subgroup', 'day', 'timeStart', 'type', 'get_actual_teacher', 'room')
    list_filter = ('course_id', 'subgroup', 'day', 'type')
    search_fields = ('subject', 'teacher__last_name', 'external_teacher', 'room')

    def get_actual_teacher(self, obj):
        if obj.teacher:
            return f"{obj.teacher.last_name} {obj.teacher.first_name}"
        return obj.external_teacher or "-"

    get_actual_teacher.short_description = "Викладач"


@admin.register(ScheduleSync)
class ScheduleSyncAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'status', 'sync_date', 'result_message')
    readonly_fields = ('sync_date', 'result_message')

    def save_model(self, request, obj, form, change):
        result = sync_pubhtml_schedule(obj.google_sheet_url, obj.course_id, obj.status)
        obj.result_message = result
        super().save_model(request, obj, form, change)

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_held')
    list_filter = ('date_held',)
    search_fields = ('title',)

@admin.register(Olympiad)
class OlympiadAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_held')
    list_filter = ('date_held',)
    search_fields = ('title',)

@admin.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'external_authors')
    # Робить вибір авторів з нашої кафедри дуже зручним (через 2 колонки)
    filter_horizontal = ('teachers',)

@admin.register(Curator)
class CuratorAdmin(admin.ModelAdmin):
    list_display = ('course', 'group_name', 'teacher')
    list_filter = ('course',)
    search_fields = ('group_name', 'teacher__last_name', 'teacher__first_name')

class LinkInline(nested_admin.NestedTabularInline):
    model = EduLink
    extra = 1
    sortable_field_name = "order"          # перетягування мишкою


class GroupInline(nested_admin.NestedStackedInline):
    model = EduGroup
    extra = 0
    sortable_field_name = "order"
    inlines = [LinkInline]


class ImageInline(nested_admin.NestedTabularInline):
    model = EduImage
    extra = 0
    sortable_field_name = "order"


@admin.register(EduSection)
class EduSectionAdmin(nested_admin.NestedModelAdmin):
    list_display = ("title", "order", "show_in_menu", "is_published")
    list_editable = ("order", "show_in_menu", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ImageInline, GroupInline]
