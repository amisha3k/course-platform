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
       -purchase required
       -user required
  -status:
       -published
       -coming soon
       -draft    

"""
class Course(models.Model):
     title=models.CharField(max_length=120)