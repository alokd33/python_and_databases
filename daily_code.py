def reverse_str(str):
    reverser_string = str[::-1]
    return reverser_string
output = reverse_str("ABC")
print(output)

# =============================================
# PYTHON DICTIONARY CHEAT SHEET
# =============================================

# 1. Dictionary Creation
# =====================
empty_dict = {}
dict_literal = {'key1': 'value1', 'key2': 'value2'}
dict_constructor = dict(key1='value1', key2='value2')
dict_from_pairs = dict([('key1', 'value1'), ('key2', 'value2')])
dict_from_keys = dict.fromkeys(['key1', 'key2'], 'default_value')

print(dict_literal)

# 2. Basic Operations
# ==================
d = {'a': 1, 'b': 2, 'c': 3}

# Access
value = d['a']                    # Get value by key
value = d.get('a')               # Safe get
value = d.get('z', 'default')    # Get with default

# Add/Update
d['d'] = 4                       # Add new key-value
d.update({'e': 5, 'f': 6})       # Update multiple
d.setdefault('g', 7)             # Set if not exists

# Remove
del d['a']                       # Delete by key
value = d.pop('b')               # Remove and return
item = d.popitem()               # Remove last item
d.clear()                        # Remove all items

# 3. Dictionary Methods
# ====================
d.keys()                         # Get all keys
d.values()                       # Get all values
d.items()                        # Get all items
d.copy()                         # Shallow copy
len(d)                           # Number of items

If your dictionary is... | Use
Flat (no nested dict/list) | copy()
Nested (contains dict inside dict, or lists) | deepcopy()

# Safe flat copy
new_dict = old_dict.copy()

# Safe deep independent copy
import copy
new_dict = copy.deepcopy(old_dict)


import copy

original = {'a': 1, 'b': {'c': 2}}
shallow_copy = original.copy()

shallow_copy['a'] = 100   # Only affects shallow_copy
shallow_copy['b']['c'] = 200  # Affects both shallow_copy and original!

print(original)
# Output: {'a': 1, 'b': {'c': 200}}  --> See? b['c'] changed in original too!

import copy

original = {'a': 1, 'b': {'c': 2}}
deep_copy = copy.deepcopy(original)

deep_copy['a'] = 100   # Only affects deep_copy
deep_copy['b']['c'] = 200  # Only affects deep_copy

print(original)
# Output: {'a': 1, 'b': {'c': 2}}  --> Original fully preserved






# 4. Dictionary Views
# ==================
keys = d.keys()                  # Keys view
values = d.values()              # Values view
items = d.items()                # Items view

# 5. Dictionary Comprehension
# ==========================
# Basic
{x: x**2 for x in range(5)}

# With condition
{x: x**2 for x in range(5) if x % 2 == 0}

# Nested
{x: {y: x*y for y in range(3)} for x in range(3)}

# 6. Dictionary Merging
# ====================
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Method 1: update()
merged = dict1.copy()
merged.update(dict2)

# Method 2: ** unpacking (Python 3.5+)
merged = {**dict1, **dict2}

# Method 3: | operator (Python 3.9+)
merged = dict1 | dict2

# 7. Dictionary Sorting
# ===================
d = {'b': 2, 'a': 1, 'c': 3}

# Sort by keys
sorted_by_key = dict(sorted(d.items()))

# Sort by values
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))

# Sort by value descending
sorted_desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

# 8. Dictionary Filtering
# =====================
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Filter by value
filtered = {k: v for k, v in d.items() if v > 2}

# Filter by key
filtered = {k: v for k, v in d.items() if k in ['a', 'c']}

# 9. Dictionary Transformations
# ===========================
# Invert dictionary
inverted = {v: k for k, v in d.items()}

# Transform values
transformed = {k: v*2 for k, v in d.items()}

# 10. Nested Dictionary Operations
# ==============================
nested = {
    'a': {'x': 1, 'y': 2},
    'b': {'x': 3, 'y': 4}
}

# Access nested
value = nested['a']['x']

# Update nested
nested['a']['x'] = 10

# 11. Default Values
# ================
from collections import defaultdict

# Using setdefault
d = {}
d.setdefault('a', []).append(1)

# Using defaultdict
dd = defaultdict(list)
dd['a'].append(1)

# 12. Dictionary Copy
# =================
import copy

# Shallow copy
shallow = d.copy()

# Deep copy
deep = copy.deepcopy(nested)

# 13. Dictionary Membership
# =======================
# Check key existence
'exists' if 'key' in d else 'not exists'

# Check value existence
'exists' if 'value' in d.values() else 'not exists'

# 14. Dictionary Size
# =================
size = len(d)                    # Number of items
is_empty = not d                 # Check if empty

# 15. Dictionary Iteration
# ======================
# Iterate keys
for key in d:
    pass

# Iterate values
for value in d.values():
    pass

# Iterate items
for key, value in d.items():
    pass

# 16. Dictionary Unpacking
# ======================
# Unpack keys
a, b, c = d.keys()

# Unpack values
x, y, z = d.values()

# Unpack items
(k1, v1), (k2, v2) = d.items()

# 17. Dictionary to Other Types
# ===========================
# To list of keys
keys_list = list(d.keys())

# To list of values
values_list = list(d.values())

# To list of tuples
items_list = list(d.items())

# 18. Dictionary Performance
# ========================
# O(1) average case for:
# - Lookup
# - Insert
# - Delete
# - Update

# 19. Common Dictionary Patterns
# ============================
# Group by
from collections import defaultdict
grouped = defaultdict(list)
for item in items:
    grouped[key].append(item)

# Counter
from collections import Counter
counts = Counter(items)


# =============================================
# COMMON DICTIONARY PATTERNS WITH EXAMPLES
# =============================================

# 1. Grouping with defaultdict
# ==========================
from collections import defaultdict

