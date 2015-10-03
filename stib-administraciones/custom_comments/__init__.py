from .models import NotificationComments
from .forms import NotificationCommentsForm

def get_model():
    return NotificationComments

def get_form():
    return NotificationCommentsForm