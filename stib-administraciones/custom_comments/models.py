from django.conf import settings
from django.db import models
from django.contrib.comments.models import BaseCommentAbstractModel


class NotificationComments(BaseCommentAbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user',
                             blank=True, null=True, related_name="%(class)s_comments")
    name = models.CharField(max_length=150, blank=False, null=False)
    body = models.TextField(max_length=3000, blank=False, null=False)
    submit_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.user_id = self.user.id
        super(NotificationComments, self).save(*args, **kwargs)

