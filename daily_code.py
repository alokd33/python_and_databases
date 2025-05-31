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

def charcount(str1): 
    """
    input : abcabc 
    output :a2b3c3 
    """
    d1 = {}
    for i in str1:
        if i in d1 : 
            d1[i] = d1[i] + 1
        else : 
            d1[i] = 1
    return "".join([str(k)+str(v) for k,v in d1.items()])

# str1 = "abcabc"
# #str1 = "111111111"
# a = charcount(str1)
# print(a)

# loops type

a = [1,2,3,5,"a", 5]
a.append(6)
print(a)

a.insert(1, 0)
print(a)

b = a.pop()
print(b, a)

print ("5 count is", a.count(5)) 
print ("5 index is", a.index(5))

a.reverse()
c = a.reverse()
print ("d reserved the list", c)

a.reverse()

d = {"a": 1, "b": 2, "c": 3}
#print(d)

# str1 = "abcabc"
# #str1 = "111111111"
# a = charcount(str1)
# print(a)

def charcount(str1):
    d = {}
    for i in str1 : 
        if i in d : 
            d[i] = d[i] + 1
        else : 
            d[i] = 1 
    str2 = "".join([(str(k)+str(v)) for k,v in d.items()])
    return str2
     
str1 = "abcabc"
#str1 = "111111111"
a = charcount(str1)
print(a)

def isvalid_brackets(str1): 
    d = {}
    open_bracket = ("{", "[", ")")
    end_bracket = ("}", "]", ")")


def reverse_string(s: str) -> str:
    """
    Reverses the input string.

    Args:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return s[::-1]

print(reverse_string("hello"))  # Output: "olleh"


def is_prime(n: int) -> bool:
    """
    Checks if the given number is prime.

    Args:
    n (int): The number to be checked.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  # Output: True

def find_largest(numbers: list) -> int:
    """
    Returns the largest number from the list.

    Args:
    numbers (list): A list of numbers.

    Returns:
    int: The largest number in the list.
    """
    return max(numbers)

print(find_largest([1, 2, 3, 4, 5]))  # Output: 5

squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares)  # Output: [4, 16, 36, 64, 100]

#Write a lambda function that multiplies a number by 2.
multiply_by_two = lambda x: x * 2

# Write a function that divides two numbers and handles division by zero.

def divide(a: float, b: float) -> float:
    """
    Divides a by b and handles division by zero.

    Args:
    a (float): The numerator.
    b (float): The denominator.

    Returns:
    float: The result of the division, or None if division by zero occurs.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: None

# Write a decorator that prints the arguments of a function before calling it.

def print_args(func):
    """
    Decorator that prints function arguments before calling the function.

    Args:
    func (function): The function to be decorated.

    Returns:
    function: The decorated function.
    """
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@print_args
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Arguments: ('Alice',), {} \n Hello, Alice!


#Write a generator that yields numbers from 1 to 5.

def count_up_to_five():
    """
    Generator that yields numbers from 1 to 5.

    Yields:
    int: Numbers from 1 to 5.
    """
    for i in range(1, 6):
        yield i

for number in count_up_to_five():
    print(number)

#Explain the Global Interpreter Lock (GIL) in Python.

"""The GIL is a mutex that protects access to Python objects, preventing multiple threads from 
    executing Python bytecode simultaneously. This means that even in a multi-threaded program, 
    only one thread can execute Python code at a time. The GIL can be a bottleneck in CPU-bound programs but
    is less of an issue for I/O-bound programs.
"""
#What is PEP 8 and why is it important

# Solution:
# PEP 8 is the style guide for Python code, covering formatting conventions such as indentation,
#     naming conventions, and code layout. Following PEP 8 improves code readability and consistency, 
# making it easier for developers to collaborate and maintain codebases.

# 1. Two Sum
# Problem:Given an array of integers nums and an integer target, return the 
# indices of the two numbers such that they add up to target


# Common imports for advanced or specialized data structures
from collections import (
    deque,             # Double-ended queue (used as stack/queue)
    Counter,           # Frequency map
    defaultdict,       # Dict with default factory
    OrderedDict,       # Remember insertion order (useful for LRU)
    namedtuple         # Lightweight class-like tuple
)
from heapq import heappush, heappop, heapify  # Min-heap (priority queue)
from queue import Queue, LifoQueue, PriorityQueue  # Thread-safe queues
from array import array  # Space-efficient array of uniform type
from typing import List, Dict, Set, Tuple, Any  # For type hinting
from collections.abc import Iterable, Iterator  # For OOP/data modeling

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Finds two indices in the list 'nums' such that their values add up to 'target'.

    Args:
    nums (List[int]): A list of integers.
    target (int): The target sum.

    Returns:
    List[int]: A list containing the indices of the two numbers.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

# 2. Add Two Numbers
# Problem:
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return it as a linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds two numbers represented by linked lists 'l1' and 'l2'.

    Args:
    l1 (ListNode): The first linked list.
    l2 (ListNode): The second linked list.

    Returns:
    ListNode: The sum of the two numbers as a linked list.
    """
    dummy = ListNode()
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

# Example usage requires creating ListNode instances for l1 and l2

# 3. Longest Substring Without Repeating Characters
# Problem:
# Given a string s, find the length of the longest substring without repeating characters.
# Coding Interview Pro
# +1
# Medium
# +1

