from django.db import models
from django.core.validators import MinValueValidator


class Resume(models.Model):
    ACTIVE = 'A'
    INACTIVE = 'I'
    FROZEN = 'F'

    STATUSES = (
        (ACTIVE, 'Активный'),
        (INACTIVE, 'Неактивный'),
        (FROZEN, 'Замороженный'),
    )

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUSES)
    grade = models.PositiveSmallIntegerField()
    specialty = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 validators=[MinValueValidator(0)], )
    education = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    portfolio = models.URLField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        db_table = 'resume'
        verbose_name = 'resume'
        verbose_name_plural = 'resumes'

    # def get_absolute_url(self):
    #     return

    def __str__(self):
        return f'{self.title}'
