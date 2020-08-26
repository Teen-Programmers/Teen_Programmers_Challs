# 2020 06 07 Weekly Challenges

Welcome to the weekly challenges for the week of the 2020/06/07!

## Challenges

So that you can later use the prebuilt test suite to make sure all the implementations work, you need to clone this folder and write all your code in the `challenges.py` file using the class and method stubs prepared for you.

### Beginner

1. Return `True` in `is_even` if the given number is even, else `False`.
2. Return `True` in `is_prime` if the given number is a prime number, else `False`.
3. Return `True` in `is_mersenne` if the given number is a Mersenne prime, else `False`.

### Intermediate

1. Complete the `class Car` to store attributes.
2. Introduce type-hinting in the constructor of `class Car`.
   - `weight` is `int`
   - `wheels` is `int`
   - `passengers` is `int`
   - `model_number` is `int`
   - `manufacturer` is `str`
3. Override the `__repr__` method so `print(car)` responds with:
   `Car weight: <weight> | Car wheels: <wheels> | Passengers: <passengers> | Model number: <model_number>`

### Extra

Creat a class `Store` with the following attributes:
   - `size` is `int`
   - `sales` is `list of ints`
   - `item_list` is `list of strs`
complete the `add_item` method to allow the user to add an item to the list and complete the `average_pay` method to get an average of the `sales` list