# Example 1: Grouping by category
products = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
    {'name': 'Mouse', 'category': 'Electronics', 'price': 50},
    {'name': 'Chair', 'category': 'Furniture', 'price': 200},
    {'name': 'Table', 'category': 'Furniture', 'price': 300},
    {'name': 'Phone', 'category': 'Electronics', 'price': 800}
]

# Create a defaultdict with list as default factory
grouped_by_category = defaultdict(list)

# Group products by category
for product in products:
    grouped_by_category[product['category']].append(product)

# Result:
# {
#     'Electronics': [
#         {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
#         {'name': 'Mouse', 'category': 'Electronics', 'price': 50},
#         {'name': 'Phone', 'category': 'Electronics', 'price': 800}
#     ],
#     'Furniture': [
#         {'name': 'Chair', 'category': 'Furniture', 'price': 200},
#         {'name': 'Table', 'category': 'Furniture', 'price': 300}
#     ]
# }

# Example 2: Grouping by price range
def get_price_range(price):
    if price < 100:
        return 'Budget'
    elif price < 500:
        return 'Mid-range'
    else:
        return 'Premium'

grouped_by_price = defaultdict(list)
for product in products:
    price_range = get_price_range(product['price'])
    grouped_by_price[price_range].append(product)

# Result:
# {
#     'Premium': [
#         {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
#         {'name': 'Phone', 'category': 'Electronics', 'price': 800}
#     ],
#     'Mid-range': [
#         {'name': 'Chair', 'category': 'Furniture', 'price': 200},
#         {'name': 'Table', 'category': 'Furniture', 'price': 300}
#     ],
#     'Budget': [
#         {'name': 'Mouse', 'category': 'Electronics', 'price': 50}
#     ]
# }

# Example 3: Grouping with multiple keys
grouped_by_category_and_price = defaultdict(list)
for product in products:
    key = (product['category'], get_price_range(product['price']))
    grouped_by_category_and_price[key].append(product)

# Result:
# {
#     ('Electronics', 'Premium'): [
#         {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
#         {'name': 'Phone', 'category': 'Electronics', 'price': 800}
#     ],
#     ('Electronics', 'Budget'): [
#         {'name': 'Mouse', 'category': 'Electronics', 'price': 50}
#     ],
#     ('Furniture', 'Mid-range'): [
#         {'name': 'Chair', 'category': 'Furniture', 'price': 200},
#         {'name': 'Table', 'category': 'Furniture', 'price': 300}
#     ]
# }

# 2. Counting with Counter
# ======================
from collections import Counter

# Example 1: Counting words in text
text = "the quick brown fox jumps over the lazy dog the fox is quick"
words = text.split()

word_counts = Counter(words)
# Result: Counter({'the': 3, 'quick': 2, 'fox': 2, 'brown': 1, 'jumps': 1,
#                 'over': 1, 'lazy': 1, 'dog': 1, 'is': 1})

# Get most common words
most_common = word_counts.most_common(3)
# Result: [('the', 3), ('quick', 2), ('fox', 2)]

# Example 2: Counting product categories
categories = [product['category'] for product in products]
category_counts = Counter(categories)
# Result: Counter({'Electronics': 3, 'Furniture': 2})

# Example 3: Counting with update
counter = Counter()
counter.update(['a', 'b', 'c', 'a', 'b', 'a'])
# Result: Counter({'a': 3, 'b': 2, 'c': 1})

# Example 4: Counter arithmetic
counter1 = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
counter2 = Counter(['a', 'b', 'd'])

# Addition
sum_counter = counter1 + counter2
# Result: Counter({'a': 4, 'b': 3, 'c': 1, 'd': 1})

# Subtraction
diff_counter = counter1 - counter2
# Result: Counter({'a': 2, 'b': 1, 'c': 1})

# Intersection
intersection = counter1 & counter2
# Result: Counter({'a': 1, 'b': 1})

# Union
union = counter1 | counter2
# Result: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

# Example 5: Counting with weights
prices = [product['price'] for product in products]
price_ranges = [get_price_range(price) for price in prices]
weighted_counts = Counter(price_ranges)
# Result: Counter({'Premium': 2, 'Mid-range': 2, 'Budget': 1})

# 3. Advanced Usage Examples
# =======================

# Example 1: Nested defaultdict
nested_dict = defaultdict(lambda: defaultdict(list))
for product in products:
    category = product['category']
    price_range = get_price_range(product['price'])
    nested_dict[category][price_range].append(product)

# Example 2: Counter with custom objects
class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __hash__(self):
        return hash((self.name, self.category))

    def __eq__(self, other):
        return (self.name, self.category) == (other.name, other.category)

products_objects = [
    Product('Laptop', 'Electronics', 1000),
    Product('Mouse', 'Electronics', 50),
    Product('Chair', 'Furniture', 200)
]

product_counter = Counter(products_objects)

# Example 3: Combining defaultdict and Counter
category_price_stats = defaultdict(Counter)
for product in products:
    category = product['category']
    price_range = get_price_range(product['price'])
    category_price_stats[category][price_range] += 1

# Result:
# {
#     'Electronics': Counter({'Premium': 2, 'Budget': 1}),
#     'Furniture': Counter({'Mid-range': 2})
# }

# 20. Dictionary Best Practices
# ===========================
# Use get() for safe access
value = d.get('key', default_value)

# Use setdefault() for initialization
d.setdefault('key', []).append(value)

# Use defaultdict for default values
dd = defaultdict(list)

# Use dict comprehension for transformations
transformed = {k: f(v) for k, v in d.items()}
# =============================================
# PYTHON DICTIONARY LOOPS & ITERATION CHEAT SHEET
# =============================================

# =============================================
# COMPREHENSIVE PYTHON DICTIONARY CHEAT SHEET
# =============================================