# Solution:

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest substring.
    """
    char_map = {}
    start = max_length = 0
    for end, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length

print(length_of_longest_substring("abcabcbb"))  # Output: 3


# 4. Median of Two Sorted Arrays
# Problem:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, find the median of the two sorted arrays.

# Solution:

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Finds the median of two sorted arrays 'nums1' and 'nums2'.

    Args:
    nums1 (List[int]): The first sorted array.
    nums2 (List[int]): The second sorted array.

    Returns:
    float: The median of the two sorted arrays.
    """
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]
    
print(find_median_sorted_arrays([1, 3], [2]))  # Output: 2.0

# 5. Longest Palindromic Substring
# Problem:
# Given a string s, return the longest palindromic substring in s.

# Solution:
def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in 's'.

    Args:
    s (str): The input string.

    Returns:
    str: The longest palindromic substring.
    """
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    return longest

print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"

# 6. Merge Intervals
# Problem:
# Given a collection of intervals, merge any overlapping intervals.

# Solution:

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges overlapping intervals from the input list.

    Args:
    intervals (List[List[int]]): A list of intervals [start, end].

    Returns:
    List[List[int]]: The merged list of intervals.
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
# Output: [[1,6],[8,10],[15,18]]

 
# 7. Valid Parentheses
# Problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# Solution:
def safe_pop(stack):
    """
    Safely pops the top item from the stack.

    This function avoids errors that occur when trying to pop from an empty list.
    It uses a conditional expression to return the top element if available,
    or a sentinel character '#' if the stack is empty.

    Parameters
    ----------
    stack : list
        A list representing the stack of brackets.

    Returns
    -------
    str
        The last item in the stack (using stack.pop()) if the stack is non-empty,
        otherwise '#' as a placeholder to indicate an unmatched or missing opening bracket.

    Expression Breakdown
    --------------------
    top = stack.pop() if stack else '#'

    - `stack.pop()`: Removes and returns the top (last) element of the stack.
    - `if stack`: Checks if the stack is not empty (truthy check).
    - `else '#'`: If the stack is empty, return '#' instead of calling pop()
      to avoid an IndexError.

    This is a key safety measure in bracket-matching problems where
    we need to avoid popping from an empty stack.
    # Step 1: Check if the stack is non-empty
    if stack:
    # Step 2: Since the stack is not empty, pop the top item
    top = stack.pop()
    else:
    # Step 3: Stack is empty, assign a placeholder value
    top = '#'
    """
    return stack.pop() if stack else '#'


def safe_pop(stack):
    """
    Safely pops the top element from a stack (list).

    If the stack is not empty, returns the top element using pop().
    If the stack is empty, returns a placeholder '#'.

    Parameters
    ----------
    stack : list
        A list representing the stack.

    Returns
    -------
    any
        The popped element if the stack is non-empty, or '#' as a fallback.
    """
    # Step 1: Check if the stack is non-empty
    if stack:
        # Step 2: Pop the top item from the stack
        top = stack.pop()
    else:
        # Step 3: Stack is empty, return a placeholder
        top = '#'

    return top


# Test Cases
stack1 = ['(', '{']
result1 = safe_pop(stack1)
print("Test 1 (Non-empty stack):", result1)  # Expected: '{'

def is_valid_parentheses(s: str) -> bool:
    """
    Determines if the input string has valid matching parentheses.

    A valid string must meet the following conditions:
    - Every opening bracket must have a corresponding closing bracket of the same type.
    - Brackets must be closed in the correct order (e.g., "([])" is valid, but "(]" is not).

    Parameters
    ----------
    s : str
        A string containing only the characters '(', ')', '{', '}', '[' and ']'.

    Returns
    -------
    bool
        True if the parentheses are valid and balanced, False otherwise.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            # Step 1: Check if the stack is non-empty
            if stack:
                # Step 2: Since the stack is not empty, pop the top item
                top = stack.pop()
            else:
                # Step 3: Stack is empty, assign a placeholder value
                top = '#'

            # Step 4: Compare the popped value with expected opening bracket
            if mapping[char] != top:
                return False
        else:
            # Push opening brackets to stack
            stack.append(char)

    # Return True only if no unmatched brackets remain
    return not stack

a = is_valid_parentheses("{}")
print(a)
a = is_valid_parentheses("{")
print(a)



