# This code provides utility functions to retrieve published courses and lessons in a Django project. 
# It queries the database using Django's ORM (Object-Relational Mapper) and applies filtering conditions.

from .models import Course,Lesson,PublishStatus


#Purpose: Fetches all courses that are published.
#How?
#It filters the Course model based on the status field.
#Only courses where status = PublishStatus.PUBLISHED are returned.
def get_publish_courses():
    return Course.objects.filter(status=PublishStatus.PUBLISHED)


# Purpose: Fetches details of a specific course if it is published.
# How?
# If course_id is None, it returns None immediately.
# It queries the Course model using .get(), filtering by:
# public_id = course_id
# status = PublishStatus.PUBLISHED
def get_course_detail(course_id=None):
    if course_id is None:
        return None
    obj=None
    try:
        obj = Course.objects.get(
            status=PublishStatus.PUBLISHED,
            public_id=course_id
        )
    except:
        pass
    return obj

# Purpose: Fetches all lessons of a given course, but only if:
# The course itself is published.
# The lessons are either published or coming soon.
def get_course_lessons(course_obj=None):
    lessons = Lesson.objects.none()
    if not isinstance(course_obj, Course):
        return lessons
    lessons = course_obj.lesson_set.filter(
        course__status=PublishStatus.PUBLISHED,
        status__in=[PublishStatus.PUBLISHED, PublishStatus.COMING_SOON]
    )
    return lessons


# Purpose: Fetches details of a specific lesson, ensuring:
# The course is published.
# The lesson is either published or coming soon.    
def get_lesson_detail(course_id=None, lesson_id=None):
    if lesson_id is None and course_id is None:
        return None
    obj = None
    try:
        obj = Lesson.objects.get(
            course__public_id=course_id,
            course__status=PublishStatus.PUBLISHED,
            status__in=[PublishStatus.PUBLISHED,PublishStatus.COMING_SOON],
            public_id=lesson_id
        )
    except Exception as e:
        print("lesson detail", e)
        pass
    return obj

        




