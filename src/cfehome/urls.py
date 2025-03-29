
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from emails.views import verify_email_token_view
from . import views

urlpatterns = [
    path("",views.home_view),
    path('verify/<uuid:token>/',verify_email_token_view),
    path("courses/",include("courses.urls")),
    path('admin/', admin.site.urls),
   
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
    