def is_valid_parentheses(s: str) -> bool:
    """
    Determines if the input string has valid matching parentheses.

    A valid string must meet the following conditions:
    - Every opening bracket must have a corresponding closing bracket of the same type.
    - Brackets must be closed in the correct order (e.g., "([])" is valid, but "(]" is not).

    Parameters
    ----------
    s : str
        A string containing only the characters '(', ')', '{', '}', '[' and ']'.

    Returns
    -------
    bool
        True if the parentheses are valid and balanced, False otherwise.

    Method Summary
    --------------
    - We use a stack to track unmatched opening brackets.
    - We use a dictionary (mapping) to check which closing bracket corresponds to which opening bracket.
    - For each character in the string:
        1. If it is a closing bracket:
            - Pop the top element of the stack (if any).
            - Compare it with the expected opening bracket using the `mapping`.
            - If it does not match, return False.
        2. If it is an opening bracket:
            - Push it onto the stack.
    - If, after processing all characters, the stack is empty, return True. Otherwise, return False.

    Core Loop with Example
    -----------------------
    Let's say: s = "({[]})"

    Initial stack: []

    Looping through each character:

    for char in s:
        if char in mapping:
            # If it's a closing bracket, pop the top of the stack (if available)
            top = stack.pop() if stack else '#'

            # Check if the popped bracket matches the expected opening bracket
            if mapping[char] != top:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)

    Step-by-step:
    - char = '(': push → stack = ['(']
    - char = '{': push → stack = ['(', '{']
    - char = '[': push → stack = ['(', '{', '[']
    - char = ']': pop '[' → matches → stack = ['(', '{']
    - char = '}': pop '{' → matches → stack = ['(']
    - char = ')': pop '(' → matches → stack = []

    Stack is empty → return True

    Example Usages
    --------------
    >>> is_valid_parentheses("()[]{}")
    True

    >>> is_valid_parentheses("(]")
    False

    >>> is_valid_parentheses("({[]})")
    True
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack


print(is_valid_parentheses("()[]{}"))  # Output: True
print(is_valid_parentheses("(]"))      # Output: False

# 8. Search in Rotated Sorted Array
# Problem:
# Given the array nums which is sorted and then rotated, return the index of the target if found, or -1.

# Solution:

def search(nums: List[int], target: int) -> int:
    """
    Searches target in a rotated sorted array.

    Args:
    nums (List[int]): The rotated sorted array.
    target (int): The value to search.

    Returns:
    int: The index of target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print(search([4,5,6,7,0,1,2], 0))  # Output: 4

# 9. Container With Most Water
# Problem:
# Given n non-negative integers representing height, find two lines that 
# together with the x-axis form a container that holds the most water

def max_area(height: List[int]) -> int:
    """
    Finds the max area of water that can be trapped between two lines.

    Args:
    height (List[int]): A list of heights.

    Returns:
    int: The maximum area.
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

print(max_area([1,8,6,2,5,4,8,3,7]))  # Output: 49

# 10. Binary Tree Level Order Traversal
# Problem:
# Given the root of a binary tree, return its level order traversal (i.e., values at each level from left to right).

# Solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a binary tree node.

        Args:
        val (int): The value of the node.
        left (TreeNode, optional): Left child node.
        right (TreeNode, optional): Right child node.
        """
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode) -> List[List[int]]:
    """
    Performs level-order traversal (BFS) on a binary tree without using any imports.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    List[List[int]]: A list where each sublist contains the values of nodes at each level.
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        level_values = []

        for i in range(level_size):
            current = queue.pop(0)
            level_values.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        result.append(level_values)

    return result

# Constructing the binary tree:
#     3
#    / \
#   9  20
#      / \
#     15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(level_order(root))
# Output: [[3], [9, 20], [15, 7]]




# 1. Maximum Depth of a Binary Tree
# Problem:
# Given a binary tree, find its maximum depth. 
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a binary tree node.

        Args:
        val (int): The value of the node.
        left (TreeNode, optional): Left child node.
        right (TreeNode, optional): Right child node.
        """
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    """
    Computes the maximum depth of a binary tree.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    int: The maximum depth of the tree.
    """
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1


# Constructing the binary tree:
#     3
#    / \
#   9  20
#      / \
#     15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(max_depth(root))  # Output: 3

# 2. Lowest Common Ancestor of a Binary Tree
# Problem:
# Given a binary tree and two nodes, find their lowest common ancestor (LCA). The LCA is defined as the lowest node in the tree that has both nodes as descendants.

# Solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a binary tree node.

        Args:
        val (int): The value of the node.
        left (TreeNode, optional): Left child node.
        right (TreeNode, optional): Right child node.
        """
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor of two nodes in a binary tree.

    Args:
    root (TreeNode): The root node of the binary tree.
    p (TreeNode): The first node.
    q (TreeNode): The second node.

    Returns:
    TreeNode: The lowest common ancestor of the two nodes.
    """
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

# Constructing the binary tree:
#     3
#    / \
#   5   1
#  / \ / \
# 6  2 0  8
#   / \
#  7   4

root = TreeNode(3)
root.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
root.right = TreeNode(1, TreeNode(0), TreeNode(8))

p = root.left  # Node 5
q = root.left.right.right  # Node 4

print(lowest_common_ancestor(root, p, q).val)  # Output: 5


# 3. Binary Tree Zigzag Level Order Traversal
# Problem:
# Given a binary tree, return the zigzag level order traversal of its nodes' 
# values. (i.e., from left to right, then right to left for the next level and alternate between).

