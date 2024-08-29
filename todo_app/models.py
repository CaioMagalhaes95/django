from django.db import models

# Create your models here.
class Task(models.Model):

    CATEGORY_CHOICES = [
        ('6601', 'Category 6601'),
        ('7051', 'Category 7051'),
        ('8849', 'Category 8849'),
    ]

    TEST_COUNT_CHOICES = [(i, str(i)) for i in range(1, 10)]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    particulate = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default='6601')
    test_count = models.IntegerField(choices=TEST_COUNT_CHOICES, default=1)
    requested_test_count = models.IntegerField(choices=TEST_COUNT_CHOICES, default=1)
    base_value = models.FloatField(default= 0.0, help_text='Valor base para cálculo')
    calculated_value = models.FloatField(default=0.0, editable=False, help_text='Valor calculado com base em base_value')

    def save(self, *args, **kwargs):
        self.calculated_value = self.base_value * 2
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title