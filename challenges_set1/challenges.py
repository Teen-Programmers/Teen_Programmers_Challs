import json
import math
import typing

### Beginner Challenges ###


def is_even(num: int) -> bool:
    """The `is_even` method for the beginner challenge."""
    pass


def is_prime(num: int) -> bool:
    """The `is_prime` method for the beginner challenge."""
    pass


def is_mersenne(num: int) -> bool:
    """The `is_mersenne` method for the beginner challenge."""
    pass


### Intermediate Challenges ###


class Car(object):
    """The `Car` class you need to write for the intermediate challenge."""

    def __init__(self, weight: int, wheels: int, passengers: int, model_number: int, manufacturer: str) -> None:
        pass


    def __repr__(self) -> str: # do not change this to __str__
        """This method needs to be overriden as part of the challenge."""
        pass


### Proficient Challenges ###

  
class Store:
    def __init__(self, size, sales, item_list) -> None:
        '''Vars should be called as inputted, eg size should be self.size'''
        pass
    def add_item(self, item: str) -> None:
        '''Update item list'''
        pass

    def average_pay(self) -> int:
        '''Average pay'''
        pass
