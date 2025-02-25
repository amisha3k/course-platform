from django.db import models

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

class AccessRequirement(models.TextChoices):
     ANYONE="any", "Anyone"
     EMAIL_REQUIRED="email","Email required"

class PublishStatus(models.TextChoices):
     PUBLISHED="publish", "Published" 
     COMING_SOON="soon","coming soon"    
     DRAFT="draft", "Draft"

def handle_upload(instance,filename):
     return f"{filename}"     

class Course(models.Model):
     title=models.CharField(max_length=120)
     description=models.TextField(blank=True, null=True)
     image=models.ImageField()
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
     @property
     def is_published(self):
          return self.status == PublishStatus.PUBLISHED                