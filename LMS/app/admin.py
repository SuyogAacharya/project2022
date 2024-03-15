from django.contrib import admin
from .models import *

class What_You_Learn_TabularInline(admin.TabularInline):
    model = What_you_learn
    extra = 1

class Requirements_TabularInline(admin.TabularInline):
    model = Requirements
    extra = 1

class Video_TabularInline(admin.TabularInline):
    model = Video
    fk_name = 'course'
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [What_You_Learn_TabularInline, Requirements_TabularInline, Video_TabularInline]



admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Language)
admin.site.register(UserCourse)
admin.site.register(TeamMember)
admin.site.register(Mission)
admin.site.register(Vision)
admin.site.register(History)
admin.site.register(StudentProfile)
admin.site.register(Notice)
admin.site.register(Resources_course)
admin.site.register(Resources_Question)
admin.site.register(Resources_ScoreBoard)