# Solution:
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a binary tree node.

        Args:
        val (int): The value of the node.
        left (TreeNode, optional): Left child node.
        right (TreeNode, optional): Right child node.
        """
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    """
    Performs a zigzag level order traversal of a binary tree.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    List[List[int]]: A list of lists representing the zigzag level order traversal.
    """
    if not root:
        return []

    result, level, direction = [], [root], 1

    while level:
        current_vals = [node.val for node in level]
        if direction == -1:
            current_vals.reverse()
        result.append(current_vals)

        direction *= -1
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level

    return result

# Constructing the binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(zigzag_level_order(root))  
# Output: [[3], [20, 9], [15, 7]]


# 3. Group Anagrams
# Problem:
# Given an array of strings, group the anagrams together.

# Solution:

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams from the given list of strings.

    Args:
    strs (List[str]): The input list of strings.

    Returns:
    List[List[str]]: A list of groups where each group contains anagrams.
    """
    anagram_map = {}  # Dictionary to store sorted word as key and list of words as value

    for word in strs:
        key = ''.join(sorted(word))  # Sort the characters of the word
        if key in anagram_map:
            anagram_map[key].append(word)
        else:
            anagram_map[key] = [word]

    return list(anagram_map.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Possible output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# 1. Find the First Repeating Element in an Array
# Problem:
# Given an integer array, find the first repeating element.
# Medium

# Solution:

def find_first_repeating(arr):
    """
    Finds the first repeating element in an array.

    Args:
    arr (List[int]): The input array.

    Returns:
    int: The first repeating element, or None if no such element exists.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None

print(find_first_repeating([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))  # Output: 1


# 2. Find the Union of Two Arrays
# Problem:
# Given two integer arrays, find the union of the two arrays.

# Solution:
def find_union(arr1, arr2):
    """
    Finds the union of two arrays.

    Args:
    arr1 (List[int]): The first input array.
    arr2 (List[int]): The second input array.

    Returns:
    List[int]: A list containing the union of the two arrays.
    """
    return list(set(arr1) | set(arr2))
print(find_union([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]


# 3. Find the Intersection of Two Arrays
# Problem:
# Given two integer arrays, find the intersection of the two arrays.

# Solution:

def find_intersection(arr1, arr2):
    """
    Finds the intersection of two arrays.

    Args:
    arr1 (List[int]): The first input array.
    arr2 (List[int]): The second input array.

    Returns:
    List[int]: A list containing the intersection of the two arrays.
    """
    return list(set(arr1) & set(arr2))

print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]


# 1. Swap Two Variables Using Tuple Packing/Unpacking
# Problem:
# Swap the values of two variables without using a temporary variable. Use tuple unpacking to achieve this.

# Constraints:

# Inputs are integers.

def swap(a: int, b: int) -> Tuple[int, int]:
    """
    Swaps two integers using tuple packing and unpacking.

    Args:
    a (int): First integer.
    b (int): Second integer.

    Returns:
    Tuple[int, int]: A tuple containing the swapped values (b, a).
    """
    a, b = b, a
    return a, b

print(swap(5, 10))  # Output: (10, 5)


# 2. Find the Tuple with Maximum Sum from a List of Tuples
# Problem:
# Given a list of tuples where each tuple contains integers, return the tuple whose elements sum to the largest value.

# Constraints:

# The list will contain at least one tuple.

# Tuples can contain any number of integers (1 or more).



from typing import List, Tuple, Dict

def count_tuple_frequency(tuples_list: List[Tuple]) -> Dict[Tuple, int]:
    """
    Counts the frequency of each tuple in the given list.

    Args:
        tuples_list (List[Tuple]): List of tuples.

    Returns:
        Dict[Tuple, int]: Dictionary mapping each tuple to its frequency.
    """
    frequency = {}
    for t in tuples_list:
        frequency[t] = frequency.get(t, 0) + 1
    return frequency

# Test
print(count_tuple_frequency([(1, 2), (3, 4), (1, 2), (0, 5), (3, 4), (3, 4)]))
# Output: {(1, 2): 2, (3, 4): 3, (0, 5): 1}


# Test
# print(max_sum_tuple([(1, 2), (3, 4), (0, 5)]))  # Output: (3, 4)



# 3. Count Frequency of Tuples in a List
# Problem:
# Given a list of tuples, count how many times each tuple appears and return a dictionary mapping each tuple to its frequency.

# Constraints:

# The list can contain any number of tuples (including duplicates).

# Tuples can contain any types of hashable elements.

def count_tuple_frequency(tuples_list: List[Tuple]) -> Dict[Tuple, int]:
    """
    Counts the frequency of each tuple in the given list.

    Args:
    tuples_list (List[tuple]): List of tuples.

    Returns:
    dict[tuple, int]: Dictionary mapping each tuple to its frequency.
    """
    frequency = {}
    for t in tuples_list:
        if t in frequency:
            frequency[t] += 1
        else:
            frequency[t] = 1
    return frequency

print(count_tuple_frequency([(1, 2), (3, 4), (1, 2), (5, 6)]))
# Output: {(1, 2): 2, (3, 4): 1, (5, 6): 1}

# 1. Merge Two Dictionaries
# Problem:
# Given two dictionaries, merge them into a single dictionary. If keys overlap, values from the second dictionary should override those from the first.

# Function Signature:

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dictionaries. If keys overlap, values from dict2 override dict1.

    Args:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.

    Returns:
    dict: The merged dictionary.
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# Output: {'a': 1, 'b': 3, 'c': 4}

# 2. Count Frequency of Characters in a String
# Problem:
# Given a string, count the frequency of each character using a dictionary.

# Function Signature:

def char_frequency(s: str) -> dict:
    """
    Counts the frequency of each character in the string.

    Args:
    s (str): Input string.

    Returns:
    dict: Dictionary with characters as keys and their frequencies as values.
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
print(char_frequency("hello"))
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# 3. Find the Key with Maximum Value in a Dictionary
# Problem:
# Given a dictionary, find the key that has the maximum value.

# Function Signature:
def key_with_max_value(d: dict) -> any:
    """
    Returns the key with the maximum value in the dictionary.

    Args:
    d (dict): Input dictionary.

    Returns:
    any: Key with the highest value.
    """
    if not d:
        return None
    max_key = max(d, key=d.get)
    return max_key
print(key_with_max_value({'a': 5, 'b': 12, 'c': 7}))
# Output: 'b'

# 4. Invert a Dictionary (Swap Keys and Values)
# Problem:
# Given a dictionary, invert it by swapping keys and values. Assume all values are unique and hashable.

# Function Signature:
def invert_dict(d: dict) -> dict:
    """
    Inverts the dictionary by swapping keys and values.

    Args:
    d (dict): Input dictionary with unique values.

    Returns:
    dict: Inverted dictionary with values as keys and keys as values.
    """
    return {v: k for k, v in d.items()}

# 5. Check if Two Dictionaries are Equal
# Problem:
# Write a function to check if two dictionaries are equal (same keys and values).

# Function Signature:
def are_dicts_equal(d1: dict, d2: dict) -> bool:
    """
    Checks if two dictionaries are equal.

    Args:
    d1 (dict): First dictionary.
    d2 (dict): Second dictionary.

    Returns:
    bool: True if both dictionaries are equal, False otherwise.
    """
    return d1 == d2
print(are_dicts_equal({'a': 1, 'b': 2}, {'b': 2, 'a': 1}))
# Output: True
print(are_dicts_equal({'a': 1}, {'a': 2}))
# Output: False


# 1. Implement a Python Class with Getters and Setters
# Problem:
# Create a class Person with private attributes name and age.
# Implement getter and setter methods for these attributes to ensure encapsulation.
class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        """Returns the name of the person."""
        return self.__name

    def set_name(self, name: str):
        """Sets the name of the person."""
        self.__name = name

    def get_age(self) -> int:
        """Returns the age of the person."""
        return self.__age

    def set_age(self, age: int):
        """Sets the age of the person."""
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Age cannot be negative.")

p = Person("Alice", 30)
print(p.get_name())  # Output: Alice
p.set_age(31)
print(p.get_age())   # Output: 31


# 2. Implement a Class Method and Static Method
# Problem:
# Create a class Circle that keeps track of the number of circle instances created.
#  Implement a class method to get this count and a static method to calculate the area of a circle given its radius.
import math

class Circle:
    count = 0

    def __init__(self, radius: float):
        self.radius = radius
        Circle.count += 1

    @classmethod
    def get_count(cls) -> int:
        """Returns the total number of Circle instances."""
        return cls.count

    @staticmethod
    def area(radius: float) -> float:
        """Calculates area of a circle with given radius."""
        return math.pi * radius ** 2

c1 = Circle(3)
c2 = Circle(4)
print(Circle.get_count())       # Output: 2
print(Circle.area(5))           # Output: 78.53981633974483

# 3. Implement Inheritance and Method Overriding
# Problem:
# Create a base class Animal with a method speak. 
# Derive a class Dog from Animal and override the speak method to print "Woof!".

class Animal:
    def speak(self):
        """Base speak method."""
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        """Override speak method for Dog."""
        print("Woof!")
a = Animal()
a.speak()  # Output: Animal speaks

d = Dog()
d.speak()  # Output: Woof!


# 1. Design a Simple Hash Function for Strings
# Problem:
# Implement a simple hash function that takes a string input and 
# returns an integer hash value. Use a basic polynomial rolling hash approach.

def simple_hash(s: str, base: int = 31, mod: int = 10**9 + 7) -> int:
    """
    Computes a simple polynomial rolling hash for the given string.

    Args:
    s (str): Input string.
    base (int): Base multiplier for the polynomial rolling hash.
    mod (int): Modulus to avoid large numbers.

    Returns:
    int: Hash value of the string.
    """
    hash_value = 0
    power = 1
    for char in s:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * power) % mod
        power = (power * base) % mod
    return hash_value