# 1. Dictionary Creation (Enhanced)
# ===============================
# Basic creation
empty_dict = {}
dict_literal = {'key1': 'value1', 'key2': 'value2'}

# Advanced creation methods
dict_constructor = dict(key1='value1', key2='value2')
dict_from_pairs = dict([('key1', 'value1'), ('key2', 'value2')])
dict_from_keys = dict.fromkeys(['key1', 'key2'], 'default_value')

# Dictionary with different key types
mixed_keys = {
    1: 'integer key',
    'string': 'string key',
    (1, 2): 'tuple key',  # tuple is immutable
    frozenset([1, 2]): 'frozenset key'  # frozenset is immutable
}

# 2. Dictionary Access (Enhanced)
# =============================
d = {'a': 1, 'b': 2, 'c': 3}

# Basic access
value = d['a']  # Raises KeyError if key doesn't exist

# Safe access methods
value = d.get('a')  # Returns None if key doesn't exist
value = d.get('z', 'default')  # Returns default if key doesn't exist

# Using setdefault (get or set)
value = d.setdefault('a', 100)  # Returns existing value
value = d.setdefault('z', 100)  # Sets and returns new value

# 3. Dictionary Views (Enhanced)
# ============================
# Views are dynamic and reflect changes
keys_view = d.keys()
values_view = d.values()
items_view = d.items()

# View operations
len(keys_view)  # Number of keys
'a' in keys_view  # Membership testing
iter(keys_view)  # Iterator protocol

# 4. Dictionary Methods (Enhanced)
# ==============================
# Basic methods
d.clear()  # Remove all items
d.copy()  # Shallow copy
d.pop('a')  # Remove and return value
d.popitem()  # Remove and return last item
d.update({'d': 4})  # Update with another dict

# Advanced methods
d.__contains__('a')  # Same as 'a' in d
d.__len__()  # Same as len(d)
d.__iter__()  # Same as iter(d)

# 5. Dictionary Comprehension (Enhanced)
# ===================================
# Basic comprehension
{x: x ** 2 for x in range(5)}

# With condition
{x: x ** 2 for x in range(5) if x % 2 == 0}

# Nested comprehension
{x: {y: x * y for y in range(3)} for x in range(3)}

# With walrus operator (Python 3.8+)
{(x := x ** 2): x for x in range(5)}

# 6. Dictionary Merging (Enhanced)
# ==============================
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Different merging methods
merged = dict1.copy()
merged.update(dict2)  # Method 1

merged = {**dict1, **dict2}  # Method 2 (Python 3.5+)

merged = dict1 | dict2  # Method 3 (Python 3.9+)


# Deep merge for nested dictionaries
def deep_merge(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


# 7. Dictionary Sorting (Enhanced)
# =============================
d = {'b': 2, 'a': 1, 'c': 3}

# Sort by keys
sorted_by_key = dict(sorted(d.items()))

# Sort by values
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))

# Sort by multiple criteria
sorted_multi = dict(sorted(d.items(), key=lambda x: (x[1], x[0])))

# 8. Dictionary Filtering (Enhanced)
# ===============================
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Filter by value
filtered = {k: v for k, v in d.items() if v > 2}

# Filter by key
filtered = {k: v for k, v in d.items() if k in ['a', 'c']}

# Filter by both
filtered = {k: v for k, v in d.items() if k in ['a', 'c'] and v > 2}

# 9. Dictionary Transformations (Enhanced)
# =====================================
# Invert dictionary (one-to-one)
inverted = {v: k for k, v in d.items()}

# Transform values
transformed = {k: v * 2 for k, v in d.items()}

# Transform keys
transformed = {k.upper(): v for k, v in d.items()}

# 10. Nested Dictionary Operations (Enhanced)
# ========================================
nested = {
    'a': {'x': 1, 'y': 2},
    'b': {'x': 3, 'y': 4}
}

# Safe nested access
value = nested.get('a', {}).get('x')


# Deep update
def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, dict):
            d[k] = deep_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


# 11. Dictionary Default Values (Enhanced)
# =====================================
from collections import defaultdict

# Using setdefault
d = {}
d.setdefault('a', []).append(1)

# Using defaultdict
dd = defaultdict(list)
dd['a'].append(1)


# Custom default factory
def constant_factory(value):
    return lambda: value


dd = defaultdict(constant_factory('<missing>'))

# 12. Dictionary Copy (Enhanced)
# ===========================
import copy

# Shallow copy
shallow = d.copy()

# Deep copy
deep = copy.deepcopy(nested)


# Custom copy
def custom_copy(d):
    return {k: v.copy() if hasattr(v, 'copy') else v for k, v in d.items()}


# 13. Dictionary Membership (Enhanced)
# =================================
# Check key existence
'exists' if 'key' in d else 'not exists'

# Check value existence
'exists' if 'value' in d.values() else 'not exists'

# Check item existence
'exists' if ('key', 'value') in d.items() else 'not exists'

# 14. Dictionary Size and Memory (Enhanced)
# ======================================
size = len(d)  # Number of items
is_empty = not d  # Check if empty

# Memory usage
import sys

memory = sys.getsizeof(d)

# 15. Dictionary Iteration (Enhanced)
# ================================
# Basic iteration
for key in d:
    pass

# Iterate with enumerate
for i, key in enumerate(d):
    pass

# Iterate with zip
for key, value in zip(d.keys(), d.values()):
    pass

# 16. Dictionary Unpacking (Enhanced)
# ================================
# Unpack keys
a, b, c = d.keys()

# Unpack values
x, y, z = d.values()

# Unpack items
(k1, v1), (k2, v2) = d.items()

# 17. Dictionary to Other Types (Enhanced)
# =====================================
# To list
keys_list = list(d.keys())
values_list = list(d.values())
items_list = list(d.items())

