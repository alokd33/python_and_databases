| Dunder Method | Python Function Equivalent | Class Usage Example | Description & When to Use |
|--------------|--------------------------|-------------------|--------------------------|
| __init__ | Constructor | def __init__(self, x, y): self.x = x; self.y = y | Called when object is created. Initialize object attributes. |
| __new__ | Object creation | def __new__(cls, *args, **kwargs): return super().__new__(cls) | Called before __init__. Controls object creation. |
| __del__ | Destructor | def __del__(self): print("Object deleted") | Called when object is about to be destroyed. |
| __str__ | str() | def __str__(self): return f"Point({self.x}, {self.y})" | String representation for end users. |
| __repr__ | repr() | def __repr__(self): return f"Point({self.x}, {self.y})" | String representation for developers. |
| __len__ | len() | def __len__(self): return len(self.items) | Returns length of object. |
| __getitem__ | obj[key] | def __getitem__(self, key): return self.items[key] | Access object using index/key. |
| __setitem__ | obj[key] = value | def __setitem__(self, key, value): self.items[key] = value | Set value using index/key. |
| __delitem__ | del obj[key] | def __delitem__(self, key): del self.items[key] | Delete item using index/key. |
| __iter__ | iter() | def __iter__(self): return iter(self.items) | Returns iterator object. |
| __next__ | next() | def __next__(self): return next(self.iterator) | Returns next item in iterator. |
| __contains__ | in | def __contains__(self, item): return item in self.items | Check if item exists in object. |
| __call__ | obj() | def __call__(self, *args): return self.process(*args) | Make object callable like function. |
| __add__ | + | def __add__(self, other): return Point(self.x + other.x, self.y + other.y) | Addition operation. |
| __sub__ | - | def __sub__(self, other): return Point(self.x - other.x, self.y - other.y) | Subtraction operation. |
| __mul__ | * | def __mul__(self, other): return Point(self.x * other.x, self.y * other.y) | Multiplication operation. |
| __truediv__ | / | def __truediv__(self, other): return Point(self.x / other.x, self.y / other.y) | True division operation. |
| __floordiv__ | // | def __floordiv__(self, other): return Point(self.x // other.x, self.y // other.y) | Floor division operation. |
| __mod__ | % | def __mod__(self, other): return Point(self.x % other.x, self.y % other.y) | Modulo operation. |
| __pow__ | | def __pow__(self, power): return Point(self.x ** power, self.y ** power) | Power operation. |
| __eq__ | == | def __eq__(self, other): return self.x == other.x and self.y == other.y | Equality comparison. |
| __ne__ | != | def __ne__(self, other): return not (self == other) | Inequality comparison. |
| __lt__ | < | def __lt__(self, other): return self.x < other.x and self.y < other.y | Less than comparison. |
| __le__ | <= | def __le__(self, other): return self.x <= other.x and self.y <= other.y | Less than or equal comparison. |
| __gt__ | > | def __gt__(self, other): return self.x > other.x and self.y > other.y | Greater than comparison. |
| __ge__ | >= | def __ge__(self, other): return self.x >= other.x and self.y >= other.y | Greater than or equal comparison. |
| __bool__ | bool() | def __bool__(self): return bool(self.x or self.y) | Boolean conversion. |
| __hash__ | hash() | def __hash__(self): return hash((self.x, self.y)) | Hash value for object. |
| __getattr__ | Attribute access | def __getattr__(self, name): return self.default_values.get(name) | Called when attribute not found. |
| __setattr__ | Attribute assignment | def __setattr__(self, name, value): object.__setattr__(self, name, value) | Called when setting attribute. |
| __delattr__ | del obj.attr | def __delattr__(self, name): del self.__dict__[name] | Called when deleting attribute. |
| __getattribute__ | Attribute access | def __getattribute__(self, name): return object.__getattribute__(self, name) | Called for all attribute access. |
| __dir__ | dir() | def __dir__(self): return ['x', 'y'] | Returns list of attributes. |
| __slots__ | Class attribute | __slots__ = ['x', 'y'] | Optimizes memory usage by pre-declaring attributes. |
| __class__ | type() | self.__class__ | Reference to object's class. |
| __dict__ | vars() | self.__dict__ | Dictionary of object's attributes. |
| __doc__ | help() | """Class documentation""" | Documentation string. |
| __module__ | - | self.__module__ | Module name where class is defined. |
| __name__ | - | self.__class__.__name__ | Class name. |
| __qualname__ | - | self.__class__.__qualname__ | Qualified class name. |
| __annotations__ | - | __annotations__ = {'x': int, 'y': int} | Type annotations. |
| __bases__ | - | self.__class__.__bases__ | Tuple of base classes. |
| __mro__ | - | self.__class__.__mro__ | Method Resolution Order. |
| __subclasses__ | - | self.__class__.__subclasses__() | List of subclasses. |
| __instancecheck__ | isinstance() | @classmethod def __instancecheck__(cls, instance): return True | Custom isinstance() behavior. |
| __subclasscheck__ | issubclass() | @classmethod def __subclasscheck__(cls, subclass): return True | Custom issubclass() behavior. |
| __enter__ | with | def __enter__(self): return self | Context manager entry. |
| __exit__ | with | def __exit__(self, exc_type, exc_val, exc_tb): pass | Context manager exit. |
| __await__ | await | def __await__(self): yield self | Makes object awaitable. |
| __aiter__ | async for | async def __aiter__(self): return self | Asynchronous iterator. |
| __anext__ | async for | async def __anext__(self): return next(self.items) | Asynchronous next item. |
| __aenter__ | async with | async def __aenter__(self): return self | Asynchronous context manager entry. |
| __aexit__ | async with | async def __aexit__(self, exc_type, exc_val, exc_tb): pass | Asynchronous context manager exit. |
| __index__ | int() | def __index__(self): return self.value | Integer conversion for indexing. |
| __round__ | round() | def __round__(self, n): return Point(round(self.x, n), round(self.y, n)) | Rounding operation. |
| __trunc__ | math.trunc() | def __trunc__(self): return Point(math.trunc(self.x), math.trunc(self.y)) | Truncation operation. |
| __floor__ | math.floor() | def __floor__(self): return Point(math.floor(self.x), math.floor(self.y)) | Floor operation. |
| __ceil__ | math.ceil() | def __ceil__(self): return Point(math.ceil(self.x), math.ceil(self.y)) | Ceiling operation. |
| __format__ | format() | def __format__(self, format_spec): return f"{self.x}:{self.y}" | Custom string formatting. |
| __bytes__ | bytes() | def __bytes__(self): return bytes([self.x, self.y]) | Bytes conversion. |
| __complex__ | complex() | def __complex__(self): return complex(self.x, self.y) | Complex number conversion. |
| __int__ | int() | def __int__(self): return int(self.x) | Integer conversion. |
| __float__ | float() | def __float__(self): return float(self.x) | Float conversion. |
| __oct__ | oct() | def __oct__(self): return oct(self.x) | Octal conversion. |
| __hex__ | hex() | def __hex__(self): return hex(self.x) | Hexadecimal conversion. |
| __abs__ | abs() | def __abs__(self): return Point(abs(self.x), abs(self.y)) | Absolute value. |
| __pos__ | +obj | def __pos__(self): return Point(+self.x, +self.y) | Unary positive. |
| __neg__ | -obj | def __neg__(self): return Point(-self.x, -self.y) | Unary negative. |
| __invert__ | ~obj | def __invert__(self): return Point(~self.x, ~self.y) | Bitwise inversion. |
| __lshift__ | << | def __lshift__(self, other): return Point(self.x << other, self.y << other) | Left shift. |
| __rshift__ | >> | def __rshift__(self, other): return Point(self.x >> other, self.y >> other) | Right shift. |
| __and__ | & | def __and__(self, other): return Point(self.x & other.x, self.y & other.y) | Bitwise AND. |
| __or__ | \| | def __or__(self, other): return Point(self.x \| other.x, self.y \| other.y) | Bitwise OR. |
| __xor__ | ^ | def __xor__(self, other): return Point(self.x ^ other.x, self.y ^ other.y) | Bitwise XOR. |
| __radd__ | + (reversed) | def __radd__(self, other): return self + other | Reversed addition. |
| __rsub__ | - (reversed) | def __rsub__(self, other): return Point(other.x - self.x, other.y - self.y) | Reversed subtraction. |
| __rmul__ | * (reversed) | def __rmul__(self, other): return self * other | Reversed multiplication. |
| __rtruediv__ | / (reversed) | def __rtruediv__(self, other): return Point(other.x / self.x, other.y / self.y) | Reversed true division. |
| __rfloordiv__ | // (reversed) | def __rfloordiv__(self, other): return Point(other.x // self.x, other.y // self.y) | Reversed floor division. |
| __rmod__ | % (reversed) | def __rmod__(self, other): return Point(other.x % self.x, other.y % self.y) | Reversed modulo. |
| __rpow__ | (reversed) | def __rpow__(self, other): return Point(other.x ** self.x, other.y ** self.y) | Reversed power. |
| __rlshift__ | << (reversed) | def __rlshift__(self, other): return Point(other << self.x, other << self.y) | Reversed left shift. |
| __rrshift__ | >> (reversed) | def __rrshift__(self, other): return Point(other >> self.x, other >> self.y) | Reversed right shift. |
| __rand__ | & (reversed) | def __rand__(self, other): return Point(other & self.x, other & self.y) | Reversed bitwise AND. |
| __ror__ | \| (reversed) | def __ror__(self, other): return Point(other \| self.x, other \| self.y) | Reversed bitwise OR. |
| __rxor__ | ^ (reversed) | def __rxor__(self, other): return Point(other ^ self.x, other ^ self.y) | Reversed bitwise XOR. |
| __iadd__ | += | def __iadd__(self, other): self.x += other.x; self.y += other.y; return self | In-place addition. |
| __isub__ | -= | def __isub__(self, other): self.x -= other.x; self.y -= other.y; return self | In-place subtraction. |
| __imul__ | = | def __imul__(self, other): self.x *= other.x; self.y *= other.y; return self | In-place multiplication. |
| __itruediv__ | /= | def __itruediv__(self, other): self.x /= other.x; self.y /= other.y; return self | In-place true division. |
| __ifloordiv__ | //= | def __ifloordiv__(self, other): self.x //= other.x; self.y //= other.y; return self | In-place floor division. |
| __imod__ | %= | def __imod__(self, other): self.x %= other.x; self.y %= other.y; return self | In-place modulo. |
| __ipow__ | = | def __ipow__(self, other): self.x **= other.x; self.y **= other.y; return self | In-place power. |
| __ilshift__ | <<= | def __ilshift__(self, other): self.x <<= other; self.y <<= other; return self | In-place left shift. |
| __irshift__ | >>= | def __irshift__(self, other): self.x >>= other; self.y >>= other; return self | In-place right shift. |
| __iand__ | &= | def __iand__(self, other): self.x &= other.x; self.y &= other.y; return self | In-place bitwise AND. |
| __ior__ | \|= | def __ior__(self, other): self.x \|= other.x; self.y \|= other.y; return self | In-place bitwise OR. |
| __ixor__ | ^= | def __ixor__(self, other): self.x ^= other.x; self.y ^= other.y; return self | In-place bitwise XOR. |
