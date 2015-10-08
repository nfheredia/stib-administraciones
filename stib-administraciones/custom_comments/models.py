from django.db import models
from django.contrib.comments.models import BaseCommentAbstractModel


class NotificationComments(BaseCommentAbstractModel):
    name = models.CharField(max_length=150, blank=False, null=False)
    body = models.TextField(max_length=3000, blank=False, null=False)
    submit_date = models.DateTimeField(auto_now_add=True)
