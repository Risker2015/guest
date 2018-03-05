from django.test import TestCase
from sign.models import Event,Guest

class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000,address='shenzhen', start_time='2018-03-05 00:00:00',create_time='2018-03-05 00:00:00')
        Guest.objects.create(id=1,event_id=1,realname='alen',phone='13711001101',email='alen@mail.com', sign=False)

    def test_event_model(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address,"shenzhen")
        self.assertTrue(result.status)

    def test_guest_model(self):
        result = Guest.objects.get(phone="13711001101")
        self.assertEqual(result.realname,'alen')
        self.assertTrue(result.sign)

if __name__ == "__main__":
    TestCase.run()