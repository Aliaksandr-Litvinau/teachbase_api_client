from django.urls import path
from api_client.views import CourseList, CourseDetail

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:id>/', CourseDetail.as_view(), name='course-detail'),
]
