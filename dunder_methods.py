#__init__ (Initialization)

# Function equivalent
def create_point(x, y):
    point = {}
    point['x'] = x
    point['y'] = y
    return point

# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Usage
p1 = create_point(3, 4)  # Using function
p2 = Point(3, 4)         # Using class (calls __init__)
print(p1,p2)

#__new__ (Object Creation)

# Function equivalent
def create_point_instance(cls, x, y):
    instance = object.__new__(cls)
    instance.x = x
    instance.y = y
    return instance

# Class implementation
class Point:
    def __new__(cls, x, y):
        print("Creating new Point instance")
        instance = super().__new__(cls)
        instance.x = x
        instance.y = y
        return instance

# Usage
p1 = create_point_instance(Point, 3, 4)  # Using function
p2 = Point(3, 4)                         # Using class (calls __new__)

print(p1,p2)

# __del__ (Destruction)

# Function equivalent
def delete_point(point):
    print(f"Deleting point: {point}")
    del point

# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print(f"Deleting point: ({self.x}, {self.y})")

# Usage
p1 = {'x': 3, 'y': 4}
a = delete_point(p1)  # Using function
print(a)

p2 = Point(3, 4)
del p2           # Using class (calls __del__)

# After deletion, p1 and p2 are no longer available
# So no need to print them after deletion

#__str__ (String Representation)

# Function equivalent
def point_to_string(point):
    return f"Point at ({point['x']}, {point['y']})"

# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point at ({self.x}, {self.y})"

# Usage
p1 = {'x': 3, 'y': 4}
print(point_to_string(p1))  # Using function

p2 = Point(3, 4)
print(str(p2))             # Using class (calls __str__)

# __repr__ (Developer String Representation)

# Function equivalent
def point_to_repr(point):
    return f"Point({point['x']}, {point['y']})"

# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Usage
p1 = {'x': 3, 'y': 4}
print("point_to_repr:", point_to_repr(p1))  # Using function

p2 = Point(3, 4)
print("point_to_repr:", repr(p2))          # Using class (calls __repr__)

#__len__ (Length)

# Function equivalent
def get_length(container):
    return len(container['items'])


# Class implementation
class PointList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


# Usage
pl1 = {'items': [1, 2, 3]}
print(get_length(pl1))  # Using function

pl2 = PointList([1, 2, 3])
print(len(pl2))  # Using class (calls __len__)

# __getitem__ (Indexing)

# Function equivalent
def get_item(container, index):
    return container['items'][index]


# Class implementation
class PointList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


# Usage
pl1 = {'items': [1, 2, 3]}
print(get_item(pl1, 0))  # Using function

pl2 = PointList([1, 2, 3])
print(pl2[0])  # Using class (calls __getitem__)

#__setitem__ (Setting Items)

# Function equivalent
def set_item(container, index, value):
    container['items'][index] = value


# Class implementation
class PointList:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value


# Usage
pl1 = {'items': [1, 2, 3]}
set_item(pl1, 0, 10)  # Using function

pl2 = PointList([1, 2, 3])
pl2[0] = 10  # Using class (calls __setitem__)


# More container operations (__delitem__, __iter__, __next__, __contains__)
# Numeric operations (__add__, __sub__, __mul__, etc.)
# Comparison operations (__eq__, __lt__, __gt__, etc.)
# Attribute access (__getattr__, __setattr__, __delattr__)
# Context managers (__enter__, __exit__)
# Asynchronous operations (__aenter__, __aexit__, __await__)
# Type conversion (__int__, __float__, __bool__)
# Bitwise operations (__and__, __or__, __xor__)
# In-place operations (__iadd__, __isub__, __imul__)
# Let me know which ones you'd like to see next!


#__delitem__ (Deleting Items)

# Function equivalent
def delete_item(container, index):
    del container['items'][index]


# Class implementation
class PointList:
    def __init__(self, items):
        self.items = items

    def __delitem__(self, index):
        del self.items[index]


# Usage
pl1 = {'items': [1, 2, 3]}
delete_item(pl1, 0)  # Using function

pl2 = PointList([1, 2, 3])
del pl2[0]  # Using class (calls __delitem__)


# __iter__ (Iteration)

# Function equivalent
def get_iterator(container):
    return iter(container['items'])


