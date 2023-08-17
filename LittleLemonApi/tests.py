from django.test import TestCase
from LittleLemonApi.models import Booking, MenuItem


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


class MenuItemTest(TestCase):
    def test_menu_item(self):
        menu_item = MenuItem.objects.create(
            title='test',
            price=10,
            inventory=10
        )

        self.assertEqual(
            menu_item.get_item(),
            "test : 10"
        )