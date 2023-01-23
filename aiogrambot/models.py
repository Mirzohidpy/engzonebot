from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class User(models.Model):
    chat_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.chat_id

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.full_name


class Level(models.Model):
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.level


class ExistingStudent(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.full_name


class LessonOrder(models.Model):
    lessonName = models.CharField(max_length=100)

    def __str__(self):
        return self.lessonName


class TrialVideos(models.Model):
    video = models.FileField(upload_to='videos/', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    level = models.ForeignKey('Level', on_delete=models.CASCADE, null=True, blank=True)
    lesson_name = models.ForeignKey('LessonOrder', on_delete=models.CASCADE)
    video_file_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.video.name

    class Meta:
        verbose_name = 'Trial Video'
        verbose_name_plural = 'Trial Videos'


class Question(models.Model):
    title = models.CharField("title", max_length=255)
    points = models.SmallIntegerField("points")
    level = models.ForeignKey("Level", on_delete=models.CASCADE)
    open_period = models.IntegerField("open period", default=30)
    is_active = models.BooleanField("Is Active", default=True)
    created_at = models.DateTimeField("Created", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated", auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', verbose_name="Question", on_delete=models.CASCADE)
    answer = models.CharField("Answer", max_length=255)
    is_correct = models.BooleanField("Correct Answer", default=False)
    is_active = models.BooleanField("Is Active", default=True)
    created_at = models.DateTimeField("Created", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated", auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.answer