# Class implementation
class PointList:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)


# Usage
pl1 = {'items': [1, 2, 3]}
for item in get_iterator(pl1):  # Using function
    print(item)

pl2 = PointList([1, 2, 3])
for item in pl2:  # Using class (calls __iter__)
    print(item)

#__next__ (Next Item)

# Function equivalent
def get_next(iterator):
    return next(iterator)


# Class implementation
class PointIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item


# Usage
items = [1, 2, 3]
it1 = iter(items)
print(get_next(it1))  # Using function

it2 = PointIterator(items)
print(next(it2))  # Using class (calls __next__)


# Function equivalent
def contains_item(container, item):
    return item in container['items']

#__contains__ (Membership Testing
# Class implementation
class PointList:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items


# Usage
pl1 = {'items': [1, 2, 3]}
print(contains_item(pl1, 1))  # Using function

pl2 = PointList([1, 2, 3])
print(1 in pl2)  # Using class (calls __contains__)


#__call__ (Making Objects Callable)

# Function equivalent
def call_point(point, x, y):
    return {'x': point['x'] + x, 'y': point['y'] + y}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, x, y):
        return Point(self.x + x, self.y + y)


# Usage
p1 = {'x': 1, 'y': 2}
result1 = call_point(p1, 3, 4)  # Using function

p2 = Point(1, 2)
result2 = p2(3, 4)  # Using class (calls __call__)

#__add__ (Addition)

# Function equivalent
def add_points(p1, p2):
    return {'x': p1['x'] + p2['x'], 'y': p1['y'] + p2['y']}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


# Usage
p1 = {'x': 1, 'y': 2}
p2 = {'x': 3, 'y': 4}
result1 = add_points(p1, p2)  # Using function
print(result1)

p3 = Point(1, 2)
p4 = Point(3, 4)
result2 = p3 + p4  # Using class (calls __add__)
print(result2)

#__sub__ (Subtraction)

# Function equivalent
def subtract_points(p1, p2):
    return {'x': p1['x'] - p2['x'], 'y': p1['y'] - p2['y']}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


# Usage
p1 = {'x': 1, 'y': 2}
p2 = {'x': 3, 'y': 4}
result1 = subtract_points(p1, p2)  # Using function

p3 = Point(1, 2)
p4 = Point(3, 4)
result2 = p3 - p4  # Using class (calls __sub__)

#__mul__ (Multiplication)

# Function equivalent
def multiply_point(p, scalar):
    return {'x': p['x'] * scalar, 'y': p['y'] * scalar}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x * other, self.y * other)
        return Point(self.x * other.x, self.y * other.y)


# Usage
p1 = {'x': 1, 'y': 2}
result1 = multiply_point(p1, 3)  # Using function

p2 = Point(1, 2)
result2 = p2 * 3  # Using class (calls __mul__)

#__truediv__ (True Div)

# Function equivalent
def divide_point(p, scalar):
    return {'x': p['x'] / scalar, 'y': p['y'] / scalar}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x / other, self.y / other)
        return Point(self.x / other.x, self.y / other.y)


# Usage
p1 = {'x': 6, 'y': 8}
result1 = divide_point(p1, 2)  # Using function

p2 = Point(6, 8)
result2 = p2 / 2  # Using class (calls __truediv__)

# More numeric operations (__floordiv__, __mod__, __pow__)
# Comparison operations (__eq__, __lt__, __gt__, etc.)
# Attribute access (__getattr__, __setattr__, __delattr__)
# Context managers (__enter__, __exit__)
# Asynchronous operations (__aenter__, __aexit__, __await__)
# Type conversion (__int__, __float__, __bool__)
# Bitwise operations (__and__, __or__, __xor__)
# In-place operations (__iadd__, __isub__, __imul__)

#__floordiv__ (Floor Division)

