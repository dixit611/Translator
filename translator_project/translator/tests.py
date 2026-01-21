from django.test import TestCase, Client
from django.urls import reverse
import json

class TranslatorTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_translate_view(self):
        url = reverse('translate')
        data = {
            'text': 'Hello',
            'src_lang': 'en',
            'dest_lang': 'es'
        }
        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertIn('translated_text', response_data)
        # Note: We can't strictly assert the translation result as it depends on googletrans API
        # but we can check it is not empty.
        self.assertTrue(response_data['translated_text'])
        print(f"Translation result: {response_data['translated_text']}")
