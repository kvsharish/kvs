from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import items

class Basictests(TestCase):
    def setup(self):
        items.objects.create(name='nokia',
                            descrption='best product',
                            costperitem= 1122,
                            stockquantity= 22,
                            volume="24684.00" )
    def test_get_method(self):
        url="http://127.0.0.1:8000/students/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=items.objects.filter(name='nokia')
        self.assertEqual(qs.count(),1)

