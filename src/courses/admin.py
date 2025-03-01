from django.contrib import admin
from cloudinary import CloudinaryImage
from django.utils.html import format_html
from .models import Course,Lesson

#admin customization
class LessonInline(admin.StackedInline):
    model=Lesson
    readonly_fields=['public_id','updated']
    extra=0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines=[LessonInline]
    list_display=['title','status','access']
    list_filter=['status','access',]
    fields=['public_id','title','description','status','image','access','display_image']
    readonly_fields=['public_id','display_image']

    
    def display_image(obj,self,*args,**kwargs):
        url=obj.image.url
        cloudinary_id=str(obj.image)
        cloudinary_html=CloudinaryImage(cloudinary_id).image(width=500)
        return format_html(cloudinary_html)
       # return format_html(f"<img src='{url}'/>")

    display_image.short_description="current image"    

#admin.site.register(Course)