# To tuple
keys_tuple = tuple(d.keys())
values_tuple = tuple(d.values())
items_tuple = tuple(d.items())

# To set
keys_set = set(d.keys())
values_set = set(d.values())

# 18. Dictionary Performance (Enhanced)
# ==================================
# Time complexity:
# - Lookup: O(1) average, O(n) worst
# - Insert: O(1) average, O(n) worst
# - Delete: O(1) average, O(n) worst
# - Update: O(1) average, O(n) worst

# Space complexity: O(n)

# 19. Dictionary Thread Safety
# ==========================
# Dictionary operations are not thread-safe
# Use threading.Lock for thread safety
from threading import Lock

lock = Lock()
with lock:
    d['key'] = 'value'

# 20. Dictionary Serialization
# =========================
import json
import pickle

# JSON serialization
json_str = json.dumps(d)
d_from_json = json.loads(json_str)

# Pickle serialization
pickle_str = pickle.dumps(d)
d_from_pickle = pickle.loads(pickle_str)


# 21. Dictionary Customization
# =========================
class CustomDict(dict):
    def __missing__(self, key):
        return f"Key {key} not found"

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.__missing__(key)


# 22. Dictionary Best Practices
# ==========================
# Use get() for safe access
value = d.get('key', default_value)

# Use setdefault() for initialization
d.setdefault('key', []).append(value)

# Use defaultdict for default values
dd = defaultdict(list)

# Use dict comprehension for transformations
transformed = {k: f(v) for k, v in d.items()}

# Use proper key types (immutable)
valid_keys = {1, 'string', (1, 2), frozenset([1, 2])}

# 23. Dictionary Common Patterns
# ===========================
# Group by
from collections import defaultdict

grouped = defaultdict(list)
for item in items:
    grouped[key].append(item)

# Counter
from collections import Counter

counts = Counter(items)

# Default value dictionary
from collections import defaultdict

dd = defaultdict(lambda: 'default')

# Ordered dictionary
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2)])

# 24. Dictionary Error Handling
# ==========================
try:
    value = d['nonexistent']
except KeyError:
    value = 'default'

# Using get() for safe access
value = d.get('nonexistent', 'default')


# 25. Dictionary Memory Optimization
# ===============================
# Use __slots__ for memory optimization
class OptimizedDict:
    __slots__ = ['a', 'b', 'c']

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3





##########
# 1. Basic Dictionary Loops
# ========================
d = {'a': 1, 'b': 2, 'c': 3}

# Loop through keys
for key in d:
    print(key)

# Loop through keys explicitly
for key in d.keys():
    print(key)

# Loop through values
for value in d.values():
    print(value)

# Loop through items (key-value pairs)
for key, value in d.items():
    print(f"{key}: {value}")

# 2. Advanced Dictionary Loops
# ==========================
# Loop with enumerate
for i, key in enumerate(d):
    print(f"Index {i}: {key}")

# Loop with zip
for key, value in zip(d.keys(), d.values()):
    print(f"{key}: {value}")

# Loop with reversed
for key in reversed(d):
    print(key)

# Loop with sorted
for key in sorted(d):
    print(key)

# 3. Nested Dictionary Loops
# ========================
nested = {
    'a': {'x': 1, 'y': 2},
    'b': {'x': 3, 'y': 4}
}

# Loop through nested dictionary
for outer_key, inner_dict in nested.items():
    for inner_key, value in inner_dict.items():
        print(f"{outer_key}.{inner_key}: {value}")

# 4. Dictionary Comprehension Loops
# ===============================
# Basic comprehension
squares = {x: x**2 for x in range(5)}

# With condition
even_squares = {x: x**2 for x in range(5) if x % 2 == 0}

# Nested comprehension
nested_squares = {x: {y: x*y for y in range(3)} for x in range(3)}

# 5. Dictionary Filter Loops
# ========================
# Filter while looping
filtered = {}
for key, value in d.items():
    if value > 1:
        filtered[key] = value

# Using dict comprehension
filtered = {k: v for k, v in d.items() if v > 1}

# 6. Dictionary Transform Loops
# ===========================
# Transform while looping
transformed = {}
for key, value in d.items():
    transformed[key.upper()] = value * 2

# Using dict comprehension
transformed = {k.upper(): v*2 for k, v in d.items()}

# 7. Dictionary Accumulate Loops
# ============================
# Sum values
total = 0
for value in d.values():
    total += value

# Using sum()
total = sum(d.values())

# 8. Dictionary Search Loops
# ========================
# Find key by value
for key, value in d.items():
    if value == target_value:
        print(f"Found key: {key}")
        break

# Find all keys with value
matching_keys = [key for key, value in d.items() if value == target_value]

# 9. Dictionary Update Loops
# ========================
# Update while looping
for key in d:
    d[key] = d[key] * 2

# Safe update while looping
for key in list(d.keys()):  # Create a list of keys to avoid RuntimeError
    d[key] = d[key] * 2

# 10. Dictionary Delete Loops
# =========================
# Delete while looping (safe way)
for key in list(d.keys()):
    if some_condition:
        del d[key]

# Using dict comprehension
d = {k: v for k, v in d.items() if not some_condition}

# 11. Dictionary Group Loops
# ========================
from collections import defaultdict

# Group by value
grouped = defaultdict(list)
for key, value in d.items():
    grouped[value].append(key)

# 12. Dictionary Chain Loops
# ========================
from itertools import chain

# Chain multiple dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

for key, value in chain(dict1.items(), dict2.items()):
    print(f"{key}: {value}")

# 13. Dictionary Parallel Loops
# ===========================
# Loop through multiple dictionaries in parallel
for (k1, v1), (k2, v2) in zip(dict1.items(), dict2.items()):
    print(f"{k1}: {v1}, {k2}: {v2}")

