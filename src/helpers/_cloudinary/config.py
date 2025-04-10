import cloudinary
from django.conf import settings

CLOUDINARY_CLOUD_NAME=settings.CLOUDINARY_CLOUD_NAME
CLOUINARY_PUBLIC_API_KEY=settings.CLOUINARY_PUBLIC_API_KEY
CLOUDINARY_SECRET_KEY=settings.CLOUDINARY_SECRET_KEY

def cloudinary_init():     
    cloudinary.config( 
       cloud_name = CLOUDINARY_CLOUD_NAME,
       api_key =  CLOUINARY_PUBLIC_API_KEY,
       api_secret = CLOUDINARY_SECRET_KEY, 
       secure=True
    )