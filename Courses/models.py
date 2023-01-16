from django.db import models
# from django.contrib.auth.models import User


class Courses(models.Model):
    course_id = models.BigAutoField(unique=True, primary_key=True)
    Coursename = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Coursename


class Coursedata(models.Model):
    ratingchoices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    Srno = models.BigAutoField(unique=True, primary_key=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    comments = models.TextField(max_length=200)
    rating = models.IntegerField(choices=ratingchoices)
