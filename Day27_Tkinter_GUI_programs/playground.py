# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# # print(add(4,6,2,1,5,7,9))


# def calculate(n, **kwargs):
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)
#
# calculate(2, add=3, multiply=5)

#Creating a class with optional keyword arguments

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make = 'Nissan')
print(my_car.model)