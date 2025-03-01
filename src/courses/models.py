import uuid
import helpers
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

"""
Field	Purpose
title	Course name
description	Course details
public_id	Unique course identifier (Indexed for fast search)
image	Cloud-based image storage (Cloudinary)
access	Defines who can view the course
status	Defines if the course is published or in draft
timestamp	Stores course creation date
updated	Stores last modification date

-courses:
  -title
  -description
  -thumbnail/image
  -access:
       -anyone
       -email required
  -status:
       -published
       -coming soon
       -draft    

"""
helpers.cloudinary_init()

class AccessRequirement(models.TextChoices):
     ANYONE="any", "Anyone"
     EMAIL_REQUIRED="email","Email required"

class PublishStatus(models.TextChoices):
     PUBLISHED="publish", "Published" 
     COMING_SOON="soon","coming soon"    
     DRAFT="draft", "Draft"

def handle_upload(instance,filename):
     return f"{filename}"     

     # from courses.models import course
     # course.object.all()-> list all courses
     # course.objects.first()-> first row of all courses

def generate_public_id(instance,*args,**kwargs):
     title=instance.title
     unique_id=str(uuid.uuid4()).replace("-","")
     if not title:
          return unique_id
     slug=slugify(title)
     unique_id_short=unique_id[:5]
     return f"{slug}-{unique_id_short}"

def get_public_id_prefix(instance,*args,**kwargs):
     if hasattr(instance,'path'):
          path=instance.path
          if path.startswith("/"):
               path=path[1:]
          if path.endswith('/'):
               path=path[:-1]
          return path             
     public_id=instance.public_id
     model_classs=instance.__class__
     model_name=model_class.__name__ 
     model_name_slug=slugify(model_name)    
     if not public_id:
        return "courses"
     return "courses/{public_id}"         

def get_display_name(instance,*args,**kwargs):
     if hasattr(instance,'get_display_name'):
          return instance.get_display_name()
     elif hasattr(instance,'title'):
          return instance.title
     model_classs=instance.__class__
     model_name=model_class.__name__         
     return "Courses upload"     

class Course(models.Model):
     title=models.CharField(max_length=120)
     description=models.TextField(blank=True, null=True)
     public_id=models.CharField(max_length=130,blank=True,null=True)
     #image=models.ImageField(upload_to=handle_upload,blank=True,null=False)
     image=CloudinaryField(
          "image", 
          null=True,
          public_id_prefix=get_public_id_prefix,
          display_name=get_display_name,
          tags=["course","thumbnail"]
          )
     access=models.CharField(
                     max_length=5,
                     choices=AccessRequirement.choices,
                     default=AccessRequirement.EMAIL_REQUIRED
                     )
     status=models.CharField(
                     max_length=10,
                     choices=PublishStatus.choices,
                     default=PublishStatus.DRAFT
                     )

     def save(self,*args,**kwargs):
          #before save
          if self.public_id=="" or self.public_id is None:
             self.public_id=generate_public_id(self)
          super().save(*args,**kwargs)
          #after save
     
     def get_absolute_url(self):
          return self.path

     @property
     def path(self):
          return f"/courses/{self.public_id}"     

     def get_display_nema(self):  
          return f"{self.title}-Course"   


     @property
     def is_published(self):
          return self.status == PublishStatus.PUBLISHED  

     @property
     def image_admin_url(self):
          if not self.image:
               return ""
          image_options={
               "width":200
          }    
          url=self.image.buuild_url(**image_options)
          return url  

     def get_image_thumbnail(self,as_html=False,width=500):
          if not self.image:
               return ""
          image_options={
               "width":width
          }     
          if as_html:
               return self.image,image(**image_options)

          url=self.image.build_url(**image_options)   
          return url  

     def get_image_detail(self,as_html=False,width=750):
          if not self.image:
               return ""
          image_options={
               "width":width
          }     
          if as_html:
               return self.image,image(**image_options)

          url=self.image.build_url(**image_options)   
          return url  

"""
lesson
     title
     description
     video
     status: published,coming soon,draft
"""
# lesson.objects.all() #lesson queryset ->all rows
#  lesson.objects.first()
# course_obj=course.objects.filter()
# course_qs=course.objects.filter(id==course_obj.id)
# lesson.objects.filter(course__id=course_obj.id)
# course_obj.lesson_set.all()
#course_obj.lesson_set.all().order_by("title")

class Lesson(models.Model):
     course=models.ForeignKey(Course, on_delete=models.CASCADE)
     #course_id
     public_id = models.CharField(max_length=130, blank=True, null=True, db_index=True)
     title=models.CharField(max_length=120)
     description=models.TextField(blank=True, null=True)
     thumbnail=CloudinaryField("image",
               public_id_prefix=get_public_id_prefix,
               display_name=get_display_name,
               tags=['thumbnail','lesson'],
               blank=True,null=True)
     video=CloudinaryField("video",
           public_id_prefix=get_public_id_prefix,
           display_name=get_display_name,
           blank=True,
           null=True,
           tags=['video','lesson'],
           resource_type='video')
     order=models.BigIntegerField(default=0)
     can_preview=models.BooleanField(default=False,help_text="if user does not has access to course,can they see this?")
     status=models.CharField(
                     max_length=10,
                     choices=PublishStatus.choices,
                     default=PublishStatus.DRAFT
                     )
     timestamp=models.DateTimeField(auto_now=True)
     updated=models.DateTimeField(auto_now=True)

     class Meta:
          ordering=['order','-updated']

     def save(self,*args,**kwargs):
          #before save
          if self.public_id=="" or self.public_id is None:
             self.public_id=generate_public_id(self)
          super().save(*args,**kwargs)
          #after save   

     @property
     def path(self):
          course_path=self.course.path
          if course_path.endswith("/"):
               course_path=course_path[:-1]
          return f"{course_path}/lessons/{self.public_id}"     

     def get_display_nema(self):  
          return f"{self.title}-{self.course.get_display_name()}"     
     

