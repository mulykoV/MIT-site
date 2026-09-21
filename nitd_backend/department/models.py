from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    patronymic = models.CharField(max_length=50, verbose_name="По батькові", blank=True)
    position = models.CharField(max_length=100, verbose_name="Посада (напр., Доцент)")
    degree = models.CharField(max_length=100, verbose_name="Науковий ступінь", blank=True)
    
    # Контакти
    email = models.EmailField(unique=True, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    github = models.URLField(blank=True, null=True, verbose_name="GitHub") # Додали GitHub
    
    # Зображення
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    
    bio = models.TextField(blank=True, verbose_name="Біографія")
    
    # Додаємо сортування, щоб виводити завідувача кафедри першим
    order = models.IntegerField(default=100, verbose_name="Порядок сортування (менше число = вище)")

    class Meta:
        ordering = ['order', 'last_name'] # Спочатку за порядком, потім за алфавітом
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва дисципліни")
    description = models.TextField(verbose_name="Опис")
    teachers = models.ManyToManyField(Teacher, related_name='courses', verbose_name="Викладачі")
    study_year = models.PositiveSmallIntegerField(verbose_name="Курс (рік навчання)")
    semester = models.PositiveSmallIntegerField(verbose_name="Семестр", blank=True, null=True)

    class Meta:
        verbose_name = "Дисципліна"
        verbose_name_plural = "Дисципліни"

    def __str__(self):
        return self.title


# --- НОВІ МОДЕЛІ ДЛЯ НОВИН ---

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст новини")
    date_posted = models.DateField(auto_now_add=True, verbose_name="Дата публікації")
    
    # Закріплення та сортування
    is_pinned = models.BooleanField(default=False, verbose_name="Закріпити нагорі")
    order = models.IntegerField(default=100, verbose_name="Порядок (менше число = вище)")

    class Meta:
        # Django спочатку покаже закріплені, потім відсортує за order, а потім за свіжістю
        ordering = ['-is_pinned', 'order', '-date_posted']
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/', verbose_name="Фото")
    
    class Meta:
        verbose_name = "Фотографію"
        verbose_name_plural = "Галерея новини"