# 14. Dictionary Ordered Loops
# ==========================
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Loop in insertion order
for key, value in od.items():
    print(f"{key}: {value}")

# 15. Dictionary Reverse Loops
# ==========================
# Loop in reverse order
for key in reversed(d):
    print(key)

# Loop items in reverse
for key, value in reversed(d.items()):
    print(f"{key}: {value}")

# 16. Dictionary Conditional Loops
# =============================
# Loop with break
for key, value in d.items():
    if value == target_value:
        print(f"Found: {key}")
        break

# Loop with continue
for key, value in d.items():
    if value < threshold:
        continue
    print(f"{key}: {value}")

# 17. Dictionary Nested Loops with Conditions
# ========================================
# Complex nested loop with conditions
for outer_key, inner_dict in nested.items():
    if outer_key.startswith('a'):
        for inner_key, value in inner_dict.items():
            if value > threshold:
                print(f"{outer_key}.{inner_key}: {value}")

# 18. Dictionary Loop Performance
# ============================
# Measure loop performance
import time

start_time = time.time()
for key, value in d.items():
    # Do something
    pass
end_time = time.time()
print(f"Loop took {end_time - start_time} seconds")

# 19. Dictionary Loop Best Practices
# ===============================
# Use items() for key-value pairs
for key, value in d.items():  # Good
    pass

for key in d:  # Less efficient if you need values
    value = d[key]
    pass

# Use list() for safe iteration during modification
for key in list(d.keys()):
    if some_condition:
        del d[key]

# 20. Dictionary Loop Patterns
# =========================
# Pattern 1: Transform and filter
result = {k.upper(): v*2 for k, v in d.items() if v > threshold}

# Pattern 2: Group and count
from collections import defaultdict
groups = defaultdict(list)
for key, value in d.items():
    groups[value].append(key)

# Pattern 3: Find maximum/minimum
max_key = max(d, key=d.get)
min_key = min(d, key=d.get)

# Pattern 4: Sort and iterate
for key in sorted(d, key=d.get, reverse=True):
    print(f"{key}: {d[key]}")



 =============================================
# PYTHON DICTIONARY TRICKS & HACKS
# =============================================

# 1. Dictionary Creation Tricks
# ===========================
# Create dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))  # {'a': 1, 'b': 2, 'c': 3}

# Create dictionary with same value
d = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

# Create dictionary from string
s = "hello"
char_count = {char: s.count(char) for char in set(s)}  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# 2. Dictionary Access Tricks
# =========================
d = {'a': 1, 'b': 2}

# Get with default using or
value = d.get('c') or 'default'  # Returns 'default' if key not found

# Chain get for nested dictionaries
nested = {'a': {'b': {'c': 1}}}
value = nested.get('a', {}).get('b', {}).get('c')  # Safe nested access

# 3. Dictionary Update Tricks
# =========================
# Update multiple keys at once
d.update({'c': 3, 'd': 4})

# Update with another dictionary using unpacking
d = {**d, **{'e': 5, 'f': 6}}  # Python 3.5+

# Update with | operator (Python 3.9+)
d |= {'g': 7, 'h': 8}

# 4. Dictionary Deletion Tricks
# ===========================
# Delete multiple keys
keys_to_remove = ['a', 'b']
for k in keys_to_remove:
    d.pop(k, None)  # None as default prevents KeyError

# Delete all keys except some
keep_keys = {'c', 'd'}
d = {k: d[k] for k in keep_keys if k in d}

# 5. Dictionary Inversion Tricks
# ===========================
# Invert dictionary (values become keys)
d = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in d.items()}

# Invert with duplicate values
from collections import defaultdict
d = {'a': 1, 'b': 2, 'c': 1}
inverted = defaultdict(list)
for k, v in d.items():
    inverted[v].append(k)

# 6. Dictionary Sorting Tricks
# ==========================
# Sort by value
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))

# Sort by key length
d = {'apple': 1, 'banana': 2, 'cherry': 3}
sorted_by_key_length = dict(sorted(d.items(), key=lambda x: len(x[0])))

# 7. Dictionary Merging Tricks
# ==========================
# Merge dictionaries with priority
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}  # dict2 values take precedence