# Function equivalent
def floor_divide_point(p, scalar):
    return {'x': p['x'] // scalar, 'y': p['y'] // scalar}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x // other, self.y // other)
        return Point(self.x // other.x, self.y // other.y)


# Usage
p1 = {'x': 7, 'y': 9}
result1 = floor_divide_point(p1, 2)  # Using function

p2 = Point(7, 9)
result2 = p2 // 2  # Using class (calls __floordiv__)

#__mod__ (Modulo)

# Function equivalent
def modulo_point(p, scalar):
    return {'x': p['x'] % scalar, 'y': p['y'] % scalar}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x % other, self.y % other)
        return Point(self.x % other.x, self.y % other.y)


# Usage
p1 = {'x': 7, 'y': 9}
result1 = modulo_point(p1, 3)  # Using function

p2 = Point(7, 9)
result2 = p2 % 3  # Using class (calls __mod__)
print("mod result1, result2:", result1, result1)


# __pow__ (Power)

# Function equivalent
def power_point(p, power):
    return {'x': p['x'] ** power, 'y': p['y'] ** power}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __pow__(self, power):
        return Point(self.x ** power, self.y ** power)


# Usage
p1 = {'x': 2, 'y': 3}
result1 = power_point(p1, 2)  # Using function

p2 = Point(2, 3)
result2 = p2 ** 2  # Using class (calls __pow__)

print("mod result1, result2:", result1, result1)


#__eq__ (Equality)


# Function equivalent
def are_points_equal(p1, p2):
    return p1['x'] == p2['x'] and p1['y'] == p2['y']


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Usage
p1 = {'x': 1, 'y': 2}
p2 = {'x': 1, 'y': 2}
print(are_points_equal(p1, p2))  # Using function

p3 = Point(1, 2)
p4 = Point(1, 2)
print(p3 == p4)  # Using class (calls __eq__)


#__gt__ (Greater Than)

# Function equivalent
def is_point_greater(p1, p2):
    return p1['x'] > p2['x'] and p1['y'] > p2['y']


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


# Usage
p1 = {'x': 3, 'y': 4}
p2 = {'x': 1, 'y': 2}
print(is_point_greater(p1, p2))  # Using function

p3 = Point(3, 4)
p4 = Point(1, 2)
print(p3 > p4)  # Using class (calls __gt__)


#__le__ (Less Than or Equal)

# Function equivalent
def is_point_less_equal(p1, p2):
    return p1['x'] <= p2['x'] and p1['y'] <= p2['y']


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

#__ge__ (Greater Than or Equal)

# Function equivalent
def is_point_greater_equal(p1, p2):
    return p1['x'] >= p2['x'] and p1['y'] >= p2['y']


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y


# Usage
p1 = {'x': 3, 'y': 4}
p2 = {'x': 1, 'y': 2}
print(is_point_greater_equal(p1, p2))  # Using function

p3 = Point(3, 4)
p4 = Point(1, 2)
print(p3 >= p4)  # Using class (calls __ge__)

#__bool__ (Boolean Conversio)

# Function equivalent for validity
def is_point_valid(p):
    return p['x'] != 0 or p['y'] != 0

# Function equivalent for comparison
def is_point_less_equal(p1, p2):
    return (p1['x'], p1['y']) <= (p2['x'], p2['y'])

# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)

# Usage
p1 = {'x': 0, 'y': 0}
print(is_point_valid(p1))  # Using function

p2 = Point(0, 0)
print(bool(p2))  # Using class (calls __bool__)

# Comparison usage
p1 = {'x': 1, 'y': 2}
p2 = {'x': 3, 'y': 4}
print(is_point_less_equal(p1, p2))  # Using function

p3 = Point(1, 2)
p4 = Point(3, 4)
print(p3 <= p4)  # Using class (calls __le__)

# __hash__ (Hash Value)

# Function equivalent
def point_hash(p):
    return hash((p['x'], p['y']))


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))


# Usage
p1 = {'x': 1, 'y': 2}
print(point_hash(p1))  # Using function

p2 = Point(1, 2)
print(hash(p2))  # Using class (calls __hash__)


#__getattr__ (Attribute Access)

# Function equivalent
def get_point_attr(p, name):
    if name == 'magnitude':
        return (p['x'] ** 2 + p['y'] ** 2) ** 0.5
    return p.get(name, None)


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, name):
        if name == 'magnitude':
            return (self.x ** 2 + self.y ** 2) ** 0.5
        raise AttributeError(f"'Point' object has no attribute '{name}'")


# Usage
p1 = {'x': 3, 'y': 4}
print(get_point_attr(p1, 'magnitude'))  # Using function

