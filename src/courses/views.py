# This code defines Django views for handling courses and lessons in an e-learning platform. 
# It interacts with the services.py module to fetch courses and lessons.
import helpers
from django.http import Http404, JsonResponse
from django.shortcuts import render
from . import services


# Instead of rendering an HTML page, this returns a JSON response containing a list of course IDs.
# JsonResponse is useful for API responses or AJAX request
def course_list_view(request):
    queryset=services.get_publish_courses()
    print(queryset)
    #return JsonResponse({"data":[x.path for x in queryset]})
    context={
        "object_list": queryset
    }
    return render(request, "courses/list.html",context)
    

def course_detail_view(request,course_id=None,*args,**kwargs):
    course_obj=services.get_course_detail(course_id=course_id)
    if course_obj is None:
        raise Http404
    lessons_queryset=services.get_course_lessons(course_obj)
    context={
        "object": course_obj,
        "lessons_queryset": lessons_queryset   
    # return JsonResponse({"data":course_obj.id,'lesson_ids':
    # [x.path for x in lessons_queryset]})
    }
    return render(request, "courses/detail.html",context)


def lesson_detail_view(request, course_id=None, lesson_id=None, *args, **kwargs):
     print(f"Course ID: {course_id}, Lesson ID: {lesson_id}")
     if not course_id or not lesson_id:
        return JsonResponse({"error": "Missing course_id or lesson_id"}, status=400)

     lesson_obj = services.get_lesson_detail(course_id=course_id, lesson_id=lesson_id)
     if lesson_obj is None:
         return JsonResponse({"error": "Lesson not found", "course_id": course_id, "lesson_id": lesson_id}, status=404)
     print("Lesson Object Found:", lesson_obj)  # Debugging line
     #template_name="courses/purchase-required.html"
     template_name="courses/lesson-coming-soon.html"
     context={
         "object": lesson_obj
     }  
     if not lesson_obj.is_coming_soon and lesson_obj.has_video:
         """
         lesson is published
         video  is available
         go forward
         """
         template_name="courses/lesson.html" 
         video_embed_html= helpers.get_cloudinary_video_object(
             lesson_obj,
             field_name='video',
             as_html=True,
             width=1000
         ) 
         context['video_embed']=video_embed_html
     return render(request, template_name, context)  
