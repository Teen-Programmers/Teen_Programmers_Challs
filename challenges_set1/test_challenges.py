import unittest
from unittest import mock
import challenges

class T100BeginnerTests(unittest.TestCase):
    """Tests for beginner challenge"""
    def setUp(self):
        pass
    def test_101_even(self):
        '''Check the `is_even` function is correct'''
        self.assertEqual(challenges.is_even(10), True)
        self.assertEqual(challenges.is_even(7), False)

    def test_102_prime(self):
        '''Check the `is_prime` function is correct'''
        self.assertEqual(challenges.is_prime(5),True)
        self.assertEqual(challenges.is_prime(137), True)
        self.assertEqual(challenges.is_prime(140), False)
    
    def test_103_mersenne(self):
        '''Check the `is_mersenee` function is correct'''
        self.assertEqual(challenges.is_mersenne(8191), True)
        self.assertEqual(challenges.is_mersenne(21), False)

class T200IntermediateTests(unittest.TestCase):
    '''Test for intermediate challenges'''
    def setUp(self):
        self.car = challenges.Car(weight=700, wheels=4, passengers=8, model_number=9999, manufacturer="Nissan")
    
    def test_201_car_init(self):
        '''Check the car object inits correctly'''
        self.assertEqual(self.car.weight, 700)
        self.assertEqual(self.car.wheels, 4)
    
    def test_202_car_repr(self):
        '''Check the car object prints as expected'''
        excpected = 'Car weight: 700 | Car wheels: 4 | Passengers: 8 | Model number: 9999'
        self.assertEqual(repr(self.car), excpected)

class T300AdvancedTests(unittest.TestCase):
    '''Check for advanced tests'''
    def setUp(self):
        self.store = challenges.Store(size=10, sales=[100,200,300,400], item_list=['Apples','Peaches','Bananas'])
    def test_301_get_avg(self):
        '''Get average sales'''
        self.assertEqual(self.store.average_pay(), 250.0)
    def test_302_add_item(self):
        '''Try updating item list'''
        self.store.add_item('Chocolate')
        self.assertEqual(self.store.item_list, ['Apples','Peaches','Bananas', 'Chocolate'])
