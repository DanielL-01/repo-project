"""
#import entire module
import pizza

pizza.make_pizza(12, "mushroom", "peppers", "cheese")
"""
#import specific function
"""
from pizza import make_pizza

make_pizza(12, "mushroom", "peppers", "cheese")
"""
"""
from pizza import make_pizza as mp

mp(12, "mushroom", "cheese")
"""
"""
from pizza import * #all (asterisk)

make_pizza(12, "mushroom", "peppers", "cheese")
make_payment(400000, 385000)
"""

import pizza as p 
p.make_pizza(12, "mushroom", "cheese")
p.make_payment(400000, 385000)