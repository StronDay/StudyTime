from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Schedule(models.Model):
    DAYS_OF_WEEK = (
        ('MON', 'Понедельник'),
        ('TUE', 'Вторник'),
        ('WED', 'Среда'),
        ('THU', 'Четверг'),
        ('FRI', 'Пятница'),
        ('SAT', 'Суббота'),
    )

    group = models.ForeignKey('students.Group', on_delete=models.PROTECT)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50)
    additional_info = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'schedules'
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.start_time}-{self.end_time} {self.subject}"