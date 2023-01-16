from .models import Courses, Coursedata
from .forms import rating
from django.shortcuts import render
from django.http import HttpResponseRedirect


def view1(request):
    cd = Courses.objects.all()
    ratingresult = {}
    for i in cd:
        print(i)
        onlypython = Courses.objects.filter(Coursename=i)
        courserating = Coursedata.objects.filter(course_id__in=onlypython)
        su = 0
        for j in courserating:
            su += j.rating
        if su > 0:
            su = su/courserating.count()
        ratingresult[i.Coursename] = round(su, 1)
    print(ratingresult)

    return render(request, "index.html", {'values': cd, 'courserating': ratingresult})


def input(request, courseid):
    form = rating()
    print(courseid)
    if request.method == "POST":
        cid = Courses.objects.get(course_id=courseid)
        Coursedata.objects.create(course_id=cid,
                                  comments=request.POST['comments'], rating=request.POST['rate'])
        return HttpResponseRedirect('/')

    cd = Courses.objects.all()
    ratingresult = {}
    for i in cd:
        print(i)
        onlypython = Courses.objects.filter(Coursename=i)
        courserating = Coursedata.objects.filter(course_id__in=onlypython)
        su = 0
        for j in courserating:
            su += j.rating
        if su > 0:
            su = su/courserating.count()
        ratingresult[i.Coursename] = round(su, 1)
    print(ratingresult)

    return render(request, "input2.html", {'form': form, 'values': cd, 'courserating': ratingresult})

    # return render(request, "input2.html", {'form': form})


# def input2(request, courseid):
#     form = rating()
#     print(courseid)
#     if request.method == "POST":
#         cid = Courses.objects.get(course_id=courseid)
#         Coursedata.objects.create(course_id=cid,
#                                   comments=request.POST['comments'], rating=request.POST['rating'])
#         return HttpResponseRedirect('/')

#     return render(request, "input2.html", {'form': form})