# Deep merge dictionaries
def deep_merge(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result

# 8. Dictionary Default Value Tricks
# ================================
# Using defaultdict with lambda
from collections import defaultdict
dd = defaultdict(lambda: 'default')

# Using setdefault in loops
result = {}
for item in items:
    result.setdefault(item.category, []).append(item)

# 9. Dictionary Comprehension Tricks
# ===============================
# Filter and transform in one go
d = {'a': 1, 'b': 2, 'c': 3}
filtered = {k.upper(): v*2 for k, v in d.items() if v > 1}

# Create dictionary from list with index
items = ['apple', 'banana', 'cherry']
d = {i: item for i, item in enumerate(items)}

# 10. Dictionary Performance Tricks
# ==============================
# Use dict.get() instead of try/except
value = d.get('key', default_value)  # Faster than try/except

# Use dict comprehension instead of loop
# Faster than:
# result = {}
# for k, v in d.items():
#     result[k] = v*2
result = {k: v*2 for k, v in d.items()}

# 11. Dictionary Memory Tricks
# =========================
# Use __slots__ for memory optimization
class OptimizedDict:
    __slots__ = ['a', 'b', 'c']
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

# 12. Dictionary Unpacking Tricks
# ============================
# Unpack dictionary into function arguments
def func(a, b, c):
    return a + b + c

d = {'a': 1, 'b': 2, 'c': 3}
result = func(**d)  # Unpacks as func(a=1, b=2, c=3)

# 13. Dictionary Key Tricks
# =======================
# Use tuples as keys
d = {(1, 2): 'point1', (3, 4): 'point2'}

# Use frozenset as keys
d = {frozenset([1, 2]): 'set1', frozenset([3, 4]): 'set2'}

# 14. Dictionary Value Tricks
# =========================
# Store functions in dictionary
def add(a, b): return a + b
def sub(a, b): return a - b

operations = {'add': add, 'sub': sub}
result = operations['add'](1, 2)  # Calls add(1, 2)

# 15. Dictionary Debugging Tricks
# ============================
# Pretty print dictionary
import json
print(json.dumps(d, indent=2))

# Print dictionary sorted by keys
for k in sorted(d):
    print(f"{k}: {d[k]}")

# 16. Dictionary Security Tricks
# ===========================
# Create immutable dictionary
from types import MappingProxyType
d = {'a': 1, 'b': 2}
immutable_d = MappingProxyType(d)  # Read-only view of d

# 17. Dictionary Serialization Tricks
# ================================
# Convert dictionary to query string
from urllib.parse import urlencode
params = {'q': 'python', 'page': 1}
query_string = urlencode(params)  # 'q=python&page=1'

# 18. Dictionary Pattern Matching (Python 3.10+)
# ===========================================
match d:
    case {'a': 1, 'b': 2}:
        print("Exact match")
    case {'a': 1, **rest}:
        print(f"Partial match with rest: {rest}")

# 19. Dictionary Cache Trick
# ========================
# Simple memoization decorator
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# 20. Dictionary Switch-Case Trick
# ==============================
def switch_case(value):
    return {
        'case1': lambda: 'result1',
        'case2': lambda: 'result2',
        'case3': lambda: 'result3'
    }.get(value, lambda: 'default')()

# Usage
result = switch_case('case1')  # Returns 'result1'

# =============================================
# COMPREHENSIVE PYTHON DICTIONARY GUIDE
# =============================================

# 1. Dictionary Fundamentals
# =========================
"""
A dictionary in Python is:
- An unordered collection of key-value pairs
- Mutable (can be changed)
- Keys must be unique and immutable
- Values can be of any type
- Implemented as a hash table
"""

# 2. Dictionary Creation
# ====================
# Empty dictionary
empty_dict = {}

# Dictionary with initial values
d = {'key1': 'value1', 'key2': 'value2'}

# Using dict() constructor
d = dict(key1='value1', key2='value2')

# From list of tuples
d = dict([('key1', 'value1'), ('key2', 'value2')])

# From two lists
keys = ['key1', 'key2']
values = ['value1', 'value2']
d = dict(zip(keys, values))

# Dictionary comprehension
d = {x: x ** 2 for x in range(5)}

# 3. Dictionary Access
# ==================
d = {'a': 1, 'b': 2, 'c': 3}

# Basic access
value = d['a']  # Raises KeyError if key doesn't exist

# Safe access
value = d.get('a')  # Returns None if key doesn't exist
value = d.get('z', 'default')  # Returns 'default' if key doesn't exist

# Check key existence
if 'a' in d:
    print("Key exists")

# 4. Dictionary Modification
# ========================
# Add/Update
d['d'] = 4  # Add new key-value pair
d.update({'e': 5, 'f': 6})  # Update multiple pairs

# Remove
del d['a']  # Remove key-value pair
value = d.pop('b')  # Remove and return value
item = d.popitem()  # Remove and return last item
d.clear()  # Remove all items

# 5. Dictionary Methods
# ===================
# Basic methods
keys = d.keys()  # Get all keys
values = d.values()  # Get all values
items = d.items()  # Get all items
length = len(d)  # Get number of items
copy = d.copy()  # Create shallow copy

# 6. Dictionary Views
# =================
# Views are dynamic
keys_view = d.keys()
values_view = d.values()
items_view = d.items()

# Views support set operations
other_keys = {'a', 'b', 'c'}
common_keys = keys_view & other_keys

# 7. Dictionary Iteration
# =====================
# Iterate keys
for key in d:
    print(key)

# Iterate values
for value in d.values():
    print(value)

# Iterate items
for key, value in d.items():
    print(f"{key}: {value}")

# 8. Dictionary Comprehension
# =========================
# Basic
squares = {x: x ** 2 for x in range(5)}

# With condition
even_squares = {x: x ** 2 for x in range(5) if x % 2 == 0}

# Nested
nested = {x: {y: x * y for y in range(3)} for x in range(3)}

# 9. Dictionary Merging
# ===================
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Update method
merged = dict1.copy()
merged.update(dict2)

# Dictionary unpacking (Python 3.5+)
merged = {**dict1, **dict2}

# Union operator (Python 3.9+)
merged = dict1 | dict2

# 10. Dictionary Sorting
# ====================
d = {'b': 2, 'a': 1, 'c': 3}

# Sort by keys
sorted_by_key = dict(sorted(d.items()))

# Sort by values
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))

# 11. Dictionary Default Values
# ===========================
from collections import defaultdict

# Using setdefault
d = {}
d.setdefault('a', []).append(1)

# Using defaultdict
dd = defaultdict(list)
dd['a'].append(1)

# 12. Dictionary Performance
# ========================
"""
Time Complexity:
- Lookup: O(1) average, O(n) worst
- Insert: O(1) average, O(n) worst
- Delete: O(1) average, O(n) worst
- Update: O(1) average, O(n) worst

Space Complexity: O(n)
"""


# 13. Dictionary Memory Optimization
# ===============================
# Use __slots__ for memory optimization
class OptimizedDict:
    __slots__ = ['a', 'b', 'c']

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


# 14. Dictionary Serialization
# =========================
import json
import pickle

# JSON serialization
json_str = json.dumps(d)
d_from_json = json.loads(json_str)

# Pickle serialization
pickle_str = pickle.dumps(d)
d_from_pickle = pickle.loads(pickle_str)