print(simple_hash("hello"))  # Output: Some integer hash value
print(simple_hash("world"))  # Output: Different integer hash value


# 2. Implement a Custom Hash Map with Separate Chaining
# Problem:
# Implement a basic hash map supporting insert, 
# search, and delete operations using separate chaining (linked lists) for collision resolution

class MyHashMap:
    def __init__(self, size: int = 1000):
        """
        Initialize the hash map with given bucket size.
        """
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key: int) -> int:
        """
        Hash function to map keys to bucket index.
        """
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the key with the given value.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Return the value to which the specified key is mapped, or -1 if none.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Remove the mapping for the specified key if it exists.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


hash_map = MyHashMap()
hash_map.put(1, 100)
hash_map.put(2, 200)
print(hash_map.get(1))  # Output: 100
hash_map.remove(1)
print(hash_map.get(1))  # Output: -1

# 3. Detect Duplicate Substrings of Size K Using Hashing
# Problem:
# Given a string s and an integer k, determine if the string contains any duplicate substring of length k.

# Function Signature:

def has_duplicate_substring(s: str, k: int) -> bool:
    """
    Uses rolling hash to detect duplicate substrings of length k in s.

    Args:
    s (str): Input string.
    k (int): Length of substrings to check.

    Returns:
    bool: True if duplicate substring exists, False otherwise.
    """
    if k == 0 or k > len(s):
        return False

    base = 26
    mod = 2**63 - 1  # large prime modulus
    hash_set = set()
    hash_val = 0
    power = 1

    # Initial hash for first k-length substring
    for i in range(k):
        hash_val = (hash_val * base + ord(s[i]) - ord('a')) % mod
        if i < k - 1:
            power = (power * base) % mod

    hash_set.add(hash_val)

    for i in range(k, len(s)):
        # Remove leading char and add trailing char
        hash_val = ((hash_val - (ord(s[i-k]) - ord('a')) * power) * base + (ord(s[i]) - ord('a'))) % mod
        if hash_val in hash_set:
            return True
        hash_set.add(hash_val)

    return False

