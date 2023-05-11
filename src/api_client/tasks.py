from datetime import datetime

from celery import shared_task

from api_client.models import Course
from api_client.teachbase_api_client import TeachbaseClient


@shared_task
def get_courses_from_teachbase():
    # Create an instance of TeachbaseClient and get a list of courses
    client = TeachbaseClient()
    client.authorize()
    courses_data = client.get_courses()

    # Traversing the list of courses and creating Course objects for each course
    for course_data in courses_data:
        course, created = Course.objects.get_or_create(
            id=course_data['id'],
            defaults={
                'name': course_data['name'],
                'created_at': datetime.fromisoformat(course_data['created_at']),
                'updated_at': datetime.fromisoformat(course_data['updated_at']),
                'owner_id': course_data['owner_id'],
                'owner_name': course_data['owner_name'],
                'thumb_url': course_data['thumb_url'],
                'cover_url': course_data['cover_url'],
                'description': course_data['description'],
                'last_activity': course_data['last_activity'],
                'total_score': course_data['total_score'],
                'total_tasks': course_data['total_tasks'],
                'unchangeable': course_data['unchangeable'],
                'include_weekly_report': course_data['include_weekly_report'],
                'content_type': course_data['content_type'],
                'is_netology': course_data['is_netology'],
                'bg_url': course_data['bg_url'],
                'video_url': course_data['video_url'],
                'demo': course_data['demo'],
                'custom_author_names': course_data['custom_author_names'],
                'custom_contents_link': course_data['custom_contents_link'],
                'hide_viewer_navigation': course_data['hide_viewer_navigation'],
                'duration': course_data['duration'],
                'competences': course_data['competences']
            }
        )