# 15. Dictionary Customization
# =========================
class CustomDict(dict):
    def __missing__(self, key):
        return f"Key {key} not found"

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.__missing__(key)


# 16. Dictionary Best Practices
# ==========================
# Use get() for safe access
value = d.get('key', default_value)

# Use setdefault() for initialization
d.setdefault('key', []).append(value)

# Use defaultdict for default values
dd = defaultdict(list)

# Use dict comprehension for transformations
transformed = {k: f(v) for k, v in d.items()}

# 17. Dictionary Common Patterns
# ===========================
# Group by
from collections import defaultdict

grouped = defaultdict(list)
for item in items:
    grouped[key].append(item)

# Counter
from collections import Counter

counts = Counter(items)

# 18. Dictionary Error Handling
# ==========================
try:
    value = d['nonexistent']
except KeyError:
    value = 'default'

# Using get() for safe access
value = d.get('nonexistent', 'default')

# 19. Dictionary Thread Safety
# =========================
from threading import Lock

lock = Lock()

with lock:
    d['key'] = 'value'

# 20. Dictionary Use Cases
# ======================
"""
Common Use Cases:
1. Configuration storage
2. Data mapping
3. Caching
4. Counting occurrences
5. Grouping data
6. Function arguments
7. Object attributes
8. Database records
9. API responses
10. State management
"""

# 21. Dictionary Limitations
# ========================
"""
Limitations:
1. Keys must be immutable
2. No guaranteed order (use OrderedDict for order)
3. Not thread-safe by default
4. Memory overhead
5. Hash collisions possible
"""

# 22. Dictionary Alternatives
# =========================
"""
Alternatives:
1. collections.defaultdict
2. collections.OrderedDict
3. collections.Counter
4. types.MappingProxyType
5. dataclasses
6. namedtuple
7. SimpleNamespace
"""

# 23. Dictionary Debugging
# ======================
# Pretty print
import pprint

pprint.pprint(d)

# Print sorted
for k in sorted(d):
    print(f"{k}: {d[k]}")

# 24. Dictionary Testing
# ====================
# Test key existence
assert 'key' in d
assert 'nonexistent' not in d

# Test value existence
assert 'value' in d.values()

# 25. Dictionary Documentation
# =========================
"""
Documentation Best Practices:
1. Document key-value types
2. Document expected values
3. Document side effects
4. Document thread safety
5. Document performance characteristics
"""

# =============================================
# PYTHON DICTIONARY ONE-LINERS
# =============================================

# 1. Dictionary Creation
# ====================
d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # Create from lists
d = {x: x**2 for x in range(5)}  # Comprehension
d = dict.fromkeys(['a', 'b', 'c'], 0)  # Same value for all keys

# 2. Dictionary Access
# ==================
value = d.get('key', 'default')  # Safe access with default
value = d.setdefault('key', 'default')  # Set if not exists
exists = 'key' in d  # Check key existence

# 3. Dictionary Update
# ==================
d.update({'new': 'value'})  # Update with another dict
d |= {'new': 'value'}  # Update with | operator (Python 3.9+)
d = {**d, **{'new': 'value'}}  # Merge dictionaries

# 4. Dictionary Filter
# ==================
filtered = {k: v for k, v in d.items() if v > 0}  # Filter by value
filtered = {k: v for k, v in d.items() if k.startswith('a')}  # Filter by key
filtered = {k: v for k, v in d.items() if k in ['a', 'b']}  # Filter by key list

# 5. Dictionary Transform
# =====================
transformed = {k.upper(): v*2 for k, v in d.items()}  # Transform keys and values
inverted = {v: k for k, v in d.items()}  # Invert dictionary
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))  # Sort by value

# 6. Dictionary Statistics
# ======================
max_key = max(d, key=d.get)  # Key with max value
min_key = min(d, key=d.get)  # Key with min value
total = sum(d.values())  # Sum of all values

# 7. Dictionary Grouping
# ====================
from collections import defaultdict
grouped = defaultdict(list, {k: [v] for k, v in items})  # Group by key

# 8. Dictionary Counter
# ===================
from collections import Counter
counts = Counter(items)  # Count occurrences

# 9. Dictionary Default Values
# =========================
from collections import defaultdict
dd = defaultdict(lambda: 'default')  # Default value factory

# 10. Dictionary Nested Access
# =========================
value = d.get('a', {}).get('b', {}).get('c')  # Safe nested access

# 11. Dictionary Remove
# ===================
d = {k: v for k, v in d.items() if k != 'remove'}  # Remove key
d = {k: v for k, v in d.items() if v != 0}  # Remove by value

# 12. Dictionary Unique Values
# =========================
unique_values = set(d.values())  # Get unique values
unique_keys = set(d.keys())  # Get unique keys

# 13. Dictionary Length
# ===================
length = len(d)  # Number of items
is_empty = not d  # Check if empty

# 14. Dictionary Copy
# =================
import copy
deep_copy = copy.deepcopy(d)  # Deep copy
shallow_copy = d.copy()  # Shallow copy

# 15. Dictionary Merge
# ==================
merged = {**d1, **d2}  # Merge two dictionaries
merged = d1 | d2  # Merge with | operator (Python 3.9+)

# 16. Dictionary Sort
# =================
sorted_by_key = dict(sorted(d.items()))  # Sort by key
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))  # Sort by value

# 17. Dictionary Max/Min
# ====================
max_value = max(d.values())  # Max value
min_value = min(d.values())  # Min value
max_key = max(d, key=d.get)  # Key with max value

# 18. Dictionary Sum/Average
# ========================
total = sum(d.values())  # Sum of values
average = sum(d.values()) / len(d)  # Average of values

# 19. Dictionary Check
# ==================
all_positive = all(v > 0 for v in d.values())  # Check all values
any_negative = any(v < 0 for v in d.values())  # Check any value