print(has_duplicate_substring("banana", 2))  # Output: True ("an" repeats)
print(has_duplicate_substring("abcdef", 3))  # Output: False

# 1. Find the First Non-Repeating Character in a String
# Problem:
# Given a string, find the first character that does not repeat anywhere in the string. 
# Return its index or -1 if it doesn't exist.
# Why people fail:
# Missing edge cases (empty string, all repeating chars) or returning the character instead of the index.

def first_non_repeating_char(s: str) -> int:
    """
    Finds the index of the first non-repeating character in the string.

    Args:
    s (str): Input string.

    Returns:
    int: Index of first unique char or -1 if none found.
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

# Example execution:
print(first_non_repeating_char("leetcode"))  # Output: 0 ('l')
print(first_non_repeating_char("aabbcc"))    # Output: -1 (no unique char)

# 2. Reverse Words in a String
# Problem:
# Given a string containing words separated by spaces, reverse the order of the words.
# Why people fail:
# They don’t handle extra spaces correctly or reverse the characters in words instead of the word order.
def reverse_words(s: str) -> str:
    """
    Reverses the order of words in a string.

    Args:
    s (str): Input string.

    Returns:
    str: String with words in reverse order.
    """
    words = s.strip().split()
    return ' '.join(words[::-1])

# Example execution:
print(reverse_words("the sky is blue"))     # Output: "blue is sky the"
print(reverse_words("  hello world  "))     # Output: "world hello"
# 3. Check if a Number is a Power of Two
# Problem:
# Given an integer, check if it is a power of two.
# Why people fail:
# Not handling zero or negative numbers properly, or using slow methods like loops instead of bitwise ops.

def is_power_of_two(n: int) -> bool:
    """
    Checks if n is a power of two.

    Args:
    n (int): Number to check.

    Returns:
    bool: True if n is power of two, False otherwise.
    """
    return n > 0 and (n & (n - 1)) == 0

# Example execution:
print(is_power_of_two(16))   # Output: True
print(is_power_of_two(18))   # Output: False
print(is_power_of_two(0))    # Output: False


# 4. Check if Two Strings are Anagrams
# Problem:
# Check if two strings are anagrams (contain the same characters in any order).
# Why people fail:
# Forgetting to handle case sensitivity, spaces, or not using efficient solutions.
def are_anagrams(s1: str, s2: str) -> bool:
    """
    Returns True if s1 and s2 are anagrams.

    Args:
    s1 (str): First string.
    s2 (str): Second string.

    Returns:
    bool: True if anagrams, False otherwise.
    """
    return sorted(s1) == sorted(s2)

# Example execution:
print(are_anagrams("listen", "silent"))    # Output: True
print(are_anagrams("hello", "world"))      # Output: Fals

# 5. Remove Duplicates from a List While Preserving Order
# Problem:
# Given a list, remove duplicates but keep the original order of elements.
# Why people fail:
# Using set() directly which loses order or inefficiently checking duplicates inside nested loops.
def remove_duplicates(lst: list) -> list:
    """
    Removes duplicates while preserving order.

    Args:
    lst (list): Input list.

    Returns:
    list: List without duplicates.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
# Example execution:
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(remove_duplicates(['a', 'b', 'a', 'c']))    # Output: ['a', 'b', 'c']


# 1. Valid Parentheses
# Problem:
# Given a string containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid. An input string is valid if:

# Open brackets are closed by the same type of brackets.

# Open brackets are closed in the correct order.

def is_valid_parentheses(s: str) -> bool:
    """
    Checks if the input string of brackets is valid.

    Args:
    s (str): String containing brackets.

    Returns:
    bool: True if valid, False otherwise.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Ignore non-bracket characters or return False
            return False
    return not stack

print(is_valid_parentheses("()[]{}"))  # Output: True
print(is_valid_parentheses("(]"))      # Output: False

# 2. Min Stack (Stack that returns minimum element in O(1))
# Problem:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Function Signature:
class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push onto min_stack if empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
    

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.get_min())  # Output: -2

# 3. Evaluate Reverse Polish Notation
# Problem:
# Evaluate the value of an arithmetic expression in Reverse Polish Notation. 
# Valid operators are +, -, *, and /.

def eval_rpn(tokens: List[str]) -> int:
    """
    Evaluates the value of an arithmetic expression in Reverse Polish Notation.

    Args:
    tokens (List[str]): List of tokens (operands and operators).

    Returns:
    int: Result of expression.
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                # Division truncates toward zero
                stack.append(int(a / b))
    return stack[0] if stack else 0

