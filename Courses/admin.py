from django.contrib import admin
from .models import Courses, Coursedata


class coursesAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'Coursename']


admin.site.register(Courses, coursesAdmin)


class coursedataAdmin(admin.ModelAdmin):
    list_display = ('Srno', 'course_id', 'comments', 'rating')


admin.site.register(Coursedata, coursedataAdmin)
