import cloudinary
from decouple import config #os.environ.get()

CLOUDINARY_CLOUD_NAME=config("CLOUDINARY_CLOUD_NAME",default="")
CLOUINARY_PUBLIC_API_KEY=config("CLOUINARY_PUBLIC_API_KEY", default="")
CLOUDINARY_SECRET_KEY=config("CLOUDINARY_SECRET_KEY")

def cloudinary_init():     
    cloudinary.config( 
       cloud_name = CLOUDINARY_CLOUD_NAME,
       api_key =  CLOUINARY_PUBLIC_API_KEY,
       api_secret = CLOUDINARY_SECRET_KEY, 
       secure=True
    )