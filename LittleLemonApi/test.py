from django.test import TestCase
from LittleLemonApi.models import Booking


class BookingTest(TestCase):
    def test_booking(self):
        booking = Booking.objects.create(
            name='test',
            phone='123456',
            email='test@test.com',
            date='2021-01-01',
            time='12:00',
            number_of_guests=1,
            message='test'
        )

        self.assertEqual(
            booking.__str__(),
            "test : 2021-01-01 : 12:00"
        )