p2 = Point(3, 4)
print(p2.magnitude)  # Using class (calls __getattr__)

#__setattr__ (Attribute Assignment)


# Function equivalent
def set_point_attr(p, name, value):
    if name in ('x', 'y'):
        p[name] = float(value)
    else:
        p[name] = value


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, name, value):
        if name in ('x', 'y'):
            object.__setattr__(self, name, float(value))
        else:
            object.__setattr__(self, name, value)


# Usage
p1 = {}
set_point_attr(p1, 'x', 3)  # Using function

p2 = Point(0, 0)
p2.x = 3  # Using class (calls __setattr__)

#__delattr__ (Attribute Deletion)


# Function equivalent
def delete_point_attr(p, name):
    if name in ('x', 'y'):
        raise AttributeError("Cannot delete x or y coordinates")
    del p[name]


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, name):
        if name in ('x', 'y'):
            raise AttributeError("Cannot delete x or y coordinates")
        object.__delattr__(self, name)


# Usage
p1 = {'x': 3, 'y': 4, 'color': 'red'}
delete_point_attr(p1, 'color')  # Using function

p2 = Point(3, 4)
p2.color = 'red'
del p2.color  # Using class (calls __delattr__)


#__enter__ and __exit__ (Context Manager)

# Function equivalent
def enter_context(point):
    print(f"Entering context with point: {point}")
    return point


def exit_context(point, exc_type, exc_val, exc_tb):
    print(f"Exiting context with point: {point}")
    if exc_type is not None:
        print(f"Exception occurred: {exc_val}")


# Class implementation
class PointContext:
    def __init__(self, point):
        self.point = point

    def __enter__(self):
        print(f"Entering context with point: {self.point}")
        return self.point

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting context with point: {self.point}")
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")


# Usage
p1 = {'x': 3, 'y': 4}
point = enter_context(p1)  # Using function
try:
    print(point['x'])
finally:
    exit_context(point, None, None, None)

p2 = Point(3, 4)
with PointContext(p2) as p:  # Using class (calls __enter__ and __exit__)
    print(p.x)


# Function equivalent
def enter_context(point):
    print(f"Entering context with point: {point}")
    return point


def exit_context(point, exc_type, exc_val, exc_tb):
    print(f"Exiting context with point: {point}")
    if exc_type is not None:
        print(f"Exception occurred: {exc_val}")


# Class implementation
class PointContext:
    def __init__(self, point):
        self.point = point

    def __enter__(self):
        print(f"Entering context with point: {self.point}")
        return self.point

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting context with point: {self.point}")
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")


# Usage
p1 = {'x': 3, 'y': 4}
point = enter_context(p1)  # Using function
try:
    print(point['x'])
finally:
    exit_context(point, None, None, None)

p2 = Point(3, 4)
with PointContext(p2) as p:  # Using class (calls __enter__ and __exit__)
    print(p.x)


# Function equivalent
async def await_point(point):
    await asyncio.sleep(1)
    return point


# Class implementation
class AwaitablePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __await__(self):
        yield from asyncio.sleep(1)
        return self


# Usage
async def main():
    p1 = {'x': 3, 'y': 4}
    result1 = await await_point(p1)  # Using function

    p2 = AwaitablePoint(3, 4)
    result2 = await p2  # Using class (calls __await__)


#__int__ (Integer Conversion)

# Function equivalent
def point_to_int(p):
    return int((p['x'] ** 2 + p['y'] ** 2) ** 0.5)


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)


# Usage
p1 = {'x': 3, 'y': 4}
print(point_to_int(p1))  # Using function

p2 = Point(3, 4)
print(int(p2))  # Using class (calls __int__)


#__int__ (Integer Conversion)

# Function equivalent
def point_to_int(p):
    return int((p['x'] ** 2 + p['y'] ** 2) ** 0.5)


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)


# Usage
p1 = {'x': 3, 'y': 4}
print(point_to_int(p1))  # Using function

p2 = Point(3, 4)
print(int(p2))  # Using class (calls __int__)

#__float__ (Float Conversion)

# Function equivalent
def point_to_float(p):
    return float((p['x'] ** 2 + p['y'] ** 2) ** 0.5)


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __float__(self):
        return float((self.x ** 2 + self.y ** 2) ** 0.5)


