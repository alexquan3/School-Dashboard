from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

SEMESTER_CHOICES = (
    ('Fall', 'Fall'),
    ('Winter', 'Winter'),
    ('Summer', 'Summer'),
)

# Create your models here.
class Classes(models.Model):
    user = models.ForeignKey(User,null=True, related_name="classes", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, null=True)
    semester = models.CharField(max_length=6,choices=SEMESTER_CHOICES,default='FALL')
    grade = models.CharField(max_length=2, blank=True,null=True)
    GPA = models.DecimalField(max_digits=6, decimal_places=2,blank=True, default=0 , validators=[
            MaxValueValidator(12.00),
            MinValueValidator(1.00)
        ])
    completed = models.BooleanField(blank=True,default='False')
      
    def __str__(self):
        return self.name

class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank =True)
    due_date = models.DateField()
    completed = models.BooleanField(blank=True,default='False')
    classes = models.ForeignKey(Classes, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name