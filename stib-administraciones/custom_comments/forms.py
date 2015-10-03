from django import forms
from django.contrib.comments.forms import CommentSecurityForm
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_text
from django.utils import timezone
from django.conf import settings
from .models import NotificationComments

class NotificationCommentsForm(CommentSecurityForm):
    name = forms.CharField(max_length=150, label="Nombre")
    body = forms.CharField(label="Comentario", widget=forms.Textarea,
                              max_length=1000)

    def get_comment_model(self):
        return NotificationComments

    def get_comment_object(self):
        if not self.is_valid():
            raise ValueError("get_comment_object may only be called on valid forms")

        NotificationComments = self.get_comment_model()
        new = NotificationComments(**self.get_comment_create_data())

        return new


    def get_comment_create_data(self):
		return dict(
		    content_type=ContentType.objects.get_for_model(self.target_object),
		    object_pk=force_text(self.target_object._get_pk_val()),
		    submit_date=timezone.now(),
		    site_id=settings.SITE_ID,
            name=self.cleaned_data['name'],
            body=self.cleaned_data['body']
		)