# Usage
p1 = {'x': 3, 'y': 4}
print(point_to_float(p1))  # Using function

p2 = Point(3, 4)
print(float(p2))  # Using class (calls __float__)


#__and__ (Bitwise AND)

# Function equivalent
def point_bitwise_and(p1, p2):
    return {'x': p1['x'] & p2['x'], 'y': p1['y'] & p2['y']}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __and__(self, other):
        return Point(self.x & other.x, self.y & other.y)


# Usage
p1 = {'x': 5, 'y': 3}  # 101 & 011 = 001
p2 = {'x': 3, 'y': 7}  # 011 & 111 = 011
result1 = point_bitwise_and(p1, p2)  # Using function

p3 = Point(5, 3)
p4 = Point(3, 7)
result2 = p3 & p4  # Using class (calls __and__)

#__or__ (Bitwise OR)

# Function equivalent
def point_bitwise_or(p1, p2):
    return {'x': p1['x'] | p2['x'], 'y': p1['y'] | p2['y']}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __or__(self, other):
        return Point(self.x | other.x, self.y | other.y)


# Usage
p1 = {'x': 5, 'y': 3}  # 101 | 011 = 111
p2 = {'x': 3, 'y': 7}  # 011 | 111 = 111
result1 = point_bitwise_or(p1, p2)  # Using function

p3 = Point(5, 3)
p4 = Point(3, 7)
result2 = p3 | p4  # Using class (calls __or__)

#__xor__ (Bitwise)

# Function equivalent
def point_bitwise_xor(p1, p2):
    return {'x': p1['x'] ^ p2['x'], 'y': p1['y'] ^ p2['y']}


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __xor__(self, other):
        return Point(self.x ^ other.x, self.y ^ other.y)


# Usage
p1 = {'x': 5, 'y': 3}  # 101 ^ 011 = 110
p2 = {'x': 3, 'y': 7}  # 011 ^ 111 = 100
result1 = point_bitwise_xor(p1, p2)  # Using function

p3 = Point(5, 3)
p4 = Point(3, 7)
result2 = p3 ^ p4  # Using class (calls __xor__)

# __iadd__ (In-place Addition)

# Function equivalent
def point_inplace_add(p1, p2):
    p1['x'] += p2['x']
    p1['y'] += p2['y']
    return p1


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


# Usage
p1 = {'x': 1, 'y': 2}
p2 = {'x': 3, 'y': 4}
result1 = point_inplace_add(p1, p2)  # Using function

p3 = Point(1, 2)
p4 = Point(3, 4)
p3 += p4  # Using class (calls __iadd__)

#__isub__ (In-place Sub)

# Function equivalent
def point_inplace_sub(p1, p2):
    p1['x'] -= p2['x']
    p1['y'] -= p2['y']
    return p1


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self


# Usage
p1 = {'x': 5, 'y': 6}
p2 = {'x': 3, 'y': 4}
result1 = point_inplace_sub(p1, p2)  # Using function

p3 = Point(5, 6)
p4 = Point(3, 4)
p3 -= p4  # Using class (calls __isub__)

#__imul__ (In-place Multipli)

# Function equivalent
def point_inplace_mul(p, scalar):
    p['x'] *= scalar
    p['y'] *= scalar
    return p


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
        else:
            self.x *= other.x
            self.y *= other.y
        return self


# Usage
p1 = {'x': 2, 'y': 3}
result1 = point_inplace_mul(p1, 3)  # Using function

p2 = Point(2, 3)
p2 *= 3  # Using class (calls __imul__)

#__ixor__ (In-place Bitwise)

# Function equivalent
def point_inplace_xor(p1, p2):
    p1['x'] ^= p2['x']
    p1['y'] ^= p2['y']
    return p1


# Class implementation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __ixor__(self, other):
        self.x ^= other.x
        self.y ^= other.y
        return self


# Usage
p1 = {'x': 5, 'y': 3}  # 101 ^ 011 = 110
p2 = {'x': 3, 'y': 7}  # 011 ^ 111 = 100
result1 = point_inplace_xor(p1, p2)  # Using function

p3 = Point(5, 3)
p4 = Point(3, 7)
p3 ^= p4  # Using class (calls __ixor__)

