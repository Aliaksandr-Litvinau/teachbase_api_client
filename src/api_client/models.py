from django.db import models


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner_id = models.IntegerField()
    owner_name = models.CharField(max_length=100)
    thumb_url = models.URLField(max_length=200, null=True, blank=True)
    cover_url = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    last_activity = models.TextField(null=True, blank=True)
    total_score = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)
    unchangeable = models.BooleanField(default=False)
    include_weekly_report = models.BooleanField(default=False)
    content_type = models.IntegerField()
    is_netology = models.BooleanField(default=False)
    bg_url = models.URLField(max_length=200, null=True, blank=True)
    video_url = models.URLField(max_length=200, null=True, blank=True)
    demo = models.BooleanField(default=False)
    custom_author_names = models.CharField(max_length=100, null=True, blank=True)
    custom_contents_link = models.URLField(max_length=200, null=True, blank=True)
    hide_viewer_navigation = models.BooleanField(default=False)
    duration = models.IntegerField(null=True, blank=True)
    competences = models.JSONField()

    def __str__(self):
        return self.name