# 20. Dictionary Format
# ===================
formatted = {k: f"${v:.2f}" for k, v in d.items()}  # Format values

# =============================================
# COMPREHENSIVE DICTIONARY OPERATIONS GUIDE
# =============================================

# 1. Dictionary Loops
# =================
d = {'a': 1, 'b': 2, 'c': 3}

# Basic loops
for key in d:  # Loop through keys
    print(key)

for value in d.values():  # Loop through values
    print(value)

for key, value in d.items():  # Loop through items
    print(f"{key}: {value}")

# Advanced loops
for i, key in enumerate(d):  # Loop with index
    print(f"{i}: {key}")

for key in reversed(d):  # Loop in reverse
    print(key)

for key in sorted(d):  # Loop in sorted order
    print(key)

# Nested loops
nested = {'a': {'x': 1}, 'b': {'y': 2}}
for outer_key, inner_dict in nested.items():
    for inner_key, value in inner_dict.items():
        print(f"{outer_key}.{inner_key}: {value}")

# 2. Dictionary Operations
# ======================
# Basic operations
d['new'] = 4  # Add/Update
del d['a']  # Delete
value = d.get('b')  # Get with default
d.clear()  # Clear all

# Advanced operations
d.update({'d': 4, 'e': 5})  # Update multiple
d.pop('b')  # Remove and return
d.popitem()  # Remove last item
d.setdefault('f', 6)  # Set if not exists

# 3. Dictionary Comprehensions
# ==========================
# Basic comprehension
squares = {x: x ** 2 for x in range(5)}

# With condition
even_squares = {x: x ** 2 for x in range(5) if x % 2 == 0}

# Nested comprehension
nested = {x: {y: x * y for y in range(3)} for x in range(3)}

# With walrus operator (Python 3.8+)
{(x := x ** 2): x for x in range(5)}

# 4. Dictionary Methods
# ===================
# Basic methods
keys = d.keys()  # Get keys
values = d.values()  # Get values
items = d.items()  # Get items
length = len(d)  # Get length
copy = d.copy()  # Create copy

# Advanced methods
d.update({'g': 7})  # Update
d.pop('h', None)  # Remove with default
d.popitem()  # Remove last
d.clear()  # Clear all

# 5. Dictionary Views
# =================
# View objects
keys_view = d.keys()
values_view = d.values()
items_view = d.items()

# View operations
len(keys_view)  # Length
'a' in keys_view  # Membership
iter(keys_view)  # Iterator

# 6. Dictionary Sorting
# ===================
# Sort by key
sorted_by_key = dict(sorted(d.items()))

# Sort by value
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))

# Sort by multiple criteria
sorted_multi = dict(sorted(d.items(), key=lambda x: (x[1], x[0])))

# 7. Dictionary Filtering
# =====================
# Filter by value
filtered = {k: v for k, v in d.items() if v > 2}

# Filter by key
filtered = {k: v for k, v in d.items() if k in ['a', 'c']}

# Filter by both
filtered = {k: v for k, v in d.items() if k in ['a', 'c'] and v > 2}

# 8. Dictionary Transformations
# ===========================
# Transform keys
transformed = {k.upper(): v for k, v in d.items()}

# Transform values
transformed = {k: v * 2 for k, v in d.items()}

# Transform both
transformed = {k.upper(): v * 2 for k, v in d.items()}

# 9. Dictionary Merging
# ===================
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge methods
merged = dict1.copy()
merged.update(dict2)  # Method 1

merged = {**dict1, **dict2}  # Method 2 (Python 3.5+)

merged = dict1 | dict2  # Method 3 (Python 3.9+)

# 10. Dictionary Default Values
# ===========================
from collections import defaultdict

# Using setdefault
d = {}
d.setdefault('a', []).append(1)

# Using defaultdict
dd = defaultdict(list)
dd['a'].append(1)

# 11. Dictionary Statistics
# =======================
# Basic statistics
max_value = max(d.values())
min_value = min(d.values())
total = sum(d.values())
average = sum(d.values()) / len(d)

# Advanced statistics
max_key = max(d, key=d.get)
min_key = min(d, key=d.get)
unique_values = set(d.values())

# 12. Dictionary Grouping
# =====================
from collections import defaultdict

# Group by value
grouped = defaultdict(list)
for k, v in d.items():
    grouped[v].append(k)

# 13. Dictionary Counter
# ====================
from collections import Counter

# Count occurrences
counts = Counter(d.values())


# 14. Dictionary Memory Operations
# =============================
# Memory efficient operations
class OptimizedDict:
    __slots__ = ['a', 'b', 'c']

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


# 15. Dictionary Serialization
# =========================
import json
import pickle

# JSON serialization
json_str = json.dumps(d)
d_from_json = json.loads(json_str)

# Pickle serialization
pickle_str = pickle.dumps(d)
d_from_pickle = pickle.loads(pickle_str)


# 16. Dictionary Customization
# =========================
class CustomDict(dict):
    def __missing__(self, key):
        return f"Key {key} not found"

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.__missing__(key)


# 17. Dictionary Thread Safety
# =========================
from threading import Lock

# Thread-safe operations
lock = Lock()
with lock:
    d['key'] = 'value'

# 18. Dictionary Pattern Matching (Python 3.10+)
# ===========================================
match d:
    case {'a': 1, 'b': 2}:
        print("Exact match")
    case {'a': 1, **rest}:
        print(f"Partial match with rest: {rest}")


# 19. Dictionary Cache
# ==================
# Simple memoization
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


# 20. Dictionary Switch-Case
# ========================
def switch_case(value):
    return {
        'case1': lambda: 'result1',
        'case2': lambda: 'result2',
        'case3': lambda: 'result3'
    }.get(value, lambda: 'default')()
