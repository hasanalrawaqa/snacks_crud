from django.test import TestCase
from django.urls import reverse
from .models import Snack

class SnackModelTest(TestCase):
    def test_string_representation(self):
        snack = Snack(title="Chips")
        self.assertEqual(str(snack), "Chips")

class SnackViewsTest(TestCase):
    def setUp(self):
        self.snack = Snack.objects.create(title="Chips", purchaser="John", description="Tasty chips", rating=8)

    def test_snack_list_view(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chips")

    def test_snack_detail_view(self):
        response = self.client.get(reverse('snack_detail', args=[self.snack.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chips")

    def test_snack_create_view(self):
        response = self.client.post(reverse('snack_create'), {
            'title': 'New Snack',
            'purchaser': 'Alice',
            'description': 'Delicious new snack',
            'rating': 7,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Snack.objects.last().title, 'New Snack')

    def test_snack_update_view(self):
        response = self.client.post(reverse('snack_update', args=[self.snack.id]), {
            'title': 'Updated Chips',
            'purchaser': 'Alice',
            'description': 'Tasty chips with updated info',
            'rating': 9,
        })
        self.assertEqual(response.status_code, 302)
        self.snack.refresh_from_db()
        self.assertEqual(self.snack.title, 'Updated Chips')

    def test_snack_delete_view(self):
        response = self.client.post(reverse('snack_delete', args=[self.snack.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Snack.objects.filter(id=self.snack.id).exists())