print(eval_rpn(["2", "1", "+", "3", "*"]))      # Output: 9
print(eval_rpn(["4", "13", "5", "/", "+"]))     # Output: 6

# 2. Min Stack
# Problem:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    
    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

# Example:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # -3
min_stack.pop()
print(min_stack.top())      # 0
print(min_stack.get_min())  # -2

# Example:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # -3
min_stack.pop()
print(min_stack.top())      # 0
print(min_stack.get_min())  # -2

# 3. Evaluate Reverse Polish Notation
# Problem:
# Evaluate arithmetic expressions given in Reverse Polish Notation (RPN).

def eval_rpn(tokens: List[str]) -> int:
    """
    Evaluate expression in Reverse Polish Notation.

    Args:
    tokens (List[str]): Tokens in RPN.

    Returns:
    int: Result of expression.
    """
    stack = []
    ops = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token not in ops:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # truncate towards zero
    return stack[0]

# Example:
print(eval_rpn(["2", "1", "+", "3", "*"]))    # 9
print(eval_rpn(["4", "13", "5", "/", "+"]))   # 6

# 3. Merge Two Sorted Linked Lists
# Problem:
# Merge two sorted linked lists and return it as a new sorted list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists.

    Args:
    l1 (ListNode): Head of first sorted list.
    l2 (ListNode): Head of second sorted list.

    Returns:
    ListNode: Head of merged sorted list.
    """
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next

def print_list(head: ListNode):
    """
    Prints linked list in format: val1 -> val2 -> ... -> None
    """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged = merge_two_lists(l1, l2)

print_list(merged)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None



# 1. Design a Scalable URL Shortener
# Problem:
# Design a URL shortener service like Bit.ly that converts long URLs into short ones, ensuring scalability and high availability.

import hashlib
from typing import Optional

# Linked list node class
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

# Function to merge two sorted linked lists
def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists and return the merged sorted list.
    """
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    
    return dummy.next

# Function to print linked list values
def print_list(head: Optional[ListNode]) -> None:
    """
    Print the linked list nodes in order.
    """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# URL Shortener class
class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "http://short.ly/"

    def shorten(self, long_url: str) -> str:
        """
        Shortens a given long URL.
        """
        short_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
        short_url = self.base_url + short_hash
        self.url_mapping[short_url] = long_url
        return short_url

    def resolve(self, short_url: str) -> str:
        """
        Resolves a shortened URL to the original long URL.
        """
        return self.url_mapping.get(short_url, "URL not found")

# ====== Test the linked list merge ======
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

merged = merge_two_lists(l1, l2)
print_list(merged)  # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# ====== Test the URL shortener ======
url_shortener = URLShortener()
short_url = url_shortener.shorten("https://www.example.com")
print("Shortened URL:", short_url)
print("Original URL:", url_shortener.resolve(short_url))




# 2. Implement an LRU Cache
# Problem:
# Design and implement a Least Recently Used (LRU) cache that supports get and put operations with O(1) time complexity.

# Solution

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initializes the LRUCache with a given capacity.

        Args:
        capacity (int): The maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with the key if it exists in the cache.

        Args:
        key (int): The key to retrieve.

        Returns:
        int: The value associated with the key, or -1 if not found.
        """
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the value associated with the key in the cache.

        Args:
        key (int): The key to insert/update.
        value (int): The value to associate with the key.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)      # Evicts key 2
print(cache.get(2))  # Output: -1 (not found)


# 3. Reverse a Linked List
# Problem:
# Reverse a singly linked list.

# Solution:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverses a singly linked list.

    Args:
    head (ListNode): The head node of the linked list.

    Returns:
    ListNode: The new head node of the reversed linked list.
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Creating a linked list: 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_linked_list(head)
# Output: 3 -> 2 -> 1 -> None

# 4. Detect Cycle in a Linked List
# Problem:
# Determine if a singly linked list has a cycle.

# Solution:

def has_cycle(head: ListNode) -> bool:
    """
    Detects if a singly linked list has a cycle.

    Args:
    head (ListNode): The head node of the linked list.

    Returns:
    bool: True if the list has a cycle, False otherwise.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Creating a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head.next.next.next.next = head.next  # Creating a cycle
print(has_cycle(head))  # Output: True

# 5. Merge Two Sorted Linked Lists
# Problem:
# Merge two sorted singly linked lists into a single sorted list.

# Solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merges two sorted singly linked lists into one sorted linked list.

    Args:
    l1 (ListNode): Head of the first sorted linked list.
    l2 (ListNode): Head of the second sorted linked list.

    Returns:
    ListNode: Head of the merged sorted linked list.
    """
    dummy = ListNode()  # Dummy head to simplify edge cases
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining nodes (only one of these will be non-empty)
    current.next = l1 if l1 else l2

    return dummy.next

 
def print_list(head: ListNode) -> None:
    """
    Prints the values in a linked list.

    Args:
    head (ListNode): Head of the linked list.
    """
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# List 1: 1 -> 3 -> 5
l1 = ListNode(1, ListNode(3, ListNode(5)))

# List 2: 2 -> 4 -> 6
l2 = ListNode(2, ListNode(4, ListNode(6)))

# Merge them
merged_head = merge_sorted_lists(l1, l2)

# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
print_list(merged_head)


#  1. Design an LRU Cache
# 📚 Data Structures: HashMap + Doubly Linked List

# Problem:
# Design a data structure that supports get(key) and put(key, value) in O(1) time.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with a given capacity.
        """
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from the linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        """Add node right after head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Return the value of the key if exists, else -1.
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Update or insert the value. Remove LRU item if capacity is exceeded.
        """
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))   # Output: 1
lru.put(3, 3)       # Evicts key 2
print(lru.get(2))   # Output: -1

