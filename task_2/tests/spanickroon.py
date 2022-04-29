#===========
#Test Module
import math

c = 42
def f(x):
    a = 123
    return math.sin(x * a * c)
#=============
# Test Function
def test_func(bebra):
    return bebra ** 2

# =============
# Spanicroon Class
class Spanickroon:

    def __init__(self, name='Nikita Koznev', age=54, milkshake="pistachioMilkShake") -> None:
        self.name = name
        self.age = age
        self.milkshake = milkshake

    name: str
    age: int
    milkshake: str

    def bad_meme(self):
        print('Minus point')

    def good_meme(self):
        print('Plus point')

spanickroon_object = Spanickroon()

