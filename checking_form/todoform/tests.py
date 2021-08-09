from django.test import Client, TestCase
from django.urls import reverse

from .models import ModelForm


class PostFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.form2 = ModelForm.objects.create(
            name='FormPhone',
            phone='+73011234567',
            date='2021-08-04',
        )

    def test_FormPhone(self):
        form_data2 = {
            'phone': '+78005553535',
            'date': '2021-08-04',
        }
        response2 = PostFormTests.guest_client.post(
            reverse('index'),
            data=form_data2,
        )
        self.assertEqual(response2.context.get('output_forms')[0], self.form2.name)

    def test_NoForm(self):
        form_data = {
            'email': 'email@yandex.ru',
        }
        response2 = PostFormTests.guest_client.post(
            reverse('index'),
            data=form_data,
        )
        self.assertEqual(response2.context.get('output_forms'), '{\n  "email": "email@yandex.ru"\n}')