#  2. Merge K Sorted Linked Lists
# 📚 Data Structures: Min-Heap (Priority Queue)

# Problem:
# Merge k sorted linked lists into a single sorted linked list.

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

def merge_k_lists(lists: list) -> ListNode:
    """
    Merges k sorted linked lists into one sorted list.

    Args:
    lists (List[ListNode]): List of k ListNode heads.

    Returns:
    ListNode: Head of merged linked list.
    """
    min_heap = []
    
    for node in lists:
        if node:
            heapq.heappush(min_heap, node)

    dummy = ListNode()
    current = dummy

    while min_heap:
        smallest = heapq.heappop(min_heap)
        current.next = smallest
        current = current.next
        if smallest.next:
            heapq.heappush(min_heap, smallest.next)

    return dummy.next

# List 1: 1 -> 4 -> 5
# List 2: 1 -> 3 -> 4
# List 3: 2 -> 6

l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))
merged = merge_k_lists([l1, l2, l3])

# Print merged list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print_list(merged)

# 3. Serialize and Deserialize a Binary Tree
# 📚 Data Structures: Binary Tree + Queue

# Problem:
# Design methods to serialize a binary tree into a string and deserialize it back to the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: TreeNode) -> str:
    """
    Encodes a tree to a single string.

    Args:
    root (TreeNode): Root of the tree.

    Returns:
    str: Serialized string.
    """
    if not root:
        return "null,"
    return str(root.val) + "," + serialize(root.left) + serialize(root.right)

def deserialize(data: str) -> TreeNode:
    """
    Decodes your encoded data to tree.

    Args:
    data (str): Serialized tree string.

    Returns:
    TreeNode: Root of the tree.
    """
    def helper(nodes):
        val = nodes.pop(0)
        if val == "null":
            return None
        root = TreeNode(int(val))
        root.left = helper(nodes)
        root.right = helper(nodes)
        return root

    nodes = data.split(",")[:-1]  # Remove last empty item
    return helper(nodes)

tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

data = serialize(tree)
print(data)  # Example: "1,2,null,null,3,4,null,null,5,null,null,"

restored = deserialize(data)
print(serialize(restored))  # Should match the original serialized string





# 3. Design Tic-Tac-Toe
# Problem: Design a Tic-Tac-Toe game that supports an n x n board and determines the winner after each move.
# Medium

# Python Implementation:

class TicTacToe:
    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self.check_winner(row, col, player):
            return player
        return 0

    def check_winner(self, row: int, col: int, player: int) -> bool:
        # Check row
        if all(self.board[row][i] == player for i in range(self.n)):
            return True
        # Check column
        if all(self.board[i][col] == player for i in range(self.n)):
            return True
        # Check diagonal
        if row == col and all(self.board[i][i] == player for i in range(self.n)):
            return True
        # Check anti-diagonal
        if row + col == self.n - 1 and all(self.board[i][self.n - 1 - i] == player for i in range(self.n)):
            return True
        return False

game = TicTacToe(3)
print(game.move(0, 0, 1))  # Output: 0 (no winner)
print(game.move(0, 2, 2))  # Output: 0 (no winner)
print(game.move(2, 2, 1))  # Output: 0 (no winner)
print(game.move(1, 1, 2))  # Output: 0 (no winner)
print(game.move(2, 0, 1))  # Output: 0 (no winner)
print(game.move(1, 0, 2))  # Output: 0 (no winner)
print(game.move(2, 1, 1))  # Output: 1 (player 1 wins)

# 4. Design Snake Game
# Problem: Design a Snake game that is played on a device with screen size height x width. 
# The snake moves in a grid and grows in length when it eats food. The game ends if the snake runs into itself
# or the wall.

from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: list):
        self.width = width
        self.height = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])
        self.snake_set = {(0, 0)}
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.score = 0

    def move(self, direction: str) -> int:
        head = self.snake[0]
        new_head = (head[0] + self.directions[direction][0], head[1] + self.directions[direction][1])

        # Check if snake hits the wall or itself
        if (new_head[0] < 0 or new_head[0] >= self.height or
            new_head[1] < 0 or new_head[1] >= self.width or
            new_head in self.snake_set):
            return -1

        # Check if snake eats food
        if self.food and new_head == self.food[0]:
            self.snake.appendleft(new_head)
            self.snake_set.add(new_head)
            self.food.popleft()
            self.score += 1
        else:
            tail = self.snake.pop()
            self.snake_set.remove(tail)
            self.snake.appendleft(new_head)
            self.snake_set.add(new_head)

        return self.score

game = SnakeGame(3, 3, [(0, 1), (1, 2)])
print(game.move('R'))  # Output: 0
print(game.move('D'))  # Output: 0

 

