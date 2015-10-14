from django.test import TestCase, RequestFactory
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from ..views import FeedbacksCreate

from stib_administraciones.stib_administraciones.perfiles.models import Perfiles


class CreatePageViewTest(TestCase):

    def setUp(self):
        # -- add site
        self.site = Site()
        self.site.id = 5
        self.site.domain = 'lalala.com'
        self.site.name = 'kskkassa'
        self.site.save()
        # -- create user
        User = get_user_model()
        self.user = User.objects.create_user(
            username='user',
            email='jsj@gmail.com',
            password='pass')
        self.user.save()

        self.create_view_url = reverse('feedback_create')

        self.factory = RequestFactory()

    def test_call_view_with_incorrect_login(self):
        # -- invalid login
        self.client.login(username='blabla', password='blablablabla')
        # -- access to view
        response = self.client.get(self.create_view_url)
        # -- not access
        self.assertEqual(response.status_code, 302)
        # -- test redirect to login
        self.assertRedirects(response, '/accounts/login/?next={}'.format(self.create_view_url))

    def test_view(self):
        request = self.factory.get(self.create_view_url)
        request.user = self.user
        view = FeedbacksCreate.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'feedbacks/feedbacks_form.html')

    def test_create_feedback(self):
        self.client.login(username='user', password='pass')
        response = self.client.post(self.create_view_url,
                                    data={'tipo_feedback': 1,
                                          'asunto': 'Bla Bla',
                                          'mensaje': 'Mensaje Mensaje'})
        self.assertEqual(response.status_code, 302)
