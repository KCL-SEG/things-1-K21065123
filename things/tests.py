from django.test import TestCase
from django.forms import ValidationError
from .models import Thing

class ThingModelTestCase(TestCase):
    
    def setUp(self):
        self.thing= Thing.objects.create(
            name= 'zoo',
            description= 'There are 4 zoos in london!',
            quantity= 4
        )

    #check if a user is valid
    def test_valid_thing(self):
        self._assert_thing_is_valid()
    
    def test_name_cant_be_blank(self):
        self.thing.name= ''
        self._assert_thing_is_invalid()
    
    def test_name_must_be_unique(self):
        second_thing= self.create_second_thing()
        self.thing.name = second_thing.name
        self._assert_thing_is_invalid()
    
    def test_name_can_be_30_chars_long(self):
        self.thing.name= 'x'*30
        self._assert_thing_is_valid()
    
    def test_name_cant_be_over_30_chars_long(self):
        self.thing.name= 'x'*31
        self._assert_thing_is_invalid()
    
    def test_description_can_be_120_chars_long(self):
        self.thing.description= 'x'*120
        self._assert_thing_is_valid()
    
    def test_description_cant_be_over_120_chars_long(self):
        self.thing.description= 'x'*121
        self._assert_thing_is_invalid()
    
    def test_description_doesnt_have_be_unique(self):
        second_thing= self.create_second_thing()
        self.thing.description = second_thing.description
        self._assert_thing_is_valid()
    
    def test_description_doesnt_have_be_unique(self):
        second_thing= self.create_second_thing()
        self.thing.quantity = second_thing.quantity
        self._assert_thing_is_valid()
    
    def test_quantity_cant_be_over_100(self):
        self.thing.quantity=110
        self._assert_thing_is_invalid()
    
    def test_quantity_cant_be_less_than_0(self):
        self.thing.quantity= -1
        self._assert_thing_is_invalid()
    
    def test_quantity_can_be_100(self):
        self.thing.quantity=100
        self._assert_thing_is_valid()
    
    def test_quantity_can_be_0(self):
        self.thing.quantity=0
        self._assert_thing_is_valid()
    

    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except ValidationError:
            self.fail('Test thing should be valid')

    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()
    
    def create_second_thing(self):
        thing= Thing.objects.create(
            name= 'river',
            description= 'There is 1 river in london!',
            quantity= 1
        )
        return thing