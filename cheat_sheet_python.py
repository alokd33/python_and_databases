# while loop
s = 0
i = 1
while i <= 10:
    print(i)
    s = s + i
    i = i + 1
    if i == 5 :
        break
print("sum", s)

x =4
y = 3
print("v =",3,"\n""cm :",x,"\n",y+4 ,"\n")

# import sys
# from io import StringIO
#
# # Simulate user input
# sys.stdin = StringIO("Hello World")  # Replace "Hello World" with the autofill value
#
# s = input("what is you value:")
# print("my value is:", s)
# sys.stdin = sys.__stdin__

a = [1,2,4,3,5,6]
print(len(a))
print(min(a))
print(max(a))
print(sum(a))
print(sorted(a))

for val in a:
    if val == 5 :
        print("val", val, "is in array a" )

for i, v in enumerate(a):
    print("index:",i, "value:", v )

b = ["a","c","b","d","e","f"]

for i, v in zip(a,b):
    print("zip a b :", i,v)

for i, v in zip(b,a):
    print("zip a b :", str(i)+str(v))

c = ["a","c","b","d","e","f", 1, 2]

# All numbers are positive
numbers = [1, 2, 3, 4]
print(all(x > 0 for x in numbers))  # Output: True

# Contains a negative number
numbers = [1, -2, 3, 4]
print(all(x > 0 for x in numbers))  # Output: False

# All values are True
print(all([True, True, True]))  # Output: True

# Contains a False value
print(all([True, False, True]))  # Output: False

# Empty iterable
print(all([]))  # Output: True (vacuously True)


# At least one value is True
print(any([False, True, False]))  # Output: True

# All values are False
print(any([False, False, False]))  # Output: False

# Empty iterable
print(any([]))  # Output: False

# At least one positive number
numbers = [-1, -2, 0, 3]
print(any(x > 0 for x in numbers))  # Output: True

# All numbers are negative or zero
numbers = [-1, -2, 0]
print(any(x > 0 for x in numbers))  # Output: False

a = [1,2,4,3,5,6]
b1 = reversed(a)
print(list(b1))


# Original string
text = "Hello"

# Using reversed()
reversed_text = ''.join(reversed(text))
print(reversed_text)  # Output: "olleH"

a1 = [1,2,4,3,5,6]
a2 = [1,2,4,3,5,6]

print(a1*5) # [1, 2, 4, 3, 5, 6, 1, 2, 4, 3, 5, 6, 1, 2, 4, 3, 5, 6, 1, 2, 4, 3, 5, 6, 1, 2, 4, 3, 5, 6]

print(a1+a2) # concatenate [1, 2, 4, 3, 5, 6, 1, 2, 4, 3, 5, 6]

print(a1.index(6)) # 5

a3 = [1,2,3,1,2,4,4,4]
print(a3.count(4)) # 3

import copy

# Shallow copy of the container
# Deep copy of container



import copy

# In Python, shallow copy and deep copy refer to the copying of container objects
# (e.g., lists, dictionaries) and how their contents are copied.
#
# 1. Shallow Copy
# A shallow copy creates a new container object but only copies references to the objects contained within it.
# If the contained objects are mutable, changes to them in one container affect the other.

# Original container
original_list = [[1, 2, 3], [4, 5, 6]]

# Shallow copy of the container
shallow_copied_list = copy.copy(original_list)

# Modify an inner list
shallow_copied_list[0][0] = 99

# Observe changes
print("Original List:", original_list)      # Output: [[99, 2, 3], [4, 5, 6]]
print("Shallow Copied List:", shallow_copied_list)  # Output: [[99, 2, 3], [4, 5, 6]]

# Modify the outer list
shallow_copied_list.append([7, 8, 9])

print("Original List:", original_list)      # Output: [[99, 2, 3], [4, 5, 6]]
print("Shallow Copied List:", shallow_copied_list)  # Output: [[99, 2, 3], [4, 5, 6], [7, 8, 9]]

# Explanation:
# The shallow copy creates a new container (shallow_copied_list), but the inner lists are references to the same objects in original_list.
# Changing the inner list affects both containers, but appending to the outer container affects only the copied list.

# 2. Deep Copy
# A deep copy creates a new container and recursively copies all the objects inside it.
# Changes to the inner objects do not affect the original container.
#
# Example: Deep Copy

import copy

# Original container
original_list = [[1, 2, 3], [4, 5, 6]]

# Deep copy of the container
deep_copied_list = copy.deepcopy(original_list)

# Modify an inner list
deep_copied_list[0][0] = 99

# Observe changes
print("Original List:", original_list)      # Output: [[1, 2, 3], [4, 5, 6]]
print("Deep Copied List:", deep_copied_list)  # Output: [[99, 2, 3], [4, 5, 6]]

# Modify the outer list
deep_copied_list.append([7, 8, 9])

print("Original List:", original_list)      # Output: [[1, 2, 3], [4, 5, 6]]
print("Deep Copied List:", deep_copied_list)  # Output: [[99, 2, 3], [4, 5, 6], [7, 8, 9]]

# Explanation:
# A deep copy creates entirely new objects for the container and its contents.
# Modifying the inner list or the outer list in deep_copied_list has no effect on original_list



# In Python, shallow copy and deep copy refer to the copying of container objects (e.g., lists, dictionaries) and how their contents are copied.
#
# 1. Shallow Copy
# A shallow copy creates a new container object but only copies references to the objects contained within it. If the contained objects are mutable, changes to them in one container affect the other.
#
# Example: Shallow Copy
# python
# Copy code
import copy

# Original container
original_list = [[1, 2, 3], [4, 5, 6]]

# Shallow copy of the container
shallow_copied_list = copy.copy(original_list)

# Modify an inner list
shallow_copied_list[0][0] = 99

# Observe changes
print("Original List:", original_list)      # Output: [[99, 2, 3], [4, 5, 6]]
print("Shallow Copied List:", shallow_copied_list)  # Output: [[99, 2, 3], [4, 5, 6]]

# Modify the outer list
shallow_copied_list.append([7, 8, 9])

print("Original List:", original_list)      # Output: [[99, 2, 3], [4, 5, 6]]
print("Shallow Copied List:", shallow_copied_list)  # Output: [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
# Explanation:
# The shallow copy creates a new container (shallow_copied_list), but the inner lists are references to the same objects in original_list.
# Changing the inner list affects both containers, but appending to the outer container affects only the copied list.
# 2. Deep Copy
# A deep copy creates a new container and recursively copies all the objects inside it. Changes to the inner objects do not affect the original container.
#
# Example: Deep Copy
# python
# Copy code
import copy

# Original container
original_list = [[1, 2, 3], [4, 5, 6]]

# Deep copy of the container
deep_copied_list = copy.deepcopy(original_list)

# Modify an inner list
deep_copied_list[0][0] = 99

# Observe changes
print("Original List:", original_list)      # Output: [[1, 2, 3], [4, 5, 6]]
print("Deep Copied List:", deep_copied_list)  # Output: [[99, 2, 3], [4, 5, 6]]

# Modify the outer list
deep_copied_list.append([7, 8, 9])

print("Original List:", original_list)      # Output: [[1, 2, 3], [4, 5, 6]]
print("Deep Copied List:", deep_copied_list)  # Output: [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
# Explanation:
# A deep copy creates entirely new objects for the container and its contents.
# Modifying the inner list or the outer list in deep_copied_list has no effect on original_list.
# Key Differences
# Aspect	Shallow Copy	Deep Copy
# What is copied?	Outer container; inner objects are references	Outer container and inner objects
# Independent?	Changes to inner objects affect the original	Fully independent
# Performance	Faster (less memory use)	Slower (more memory use)

# 3. When to Use Which?
# Use shallow copy when the objects in the container are immutable (e.g., numbers, strings).
# Use deep copy when you need to modify the inner objects without affecting the original container.


# Operations on list :
a4 = [1,3,2,4]
a4.append(5)
print(a4) # add item at the end [1, 3, 2, 4, 5]

a4 = [1,3,2,4]
a5 = [5,6]
a4.extend(a5)
print(a4) # [1, 3, 2, 4, 5, 6] Add seq of the items at the end

a4 = [1,3,2,4]
a4.insert(1,5) # insert item at index(idx, val)
print(a4) # [1, 5, 3, 2, 4]

a4 = [1,3,2,4,3]
a4.remove(3) # remove first item of value val
print(a4) # [1, 2, 4, 3]

a4 = [1,3,2,4]
print(a4.pop(0)) # value, remove & return item at index idx ( default last) # 1
print(a4) # [3, 2, 4]

a4 = [1,3,2,4]
print(a4.pop()) # value, remove & return item at index idx ( default last) # 4
print(a4) # [1, 3, 2]

a4 = [1,3,2,4]
print(a4.sort()) # None
print(a4) # [1, 2, 3, 4]

a4 = ["ab","aa","cd","bb"]
print(a4.sort()) # None
print(a4) # ['aa', 'ab', 'bb', 'cd']

a4 = [1,3,2,4]
print(a4.reverse()) # None
print(a4) # [4, 2, 3, 1]


# Python list comprehensions provide a concise way to create lists.
# They are faster and require less code compared to using traditional for loops for the same purpose.

#[expression for item in iterable if condition]
# expression: The value to be added to the list.
# item: Current element from the iterable.
# iterable: A sequence or collection (e.g., list, range, string).
# condition: (Optional) Filters elements of the iterable.


# 1. Simple List Comprehension
# Create a list of squares of numbers from 1 to 5:

squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# 2. With a Condition
# Create a list of even numbers from 1 to 10:


evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]


# 3. Nested Loops
# Generate a list of coordinate pairs (x, y) where x and y are from 1 to 3:


coordinates = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(coordinates)
# Output: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


# 4. Conditional Expressions in Expression
# Replace negative numbers with 0:


nums = [-1, 2, -3, 4]
non_negative = [x if x > 0 else 0 for x in nums]
print(non_negative)  # Output: [0, 2, 0, 4]

# 5. String Manipulation
# Extract the uppercase letters from a string:

text = "Hello World!"
uppercase = [char for char in text if char.isupper()]
print(uppercase)  # Output: ['H', 'W']


# 6. Flatten a Nested List
# Flatten a 2D list into a 1D list:

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]


# 7. Using Functions
# Apply a function to all elements in a list:

def square(x):
    return x ** 2

nums = [1, 2, 3, 4]
squared = [square(x) for x in nums]
print(squared)  # Output: [1, 4, 9, 16]


# 8. List of Dictionaries
# Extract specific values from a list of dictionaries:

students = [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 90}]
names = [student["name"] for student in students]
print(names)  # Output: ['Alice', 'Bob']
score = [student["score"] for student in students]
print(score)  # Output: ['85', '90']


# 9. Cartesian Product
# Find all combinations of elements from two lists:

list1 = [1, 2]
list2 = ['a', 'b']
cartesian = [(x, y) for x in list1 for y in list2]
print(cartesian)  # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]


# 10. Remove Duplicates
# Create a list of unique elements from another list:

nums = [1, 2, 2, 3, 3, 4]
unique_nums = list({x for x in nums})
print(unique_nums)  # Output: [1, 2, 3, 4]


# 11. Nested List Comprehension
# Create a multiplication table:

table = [[x * y for y in range(1, 6)] for x in range(1, 6)]
print(table)
# Output:
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]

# 12. Handling Strings
# Create a list of words from a sentence:

sentence = "This is a list comprehension example"
words = [word for word in sentence.split()]
print(words)  # Output: ['This', 'is', 'a', 'list', 'comprehension', 'example']

# 13. Filtering with Multiple Conditions
# Create a list of numbers divisible by both 2 and 3:

nums = [x for x in range(1, 20) if x % 2 == 0 and x % 3 == 0]
print(nums)  # Output: [6, 12, 18]

# Operation on dictionaies

# 1. Accessing Dictionary Elements
# Accessing Values

d = {"name": "Alice", "age": 25, "city": "New York"}
print(d["name"])       # Output: Alice

# Using `get()` (avoids KeyError if key is missing)
print(d.get("age"))    # Output: 25
print(d.get("gender")) # Output: None
print(d.get("gender", "Not Found"))  # Output: Not Found


# 2. Adding and Updating Values

# Adding a new key-value pair
d["gender"] = "Female"
print(d)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'gender': 'Female'}

# Updating an existing value
d["age"] = 26
print(d)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'gender': 'Female'}

# Using update() to merge/update
d.update({"age": 30, "country": "USA"})
print(d)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'gender': 'Female', 'country': 'USA'}

# 3. Removing Elements
#Using pop()
# Remove key and return value
age = d.pop("age")
print(age)  # Output: 30
print(d)    # Output: {'name': 'Alice', 'city': 'New York', 'gender': 'Female', 'country': 'USA'}

# Using popitem() (LIFO order) Last in First out
last_item = d.popitem()
print(last_item)  # Output: ('country', 'USA')
print(d)          # Output: {'name': 'Alice', 'city': 'New York', 'gender': 'Female'}

# Using del

# Remove a key-value pair
del d["city"]
print(d)  # Output: {'name': 'Alice', 'gender': 'Female'}

# Delete the entire dictionary
del d
#print(d)  # Raises NameError as d no longer exists

# Using clear()
d = {"name": "Alice", "age": 25}
d.clear()
print(d)  # Output: {}

# 4. Dictionary Views
# Accessing Keys, Values, and Items

d = {"name": "Alice", "age": 25, "city": "New York"}

# Keys
print(d.keys())  # Output: dict_keys(['name', 'age', 'city'])

# Values
print(d.values())  # Output: dict_values(['Alice', 25, 'New York'])

# Items (key-value pairs)
print(d.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# Iterating Over Keys, Values, and Items

# Iterate over keys
for key in d.keys():
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

#5. Checking for Existence of Keys

print("name" in d)        # Output: True
print("gender" not in d)  # Output: True

# 6. Default Values
# Using setdefault()

# Adds the key if it does not exist
d.setdefault("gender", "Female")
print(d)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'gender': 'Female'}

# Does not overwrite existing key
d.setdefault("age", 30)
print(d)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'gender': 'Female'}

# Using fromkeys()

keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(default_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}


# 7. Dictionary Copying
# Shallow Copy

d = {"name": "Alice", "age": 25}
shallow_copy = d.copy()
print(shallow_copy)  # Output: {'name': 'Alice', 'age': 25}

# Deep Copy
import copy

d = {"name": "Alice", "nested": {"age": 25}}
deep_copy = copy.deepcopy(d)
deep_copy["nested"]["age"] = 30
print(d)         # Output: {'name': 'Alice', 'nested': {'age': 25}}
print(deep_copy) # Output: {'name': 'Alice', 'nested': {'age': 30}}

# 8. Dictionary Comprehensions
# Create a Dictionary from a List

nums = [1, 2, 3, 4]
squared = {x: x**2 for x in nums}
print(squared)  # Output: {1: 1, 2: 4, 3: 9, 4: 16}

#Conditional Comprehension

# Only include even numbers
evens = {x: x**2 for x in nums if x % 2 == 0}
print(evens)  # Output: {2: 4, 4: 16}

#Nested Dictionary Comprehension

nested_dict = {x: {y: y**2 for y in range(1, 4)} for x in range(1, 3)}
print(nested_dict)
# Output: {1: {1: 1, 2: 4, 3: 9}, 2: {1: 1, 2: 4, 3: 9}}

#9. Sorting a Dictionary
# Sort by Keys
unsorted_dict = {"b": 2, "a": 1, "c": 3}
sorted_dict = dict(sorted(unsorted_dict.items()))
print(sorted_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Sort by Values
unsorted_dict = {"b": 20, "a": 1, "c": 3}
sorted_by_values = dict(sorted(unsorted_dict.items(), key=lambda x: x[1]))
print(sorted_by_values)  # Output: {'a': 1, 'c': 3, 'b': 20}

# 10. Dictionary as a Stack or Queue
# Stack Using popitem() Last in first out

stack = {}
stack["a"] = 1
stack["b"] = 2
print(stack) # {'a': 1, 'b': 2}
print(stack.popitem())  # Output: ('b', 2)
print(stack) # {'a': 1}

# Queue Using pop() # First in first out

queue = {"a": 1, "b": 2}
print(queue.pop("a"))  # Output: 1
print(queue)           # Output: {'b': 2}

# 11. Merging Dictionaries
# Using update()
d1 = {"name": "Alice"}
d2 = {"age": 25}
d1.update(d2)
print(d1)  # Output: {'name': 'Alice', 'age': 25'}

#Using Dictionary Unpacking (Python 3.9+)

merged = {**d1, **d2}
print(merged)  # Output: {'name': 'Alice', 'age': 25}

# Python sets are unordered, mutable collections of unique elements.
# Here’s a comprehensive guide to all operations on sets with examples, including standard operations and advanced use cases.

# 1. Creating Sets

# Creating a set
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}

# Creating an empty set (use set(), not {})
empty_set = set()
print(empty_set)  # Output: set()

# Set from a list (removes duplicates)
my_set = set([1, 2, 2, 3])
print(my_set)  # Output: {1, 2, 3}


# 2. Adding Elements

# Adding a single element
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Adding multiple elements using update()
my_set.update([5, 6, 7])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

# 3. Removing Elements

# Using remove() (raises KeyError if element is not found)
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6, 7}

# Using discard() (does not raise an error if element is not found)
my_set.discard(10)

# Using pop() (removes and returns a random element)
removed_element = my_set.pop()
print(removed_element)  # Example Output: 1
print(my_set)  # Example Output: {2, 4, 5, 6, 7}

# Clearing all elements
my_set.clear()
print(my_set)  # Output: set()

# 4. Accessing Elements

# Sets are unordered, so you cannot access elements by index.
# Instead, iterate through the set.
# Creating a set
my_set = {1, 2, 3}
for element in my_set:
    print(element)

# 5. Set Operations
# Union (| or union())
# Combine all elements from both sets:

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)            # Output: {1, 2, 3, 4, 5}
print(a.union(b))       # Output: {1, 2, 3, 4, 5}

# Intersection (& or intersection())
# Find common elements:

print(a & b)            # Output: {3}
print(a.intersection(b))  # Output: {3}

# Difference (- or difference())
# Find elements in the first set but not in the second:


print(a - b)            # Output: {1, 2}
print(a.difference(b))  # Output: {1, 2}

# Symmetric Difference (^ or symmetric_difference())
# Find elements in either set, but not in both:

print(a ^ b)  # Output: {1, 2, 4, 5}
print(a.symmetric_difference(b))  # Output: {1, 2, 4, 5}

# 6. Checking Subset and Superset
# Subset (issubset())

a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # Output: True
print(b.issubset(a))  # Output: False

# Superset (issuperset())

print(b.issuperset(a))  # Output: True
print(a.issuperset(b))  # Output: False

# Disjoint Sets (isdisjoint())
# Check if two sets have no elements in common:

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # Output: True

# 7. Set Comparisons

a = {1, 2, 3}
b = {1, 2}

print(a == b)  # Output: False (sets are not equal)
print(a != b)  # Output: True (sets are not equal)

# 8. Set Comprehensions
# Creating a set of squares
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}

# Conditional comprehension
even_squares = {x**2 for x in range(1, 6) if x % 2 == 0}
print(even_squares)  # Output: {4, 16}


# 9. Frozen Sets (Immutable Sets)
# A frozenset is an immutable version of a set.

a = frozenset([1, 2, 3])
print(a)  # Output: frozenset({1, 2, 3})

# Immutable, so operations like add() or remove() are not allowed
# a.add(4)  # Raises AttributeError

# Set operations still work
b = {3, 4, 5}
print(a | b)  # Output: {1, 2, 3, 4, 5}


# 10. Iterating Over Sets

my_set = {1, 2, 3, 4}
for element in my_set:
    print(element)

original = {1, 2, 3}
# Shallow copy
copy_set = original.copy()
print(copy_set)  # Output: {1, 2, 3}


# 12. Length of a Set
print(len(my_set))  # Output: 4

# 13. Converting Between Data Types

# Convert list to set
my_list = [1, 2, 2, 3]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3}

# Convert set to list
my_list_again = list(my_set)
print(my_list_again)  # Output: [1, 2, 3]

# 14. Checking Membership

my_set = {1, 2, 3}
print(2 in my_set)      # Output: True
print(5 not in my_set)  # Output: True

# 15. Removing Duplicates from a List

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
unique_list = list(unique_set)
print(unique_list)  # Output: [1, 2, 3, 4, 5]

# Common Mistakes
# Using {} for an empty set:

my_set = {}  # This creates a dictionary, not a set.
my_set = set()  # Correct way to create an empty set.

# Using mutable elements in a set:
# Sets cannot contain mutable elements like lists
# my_set = {1, [2, 3]}  # Raises TypeError

# 1. Creating Strings

# Single and double quotes
s1 = 'Hello'
s2 = "World"
print(s1, s2)  # Output: Hello World

# Multiline strings
multiline = """This is
a multiline
string."""
print(multiline)

# String with escape characters
escaped = "He said, \"Python is great!\""
print(escaped)  # Output: He said, "Python is great!"

# 2. Accessing Characters

s = "Python"

# Indexing
print(s[0])  # Output: P
print(s[-1]) # Output: n

# Slicing
print(s[1:4])   # Output: yth
print(s[:3])    # Output: Pyt
print(s[3:])    # Output: hon

# 3. String Length

s = "Hello"
print(len(s))  # Output: 5

# 4. Iterating Through Strings

for char in "Python":
    print(char)

# 5. String Concatenation

s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print(result)  # Output: Hello World

# 6. String Repetition

print("Python " * 3)  # Output: Python Python Python

# 7. String Membership
s = "Python"
print("P" in s)   # Output: True
print("z" not in s)  # Output: True

# 8. Modifying Strings
# Changing Case
s = "Python Programming"
print(s.lower())   # Output: python programming
print(s.upper())   # Output: PYTHON PROGRAMMING
print(s.title())   # Output: Python Programming
print(s.capitalize())  # Output: Python programming
print(s.swapcase())    # Output: pYTHON pROGRAMMING

# Stripping Whitespace

s = "   Python   "
print(s.strip())   # Output: Python
print(s.lstrip())  # Output: Python
print(s.rstrip())  # Output:    Python

#Replacing Substrings

s = "Python is fun"
print(s.replace("fun", "awesome"))  # Output: Python is awesome

# Splitting and Joining
s = "Python is fun"
words = s.split()  # Splits on spaces
print(words)  # Output: ['Python', 'is', 'fun']

# s = "Python is fun"
# words = s.split(" is ")  # Splits on is
# print(words)  # Output: ['Python', 'fun']

joined = "-".join(words)
print(joined)  # Output: Python-is-fun

# 9. String Searching
# Finding Substrings

s = "Python programming"
print(s.find("prog"))  # Output: 7
print(s.rfind("t"))    # Output: 2 (last occurrence)
print(s.index("prog")) # Output: 7
# print(s.index("z"))  # Raises ValueError

#Checking Start/End

s = "Python programming"
print(s.startswith("Python"))  # Output: True
print(s.endswith("ing"))       # Output: True

# 10. Formatting Strings
# Using format()

name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 25 years old.

# Using f-strings (Python 3.6+)

print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.

# 11. String Validation
# Checking Content

s = "Python3"

print(s.isalnum())   # True: Contains only letters and numbers
print(s.isalpha())   # False: Contains numbers too
print(s.isdigit())   # False: Contains letters
print(s.islower())   # False: Has uppercase letters
print(s.isupper())   # False: Has lowercase letters
print(" ".isspace()) # True: Contains only whitespace


# 12. String Encoding

s = "Hello"
encoded = s.encode("utf-8")
print(encoded)  # Output: b'Hello'

decoded = encoded.decode("utf-8")
print(decoded)  # Output: Hello

# 13. String Comparison

s1 = "Apple"
s2 = "Banana"
print(s1 == s2)   # Output: False
print(s1 < s2)    # Output: True (Alphabetical comparison)
print(s1 > s2)    # Output: False


# 14. Advanced String Operations

# Counting Substrings

s = "Python programming"
print(s.count("o"))  # Output: 2

# Reversing a String

s = "Python"
reversed_s = s[::-1]
print(reversed_s)  # Output: no


# Padding Strings

s = "Python"
print(s.center(10, "-"))  # Output: --Python--
print(s.ljust(10, "-"))   # Output: Python----
print(s.rjust(10, "-"))   # Output: ----Python
# Translating Strings


s = "abc"
translation_table = str.maketrans("abc", "xyz")
print(s.translate(translation_table))  # Output: xyz


# 15. Multi-line Strings

s = """This is
a multi-line
string."""
print(s)


# 16. Splitting Lines

s = "Line1\nLine2\nLine3"
lines = s.splitlines()
print(lines)  # Output: ['Line1', 'Line2', 'Line3']


# 17. Immutability of Strings
s = "Python"
s = s.replace("P", "J")
print(s)  # Output: Jython


# 18. String Comprehensions

# Create a list of uppercase letters
s = "python"
uppercase = [char.upper() for char in s]
print(uppercase)  # Output: ['P', 'Y', 'T', 'H', 'O', 'N']


# 19. String Membership

s = "Python programming"
print("Python" in s)       # Output: True
print("Java" not in s)     # Output: True


# 20. Converting Data Types
# Convert String to List

s = "Python"
char_list = list(s)
print(char_list)  # Output: ['P', 'y', 't', 'h', 'o', 'n']

# Convert List to String

char_list = ['P', 'y', 't', 'h', 'o', 'n']
s = ''.join(char_list)
print(s)  # Output: Python


# 21. String Copy

s1 = "Hello"
s2 = s1  # Strings are immutable, so this is a safe copy
print(s2)  # Output: Hello


# Summary of Common String Methods:
# Method	Description
# s.lower()	Converts string to lowercase
# s.upper()	Converts string to uppercase
# s.title()	Converts first letter of each word to uppercase
# s.strip()	Removes leading/trailing whitespace
# s.replace(old, new)	Replaces substring with another
# s.split()	Splits string into a list
# s.join(iterable)	Joins elements of an iterable with string
# s.find(sub)	Finds the first occurrence of substring
# s.count(sub)	Counts occurrences of substring
# s.startswith(prefix)	Checks if string starts with prefix
# s.endswith(suffix)	Checks if string ends with suffix

# To remove all special characters from a string, leaving only
# alphanumeric characters (letters and digits), you can use the following methods:


# 1. Using Regular Expressions (re.sub)
import re

# Example string
s = "Hello123! @Python#World."

# Remove all special characters (keep only letters and digits)
result = re.sub(r'[^a-zA-Z0-9]', '', s)
print(result)  # Output: "Hello123PythonWorld"

# 2. Using String Comprehension
# Example string
s = "Hello123! @Python#World."

# Remove special characters
result = ''.join([char for char in s if char.isalnum()])
print(result)  # Output: "Hello123PythonWorld"


# 3. Using filter()

# Example string
s = "Hello123! @Python#World."

# Remove special characters
result = ''.join(filter(str.isalnum, s))
print(result)  # Output: "Hello123PythonWorld"

# 4. Using str.translate()

import string

# Example string
s = "Hello123! @Python#World."

# Create a translation table for special characters
special_chars = string.punctuation + string.whitespace
translation_table = str.maketrans('', '', special_chars)

# Remove special characters
result = s.translate(translation_table)
print(result)  # Output: "Hello123PythonWorld

# Explanation of Methods:
# re.sub: Matches any character that is not (^) alphanumeric (a-zA-Z0-9) and replaces it with an empty string.
# Comprehension: Iterates through each character and keeps it only if it is alphanumeric using char.isalnum().
# filter(): Filters the string to include only alphanumeric characters by applying str.isalnum.
# str.translate(): Removes specific characters using a translation table, which
# is particularly efficient for large strings.

# Here's a comprehensive guide to Python looping over different data types (list, dict, set, and string) ' \
# 'with various approaches, covering len(), range(), enumerate(), key-value pairs, and more:

# 1. Loops for List
# 1.1. Loop through elements

my_list = [10, 20, 30, 40]

for item in my_list:
    print(item)  # Output: 10, 20, 30, 40


# 1.2. Loop with len() and range()

for i in range(len(my_list)):
    print(f"Index: {i}, Value: {my_list[i]}")
# Output:
# Index: 0, Value: 10
# Index: 1, Value: 20
# Index: 2, Value: 30
# Index: 3, Value: 40

# 1.3. Loop with enumerate() (Index and Value)
my_list = [10, 20, 30, 40]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: 10
# Index: 1, Value: 20
# Index: 2, Value: 30
# Index: 3, Value: 40

# 1.4. Using range() with step

# range([start,] end [,step])
# start default 0, end not included in sequence, step signed, default 1
# range(5) # 0,1,2,3,4
# range(3,8) # 3,4,5,6,7
# range(2,12,3) # 2,5,8,11
# range(20,5,-5) # 20,15,10
# range(len(seq)) # seq of index of value in seq

my_list = [10, 20, 30, 40]
for i in range(0, len(my_list), 2):
    print(my_list[i])  # Output: 10, 30



# 2. Loops for Dict
# 2.1. Loop through keys

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

for key in my_dict:
    print(key)
# Output:
# name
# age
# city

# 2.2. Loop through values
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for value in my_dict.values():
    print(value)
# Output:
# Alice
# 25
# New York

# 2.3. Loop through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: New York

# 2.4. Loop through keys using len() and list()

keys = list(my_dict.keys())
for i in range(len(keys)):
    print(f"Key: {keys[i]}, Value: {my_dict[keys[i]]}")
# Output:
# Key: name, Value: Alice
# Key: age, Value: 25
# Key: city, Value: New York

# 3. Loops for Set
# 3.1. Loop through elements

my_set = {10, 20, 30, 40}

for item in my_set:
    print(item)
# Output (order may vary):
# 10
# 20
# 30
# 40

# 3.2. Loop with len() and list()

for i in range(len(my_set)):
    print(list(my_set)[i])
# Output (order may vary):
# 10
# 20
# 30
# 40

# 3.3. Loop with enumerate()

for index, value in enumerate(my_set):
    print(f"Index: {index}, Value: {value}")
# Output (order may vary):
# Index: 0, Value: 10
# Index: 1, Value: 20
# Index: 2, Value: 30
# Index: 3, Value: 40


# 4. Loops for String
# 4.1. Loop through characters

my_string = "Python"

for char in my_string:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n

# 4.2. Loop with len() and range()
my_string = "Python"
for i in range(len(my_string)):
    print(f"Index: {i}, Character: {my_string[i]}")
# Output:
# Index: 0, Character: P
# Index: 1, Character: y
# Index: 2, Character: t
# Index: 3, Character: h
# Index: 4, Character: o
# Index: 5, Character: n

#4.3. Loop with enumerate() (Index and Character)

for index, char in enumerate(my_string):
    print(f"Index: {index}, Character: {char}")
# Output:
# Index: 0, Character: P
# Index: 1, Character: y
# Index: 2, Character: t
# Index: 3, Character: h
# Index: 4, Character: o
# Index: 5, Character: n

# 4.4. Reverse String Loop

for char in reversed(my_string):
    print(char)
# Output:
# n
# o
# h
# t
# y
# P

# Summary of Methods
# Data Type	Method	Description
# List	for item in list	Loop through each element
# enumerate()	Get index and value
# range(len(list))	Use indices to access elements
# Dict	.keys()	Loop through keys
# .values()	Loop through values
# .items()	Loop through key-value pairs
# Set	for item in set	Loop through each element
# enumerate()	Get index and value
# String	for char in string	Loop through each character
# enumerate()	Get index and character
# reversed()	Loop through characters in reverse order

#1. Infinite Loops
#A while loop can run indefinitely until a specific condition is met. This is hard to achieve with a for loop.

# Infinite loop waiting for a specific user input
# while True:
#     user_input = input("Type 'exit' to quit: ")
#     if user_input.lower() == "exit":
#         print("Exiting...")
#         break

# 2. Dynamic Condition
# When the termination condition depends on a state that changes dynamically, a while loop is more suitable.

# Keep halving a number until it becomes less than 1
number = 100
while number >= 1:
    print(number)
    number /= 2
# Output: 100, 50.0, 25.0, 12.5, 6.25, 3.125, 1.5625, 0.78125

# 3. Waiting for an External Event
#When waiting for an external condition (e.g., user action, a server response), a while loop works better.

import random

# Simulate waiting for a random number to be greater than 90
while True:
    num = random.randint(1, 100)
    print(f"Generated number: {num}")
    if num > 90:
        print("Number greater than 90. Stopping.")
        break

#4. Monitoring a Changing State
# while loops can monitor a state variable that might change due to various factors.

# Simulating a countdown timer
timer = 10
while timer > 0:
    print(f"Time remaining: {timer} seconds")
    timer -= 1
# Output: Time remaining: 10, 9, ..., 1 seconds


# 5. Conditional Input Validation
# Repeatedly ask for input until a valid condition is met.
# Example:

# Ask the user for a valid number between 1 and 10
# while True:
#     try:
#         num = int(input("Enter a number between 1 and 10: "))
#         if 1 <= num <= 10:
#             print(f"You entered a valid number: {num}")
#             break
#         else:
#             print("Number not in range. Try again.")
#     except ValueError:
#         print("Invalid input. Please enter a number.")


# 6. Simulating Do-While Behavior
# Python doesn't have a do-while loop, but a while loop can simulate it by executing the body at least once.
#Example:

# Simulate do-while: execute at least once
# while True:
#     num = int(input("Enter a positive number: "))
#     if num > 0:
#         print(f"You entered: {num}")
#         break
#     print("Number is not positive. Try again.")

# 7. Backtracking Problems
# In recursive algorithms or backtracking scenarios, a while loop works better for iterative exploration.
# Example:

# Simulating a backtracking problem
path = [1, 2, 3, 4]
while path:
    step = path.pop()
    print(f"Backtracking step: {step}")
print(path)
# Output: Backtracking step: 4, 3, 2, 1

# 8. Real-Time Data Processing
# Continuously process data from a stream or queue.
# Example:

# Processing items in a queue
queue = [1, 2, 3, 4, 5]
while queue:
    item = queue.pop(0)  # Remove the first item
    print(f"Processing item: {item}")
# Output: Processing item: 1, 2, 3, 4, 5


# 9. Polling or Repeated Checks
# Perform a task repeatedly until a condition becomes true.
# Example:

# Simulate polling a status
status = "loading"
while status != "complete":
    print("Checking status...")
    status = "complete"  # Simulate the status changing
print("Status is complete!")

# 10. Iteration with Complex Conditions
# When the loop condition depends on multiple variables that change during execution.
# Example:

# Exit when either counter reaches a certain point
a, b = 0, 10
while a < 5 and b > 0:
    print(f"a: {a}, b: {b}")
    a += 1
    b -= 2
# Output: a: 0, b: 10; a: 1, b: 8; ..., a: 4, b: 2

# Summary: When to Use while Instead of for
# Scenario	Why while Works Better
# Unknown number of iterations	while loops can run indefinitely based on a condition.
# Dynamic conditions	The termination condition can depend on variables that change during execution.
# Input validation or external events	Suitable for waiting or repeatedly checking for user input or external triggers.
# Simulating do-while loops	Ensures the body executes at least once, regardless of the condition.
# Backtracking or state monitoring	Ideal for tracking dynamic states or exploring paths iteratively.
# Let me know if you'd like more examples or explanations!


# Summary of Data Types
# *args	tuple  int, float, str, list, tuple, dict  (10, 3.14, "hello", [1, 2], (3, 4), {"key": "value"})
# **kwargs dict Key = str, Value = int, float, str, list, tuple, dict  {"a": 10, "b": 3.14, "c": "hello", "d": [1, 2]}

# Use Cases of *args and **kwargs
# 1. Flexible Argument Passing


# **Explanation of *args and **kwargs
# What is *args?
# Purpose: To accept an arbitrary number of positional arguments in a function.
# Data Structure: Stored as a tuple.
# Example:

def example(*args):
    print(args)

example(1, 2, 3, "hello")
# Output: (1, 2, 3, 'hello')

# What is **kwargs?
# Purpose: To accept an arbitrary number of keyword arguments in a function.
# Data Structure: Stored as a dictionary.
# Example:

def example(**kwargs):
    print(kwargs)

example(a=1, b=2, c="hello")
# Output: {'a': 1, 'b': 2, 'c': 'hello'}

def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, a=10, b=20)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'a': 10, 'b': 20}

# Data Types for *args
# Data Type: tuple
# *args captures all positional arguments as a tuple.
# Each element in *args can be of any data type.
# Example Function to Show *args Data Types


def demo_args(*args):
    """
    Demonstrates the data types stored in *args.

    Args:
        *args (tuple): Variable-length positional arguments.

    Prints:
        The type of *args and the type of each element inside *args.
    """
    print(f"*args is of type: {type(args)}")  # Always a tuple
    for i, arg in enumerate(args):
        print(f"args[{i}] is of type: {type(arg)}, value: {arg}")

demo_args(10, 3.14, "hello", [1, 2], (3, 4), {"key": "value"})

# *args is of type: <class 'tuple'>
# args[0] is of type: <class 'int'>, value: 10
# args[1] is of type: <class 'float'>, value: 3.14
# args[2] is of type: <class 'str'>, value: hello
# args[3] is of type: <class 'list'>, value: [1, 2]
# args[4] is of type: <class 'tuple'>, value: (3, 4)
# args[5] is of type: <class 'dict'>, value: {'key': 'value'}

# Data Types for **kwargs
# Data Type: dict
# **kwargs captures all keyword arguments as a dictionary.
# Keys are always str, and values can be of any data type.
# Example Function to Show **kwargs Data Types

def demo_kwargs(**kwargs):
    """
    Demonstrates the data types stored in **kwargs.

    Args:
        **kwargs (dict): Variable-length keyword arguments.

    Prints:
        The type of **kwargs and the type of each value inside **kwargs.
    """
    print(f"**kwargs is of type: {type(kwargs)}")  # Always a dictionary
    for key, value in kwargs.items():
        print(f"kwargs[{key!r}] is of type: {type(value)}, value: {value}")

demo_kwargs(a=10, b=3.14, c="hello", d=[1, 2], e=(3, 4), f={"key": "value"})

# **kwargs is of type: <class 'dict'>
# kwargs['a'] is of type: <class 'int'>, value: 10
# kwargs['b'] is of type: <class 'float'>, value: 3.14
# kwargs['c'] is of type: <class 'str'>, value: hello
# kwargs['d'] is of type: <class 'list'>, value: [1, 2]
# kwargs['e'] is of type: <class 'tuple'>, value: (3, 4)
# kwargs['f'] is of type: <class 'dict'>, value: {'key': 'value'}

def demo_args_kwargs(my_list, my_string, *args, **kwargs):
    """
    Demonstrates the data types stored in *args and **kwargs, along with additional arguments.

    Args:
        my_list (list): A list passed explicitly to the function.
        my_string (str): A string passed explicitly to the function.
        *args (tuple): Variable-length positional arguments.
        **kwargs (dict): Variable-length keyword arguments.

    Prints:
        The type of each argument, including *args and **kwargs, and their contents.
    """
    print(f"my_list is of type: {type(my_list)}, value: {my_list}")
    print(f"my_string is of type: {type(my_string)}, value: {my_string}")

    print(f"\n*args is of type: {type(args)}")
    for i, arg in enumerate(args):
        print(f"args[{i}] is of type: {type(arg)}, value: {arg}")

    print(f"\n**kwargs is of type: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"kwargs[{key!r}] is of type: {type(value)}, value: {value}")

# Usage Examples
# Example 1: Passing All Arguments

demo_args_kwargs(
    [1, 2, 3],
    "Hello, World!",
    10, 3.14, "additional_arg",
    a=42, b="Python", c={"key": "value"}
)

# my_list is of type: <class 'list'>, value: [1, 2, 3]
# my_string is of type: <class 'str'>, value: Hello, World!
#
# *args is of type: <class 'tuple'>
# args[0] is of type: <class 'int'>, value: 10
# args[1] is of type: <class 'float'>, value: 3.14
# args[2] is of type: <class 'str'>, value: additional_arg
#
# **kwargs is of type: <class 'dict'>
# kwargs['a'] is of type: <class 'int'>, value: 42
# kwargs['b'] is of type: <class 'str'>, value: Python
# kwargs['c'] is of type: <class 'dict'>, value: {'key': 'value'}


# # Example 2: Omitting *args
#
# demo_args_kwargs(
#     [1, 2, 3],
#     "Only explicit args here!",
#     a=10, b="No positional args"
# )

# Example 3: Omitting **kwargs

# demo_args_kwargs(
#     [4, 5, 6],
#     "No keyword args here!",
#     42, 3.1415, "Another string"
# )

# Additional Arguments:
#
# my_list: Explicitly demonstrates how a list argument is handled.
# my_string: Explicitly demonstrates how a string argument is handled.
# Versatility:
#
# Still processes *args as a tuple and **kwargs as a dictionary, showing their data types.
# Flexible Inputs:
#
# Works seamlessly with or without *args and **kwargs.


def demo_function(operation_mode, *args, **kwargs):
    """
    Demonstrates the use of *args, **kwargs, and an additional variable.

    Args:
        operation_mode (str): A required argument to specify the mode of operation.
                              Example values: "sum", "concat", "process".

        *args: Variable-length positional arguments.
               - Supports any data structure (e.g., int, float, str, list, tuple, dict).
               - All positional arguments are accessible as a tuple.
               - Example: demo_function("sum", 1, 2, 3) -> args = (1, 2, 3)

        **kwargs: Variable-length keyword arguments.
                  - Supports any data structure (e.g., int, float, str, list, tuple, dict).
                  - All keyword arguments are accessible as a dictionary.
                  - Example: demo_function("process", a=1, b=2) -> kwargs = {"a": 1, "b": 2}

    Returns:
        Depends on the operation_mode:
        - If "sum": Returns the sum of numeric arguments.
        - If "concat": Returns a concatenated string from all arguments.
        - If "process": Processes **kwargs into a formatted dictionary.

    Examples:
        1. Summing numbers:
           demo_function("sum", 1, 2, 3)
           Output: 6

        2. Concatenating strings:
           demo_function("concat", "hello", "world", separator=" ")
           Output: "hello world"

        3. Processing kwargs:
           demo_function("process", a=1, b="test")
           Output: {"processed_kwargs": {"a": 1, "b": "test"}}
    """
    # Handle based on operation_mode
    if operation_mode == "sum":
        # Sum numeric arguments
        result = sum(arg for arg in args if isinstance(arg, (int, float)))
    elif operation_mode == "concat":
        # Concatenate strings with optional separator
        separator = kwargs.get("separator", "")
        result = separator.join(str(arg) for arg in args if isinstance(arg, str))
    elif operation_mode == "process":
        # Return a formatted dictionary of kwargs
        result = {"processed_kwargs": kwargs}
    else:
        raise ValueError(f"Unsupported operation_mode: {operation_mode}")

    return result

# Example 1: Summing Numbers (operation_mode="sum")
result = demo_function("sum", 1, 2, 3, 4.5, "not included")
print(result)
# Output: 10.5

# Example 3: Processing **kwargs (operation_mode="process")
result = demo_function("process", a=1, b="test", c=[3, 4])
print(result)
#{'processed_kwargs': {'a': 1, 'b': 'test', 'c': [3, 4]}}

# Python Function with try, except, finally, and raise

def process_data(input_list, input_dict):
    """
    A function to demonstrate try, except, finally, and raise with list and dictionary processing.

    Args:
        input_list (list): A list of integers to be processed.
        input_dict (dict): A dictionary where keys are strings and values are integers.

    Returns:
        dict: A dictionary containing processed results:
              - "list_sum": Sum of the list elements.
              - "dict_values_sum": Sum of the dictionary values.

    Raises:
        TypeError: If input_list is not a list or input_dict is not a dictionary.
        ValueError: If the list contains non-integer values or the dictionary contains non-integer values.

    Examples:
        1. Valid inputs:
           process_data([1, 2, 3], {"a": 10, "b": 20})
           Output: {"list_sum": 6, "dict_values_sum": 30}

        2. Invalid inputs:
           process_data("not a list", {"a": 10})
           Raises TypeError: "Expected a list for input_list."

        3. Invalid list values:
           process_data([1, "two"], {"a": 10})
           Raises ValueError: "All elements in input_list must be integers."
    """
    try:
        # Validate input types
        if not isinstance(input_list, list):
            raise TypeError("Expected a list for input_list.")
        if not isinstance(input_dict, dict):
            raise TypeError("Expected a dictionary for input_dict.")

        # Validate list elements
        if not all(isinstance(item, int) for item in input_list):
            raise ValueError("All elements in input_list must be integers.")

        # Validate dictionary values
        if not all(isinstance(value, int) for value in input_dict.values()):
            raise ValueError("All values in input_dict must be integers.")

        # Process data
        list_sum = sum(input_list)
        dict_values_sum = sum(input_dict.values())

        return {"list_sum": list_sum, "dict_values_sum": dict_values_sum}

    except TypeError as te:
        print(f"TypeError: {te}")
        raise  # Re-raise the exception after logging
    except ValueError as ve:
        print(f"ValueError: {ve}")
        raise  # Re-raise the exception after logging
    finally:
        print("Processing completed. Cleanup can be done here if needed.")

# Usage Examples
# 1. Valid Inputs

result = process_data([1, 2, 3], {"a": 10, "b": 20})
print(result)
# Output:
# Processing completed. Cleanup can be done here if needed.
# {"list_sum": 6, "dict_values_sum": 30}

# 2. Invalid Input Type for input_list

try:
    result = process_data("not a list", {"a": 10})
except Exception as e:
    print(f"Caught an exception: {e}")
# Output:
# TypeError: Expected a list for input_list.
# Processing completed. Cleanup can be done here if needed.
# Caught an exception: Expected a list for input_list.


# Python Function for File Operations

def file_operations(file_path, mode, content=None, encoding="utf-8"):
    """
    Perform file operations including reading, writing, and appending with error handling.

    Args:
        file_path (str): The path to the file to be operated on.
        mode (str): The mode of operation: "read", "write", or "append".
        content (str, optional): The content to write or append to the file. Required for "write" and "append".
        encoding (str, optional): The encoding to use when opening the file. Defaults to "utf-8".

    Returns:
        str: The content of the file if mode is "read".
        None: For "write" or "append" operations.

    Raises:
        ValueError: If an invalid mode is provided.
        FileNotFoundError: If the file is not found in "read" mode.
        Exception: For other file-related errors.

    Examples:
        1. Writing to a file:
           file_operations("example.txt", "write", content="Hello, World!")

        2. Appending to a file:
           file_operations("example.txt", "append", content="\nAppending this line.")

        3. Reading from a file:
           content = file_operations("example.txt", "read")
           print(content)
    """
    try:
        if mode == "read":
            with open(file_path, "r", encoding=encoding) as file:
                data = file.read()
                return data
        elif mode == "write":
            if content is None:
                raise ValueError("Content must be provided for 'write' mode.")
            with open(file_path, "w", encoding=encoding) as file:
                file.write(content)
        elif mode == "append":
            if content is None:
                raise ValueError("Content must be provided for 'append' mode.")
            with open(file_path, "a", encoding=encoding) as file:
                file.write(content)
        else:
            raise ValueError("Invalid mode. Use 'read', 'write', or 'append'.")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        raise
    except ValueError as e:
        print(f"ValueError: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        print(f"Operation '{mode}' completed on file: {file_path}.")

# Usage Examples
# 1. Writing to a File
file_operations("example.txt", "write", content="Hello, World!")

# Result:
# Creates (or overwrites if it exists) example.txt with the content "Hello, World!".

# Output:
# Copy code
# Operation 'write' completed on file: example.txt.

# 2. Appending to a File

file_operations("example.txt", "append", content="\nAppending this line.")

# Result:
#
# Appends "\nAppending this line." to example.txt.
# Output:
# Operation 'append' completed on file: example.txt.

# 3. Reading from a File
content = file_operations("example.txt", "read")
print(content)
# Result:
#
# Reads the content of example.txt and prints it.
# Output:
# Operation 'read' completed on file: example.txt.
# Hello, World!
# Appending this line.


# Mode Handling:
#
# "read": Reads the file's content and returns it.
# "write": Writes the provided content to the file (overwrites existing content).
# "append": Appends the provided content to the file.
# Error Handling:
#
# FileNotFoundError: Catches file not found errors for "read" mode.
# ValueError: Ensures valid input for mode and content requirements.
# Generic Exception: Handles any unexpected file operation errors.
# Encoding:
#
# Supports encoding for international text (default: "utf-8").
# Resource Management:
#
# Uses with open(...) to ensure files are properly closed after the operation.


#  if bool(x) == True : <=> if x :
#  if bool(x) == False : <=> if not x :


# Operation	Description
# write()	Writes a string to the file.
# writelines()	Writes multiple strings (from a list) to the file without adding newlines.
# close()	Closes the file explicitly.
# flush()	Flushes the internal buffer, forcing the content to be written to disk.
# tell()	Returns the current position of the file pointer.
# truncate()	Truncates the file to a specified size.
# seek()	Moves the file pointer to a specified position.
# read()	Reads the entire file content as a string.
# readlines()	Reads all lines from the file into a list.
# readline()	Reads a single line from the file.


def write_to_file(file_path, content):
    """
    Write content to a file.

    Args:
        file_path (str): The file path to write to.
        content (str): The content to write.

    Example:
        write_to_file("example.txt", "Hello, World!")
    """
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Content written to {file_path}")


def write_lines_to_file(file_path, lines):
    """
    Write multiple lines to a file.

    Args:
        file_path (str): The file path to write to.
        lines (list of str): The lines to write.

    Example:
        write_lines_to_file("example.txt", ["Line 1\n", "Line 2\n"])
    """
    with open(file_path, "w") as file:
        file.writelines(lines)
    print(f"Lines written to {file_path}")


def close_file(file_path):
    """
    Demonstrate explicitly closing a file.

    Args:
        file_path (str): The file to open and close.

    Example:
        close_file("example.txt")
    """
    file = open(file_path, "w")
    file.write("Temporary content")
    file.close()
    print(f"File {file_path} closed.")


def flush_file(file_path):
    """
    Flush buffered content to the file.

    Args:
        file_path (str): The file path to write to.

    Example:
        flush_file("example.txt")
    """
    with open(file_path, "w") as file:
        file.write("Buffered content")
        file.flush()
        print("File buffer flushed to disk.")


def tell_position(file_path):
    """
    Get the current position of the file pointer.

    Args:
        file_path (str): The file to demonstrate pointer position.

    Example:
        tell_position("example.txt")
    """
    with open(file_path, "w") as file:
        file.write("12345")
        position = file.tell()
        print(f"Current file pointer position: {position}")


def truncate_file(file_path, size):
    """
    Truncate the file to a specified size.

    Args:
        file_path (str): The file to truncate.
        size (int): The size to truncate the file to.

    Example:
        truncate_file("example.txt", 5)
    """
    with open(file_path, "w") as file:
        file.write("1234567890")
        file.truncate(size)
    print(f"File {file_path} truncated to {size} bytes.")


def seek_position(file_path, position):
    """
    Move the file pointer to a specified position.

    Args:
        file_path (str): The file to move the pointer in.
        position (int): The position to move to.

    Example:
        seek_position("example.txt", 2)
    """
    with open(file_path, "w+") as file:
        file.write("1234567890")
        file.seek(position)
        print(f"File pointer moved to position: {file.tell()}")


def read_file(file_path):
    """
    Read the entire content of a file.

    Args:
        file_path (str): The file to read.

    Returns:
        str: The file content.

    Example:
        content = read_file("example.txt")
        print(content)
    """
    with open(file_path, "r") as file:
        content = file.read()
    print(f"Read content from {file_path}: {content}")
    return content


def read_lines_from_file(file_path):
    """
    Read all lines from a file into a list.

    Args:
        file_path (str): The file to read.

    Returns:
        list of str: The lines from the file.

    Example:
        lines = read_lines_from_file("example.txt")
        print(lines)
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
    print(f"Read lines from {file_path}: {lines}")
    return lines


def read_line_from_file(file_path):
    """
    Read a single line from a file.

    Args:
        file_path (str): The file to read.

    Returns:
        str: The first line from the file.

    Example:
        line = read_line_from_file("example.txt")
        print(line)
    """
    with open(file_path, "r") as file:
        line = file.readline()
    print(f"Read line from {file_path}: {line}")
    return line


# Usage Examples
# 1. Writing Content to a File
write_to_file("example.txt", "Hello, World!")

# 2. Writing Multiple Lines to a File

write_lines_to_file("example.txt", ["Line 1\n", "Line 2\n", "Line 3\n"])

# 3. Closing a File Explicitly

close_file("example.txt")

# 4. Flushing Buffered Content

flush_file("example.txt")

# 5. Getting the File Pointer Position

tell_position("example.txt")

# 6. Truncating a File
truncate_file("example.txt", 5)

# 7. Moving the File Pointer
seek_position("example.txt", 2)

# 9. Reading All Lines
lines = read_lines_from_file("example.txt")
print(lines)

# Read lines from example.txt: ['1234567890']
# ['1234567890']
# 10. Reading a Single Line

line = read_line_from_file("example.txt")
print(line)
# Read line from example.txt: 1234567890
# 1234567890



# Key Differences Between str.format() and f-Strings
# Feature	str.format()	f-Strings
# Syntax	"{}".format(value)	f"{value}"
# Readability	Requires explicit .format() call	Directly embeds variables and expressions
# Performance	Slightly slower (parses templates at runtime)	Faster (evaluates at compile-time)
# Version Availability	Python 2.7+	Python 3.6+



# Here's a detailed explanation and examples of Python's format() and f-strings, including their usage in functions.
#
# 1. Using str.format() in a Function
# The str.format() method allows you to insert values into a string template.
#
# Example Function Using str.format()

def format_string_example(name, age, city):
    """
    Demonstrates the use of str.format() for string formatting.

    Args:
        name (str): The person's name.
        age (int): The person's age.
        city (str): The city where the person lives.

    Returns:
        str: A formatted string using str.format().
    """
    formatted_string = "Hello, my name is {}. I am {} years old and I live in {}.".format(name, age, city)
    return formatted_string

result = format_string_example("Alice", 30, "New York")
print(result)
#
# Hello, my name is Alice. I am 30 years old and I live in New York.


# 2. Using f-Strings in a Function
# F-strings (introduced in Python 3.6) provide a concise and readable way to embed expressions directly into string literals.
#
# Example Function Using f-Strings

def f_string_example(name, age, city):
    """
    Demonstrates the use of f-strings for string formatting.

    Args:
        name (str): The person's name.
        age (int): The person's age.
        city (str): The city where the person lives.

    Returns:
        str: A formatted string using f-strings.
    """
    formatted_string = f"Hello, my name is {name}. I am {age} years old and I live in {city}."
    return formatted_string

# Usage
result = f_string_example("Alice", 30, "New York")
print(result)
# Output:
# Hello, my name is Alice. I am 30 years old and I live in New York.


# Comparison of str.format() and f-Strings
# Here’s an example to show both methods in the same function:

def compare_format_methods(name, age, city):
    """
    Compares str.format() and f-strings for string formatting.

    Args:
        name (str): The person's name.
        age (int): The person's age.
        city (str): The city where the person lives.

    Returns:
        dict: A dictionary with formatted strings using both methods.
    """
    using_format = "Using str.format(): Hello, my name is {}. I am {} years old and I live in {}.".format(name, age, city)
    using_fstring = f"Using f-strings: Hello, my name is {name}. I am {age} years old and I live in {city}."
    return {"str.format": using_format, "f-strings": using_fstring}

# Usage

result = compare_format_methods("Bob", 25, "Los Angeles")
print(result["str.format"])
print(result["f-strings"])

# Output

# Using str.format(): Hello, my name is Bob. I am 25 years old and I live in Los Angeles.
# Using f-strings: Hello, my name is Bob. I am 25 years old and I live in Los Angeles.

# Advanced Usage Examples
# 1. Formatting Numbers

def format_numbers_example(value):
    return {
        "default": f"The value is {value}",
        "fixed_decimal": f"The value is {value:.2f}",
        "scientific": f"The value is {value:.2e}",
        "percentage": f"The value is {value:.2%}",
    }

result = format_numbers_example(1234.5678)
print(result)

# Output

# {
#     'default': 'The value is 1234.5678',
#     'fixed_decimal': 'The value is 1234.57',
#     'scientific': 'The value is 1.23e+03',
#     'percentage': 'The value is 123456.78%'
# }

# 2. Aligning Text

def align_text_example(left, center, right):
    return {
        "left_aligned": f"{left:<10}",    # Align left with width 10
        "center_aligned": f"{center:^10}", # Center with width 10
        "right_aligned": f"{right:>10}",  # Align right with width 10
    }

result = align_text_example("Left", "Center", "Right")
print(result)

# Output

# {
#     'left_aligned': 'Left      ',
#     'center_aligned': '  Center  ',
#     'right_aligned': '     Right'
# }

# 3. Embedding Calculations
def f_string_calculations(a, b):
    """
    Demonstrates embedding calculations in f-strings.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        str: A formatted string with calculations.
    """
    return f"The sum of {a} and {b} is {a + b}. The product is {a * b}."

result = f_string_calculations(5, 10)
print(result)
# Output
#The sum of 5 and 10 is 15. The product is 50.



# Here’s the updated Python class for Binary Search Tree (BST) with a
# tree diagram included in the docstring to provide better visualization. The diagram helps illustrate how the tree structure evolves as values are inserted.
#
# Updated Code with Tree Diagram in Docstring

class TreeNode:
    """
    A class representing a node in the Binary Search Tree.

    Attributes:
        value (int): The value of the node.
        left (TreeNode): Reference to the left child.
        right (TreeNode): Reference to the right child.

    Example Tree Structure:
        Insert values in this order: [15, 10, 20, 8, 12, 17, 25]

        The resulting BST:
                  15
                 /  \
               10    20
              / \    / \
             8  12  17  25
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_into_bst(root, value):
    """
    Insert a value into the BST.

    This function recursively inserts a value into the correct position in the tree.

    Args:
        root (TreeNode): The root of the tree.
        value (int): The value to insert.

    Returns:
        TreeNode: The root of the updated tree.

    Example:
        Insert values: [15, 10, 20, 8, 12]

        Tree structure:
                  15
                 /  \
               10    20
              / \
             8  12
    """
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    elif value > root.value:
        root.right = insert_into_bst(root.right, value)

    return root


def inorder_traversal(root):
    """
    Perform an inorder traversal of the BST.

    This traversal visits nodes in the order: left subtree → root → right subtree.

    Args:
        root (TreeNode): The root of the tree.

    Returns:
        list: The values in the BST in sorted order.

    Example:
        For this tree:
                  15
                 /  \
               10    20
              / \
             8  12

        Inorder traversal result: [8, 10, 12, 15, 20]
    """
    if root is None:
        return []

    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)


def build_bst_from_array(arr):
    """
    Build a BST from an array of integers.

    This function iteratively inserts each value from the array into the BST.

    Args:
        arr (list): The array of integers.

    Returns:
        TreeNode: The root of the BST.

    Example:
        Input Array: [15, 10, 20, 8, 12, 17, 25]

        Tree structure:
                  15
                 /  \
               10    20
              / \    / \
             8  12  17  25

        Inorder traversal result: [8, 10, 12, 15, 17, 20, 25]
    """
    root = None
    for value in arr:
        root = insert_into_bst(root, value)
    return root
# Example Usage
# 1. Building and Traversing the Tree

# Step 1: Create an array of integers
values = [15, 10, 20, 8, 12, 17, 25]

# Step 2: Build the BST
root = build_bst_from_array(values)

# Step 3: Perform an inorder traversal
print("Inorder Traversal:", inorder_traversal(root))
# Output:

# less
# Copy code
# Inorder Traversal: [8, 10, 12, 15, 17, 20, 25]
# Tree Visualization
# For the input array [15, 10, 20, 8, 12, 17, 25], the BST looks like this:
#
# markdown
# Copy code
#           15
#          /  \
#        10    20
#       / \    / \
#      8  12  17  25
# Tree Diagram for Each Step
# Insert 15:
#
# markdown
# Copy code
#        15
# Insert 10:
#
# markdown
# Copy code
#        15
#       /
#     10
# Insert 20:
#
# markdown
# Copy code
#        15
#       /  \
#     10    20
# Insert 8:
#
# markdown
# Copy code
#        15
#       /  \
#     10    20
#    /
#   8
# Insert 12:

# markdown
# Copy code
#        15
#       /  \
#     10    20
#    / \
#   8  12
# Insert 17:

# markdown
# Copy code
#        15
#       /  \
#     10    20
#    / \    /
#   8  12  17
# Insert 25:

# markdown
# Copy code
#        15
#       /  \
#     10    20
#    / \    / \
#   8  12  17  25
# Final Example

values = [15, 10, 20, 8, 12, 17, 25]
root = build_bst_from_array(values)

# Perform inorder traversal
print("Inorder Traversal:", inorder_traversal(root))
# Output: [8, 10, 12, 15, 17, 20, 25]

# Insert a new value
insert_into_bst(root, 18)
print("Inorder Traversal after inserting 18:", inorder_traversal(root))
# Output: [8, 10, 12, 15, 17, 18, 20, 25]
# This step-by-step illustration and docstring make it clear how the Binary Search Tree grows
# with each insertion, along with its output after an inorder traversal. Let me know if you need further details!

#Summary of Stack vs Queue

# Operation	Stack (LIFO)	Queue (FIFO)
# Add	push() (Top of stack)	enqueue() (Rear of queue)
# Remove	pop() (Top of stack)	dequeue() (Front of queue)
# Peek	peek() (Top element)	peek() (Front element)
# Check Empty	is_empty()	is_empty()
# Size	size()	size()

# Here’s an implementation of Stack and Queue classes in Python. Both include
# all standard operations, docstrings, and
# diagrams illustrating how the data structures work for adding and removing elements.

# Stack
# A stack is a Last-In-First-Out (LIFO) data structure:
#
# Push: Adds an element to the top of the stack.
# Pop: Removes the top element.
# Peek: Views the top element without removing it.
# IsEmpty: Checks if the stack is empty.

# Stack Diagram :  Last-In-First-Out (LIFO) data structure: browser
# Initial Stack:
# [ ]
# After Push (5, 10):
#
# [10]   <- Top
# [ 5 ]
#
# After Pop:
# [ 5 ]   <- Top

# Stack Implementation

class Stack:
    """
    A class to represent a Stack (LIFO).

    Operations:
        - push: Add an element to the stack.
        - pop: Remove and return the top element.
        - peek: Return the top element without removing it.
        - is_empty: Check if the stack is empty.
        - size: Return the number of elements in the stack.

    Example:
        # >>> stack = Stack()
        # >>> stack.push(5)
        # >>> stack.push(10)
        # >>> print(stack.peek())  # Output: 10
        # >>> print(stack.pop())   # Output: 10
        # >>> print(stack.is_empty())  # Output: False
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The element to add.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top element of the stack.

        Returns:
            The top element of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top element of the stack without removing it.

        Returns:
            The top element of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.items)

# Stack Usage Example

stack = Stack()
stack.push(5)
stack.push(10)
print("Top Element:", stack.peek())  # Output: Top Element: 10
print("Removed Element:", stack.pop())  # Output: Removed Element: 10
print("Is Empty:", stack.is_empty())  # Output: Is Empty: False


# Queue
# A queue is a First-In-First-Out (FIFO) data structure:
#
# Enqueue: Adds an element to the rear.
# Dequeue: Removes the front element.
# Peek: Views the front element without removing it.
# IsEmpty: Checks if the queue is empty.
# Queue Diagram
# Initial Queue: First-In-First-Out (FIFO)

# [ ]
# After Enqueue (5, 10):
# [5] <- Front
# [10] <- Rear
# After Dequeue:
# [10] <- Front and Rear
# Queue Implementation

class Queue:
    """
    A class to represent a Queue (FIFO).

    Operations:
        - enqueue: Add an element to the rear of the queue.
        - dequeue: Remove and return the front element.
        - peek: Return the front element without removing it.
        - is_empty: Check if the queue is empty.
        - size: Return the number of elements in the queue.

    Example:
        # >>> queue = Queue()
        # >>> queue.enqueue(5)
        # >>> queue.enqueue(10)
        # >>> print(queue.peek())  # Output: 5
        # >>> print(queue.dequeue())  # Output: 5
        # >>> print(queue.is_empty())  # Output: False
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args:
            item: The element to add.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front element of the queue.

        Returns:
            The front element of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        """
        Return the front element of the queue without removing it.

        Returns:
            The front element of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the size of the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self.items)

queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
print("Front Element:", queue.peek())  # Output: Front Element: 5
print("Removed Element:", queue.dequeue())  # Output: Removed Element: 5
print("Is Empty:", queue.is_empty())  # Output: Is Empty: False


# Why These Algorithms Are Popular
# Quick Sort:
# Most practical for general-purpose sorting and commonly found in coding interviews.
# Merge Sort:
# A go-to algorithm for recursion problems or stability requirements.
# Heap Sort:
# Directly tied to heap-related problems, like priority queues or finding
# 𝑘
# k-largest elements.
# Counting Sort / Radix Sort:
# Frequently asked for sorting categorical or integer data efficiently.

# Real-World Scenarios
# Quick Sort:
#
# Sorting large datasets in memory (general-purpose use).
# Merge Sort:
#
# Sorting linked lists or external sorting (e.g., sorting files on disk).
# Heap Sort:
#
# Finding the top
# 𝑘
# k elements in streaming data.
# Counting Sort:
#
# Sorting grades, ranks, or categorical data in a limited range.
# Radix Sort:
#
# Sorting long numbers or strings (e.g., phone numbers or IP addresses).
# Tim Sort:
#
# Used internally by Python and Java for real-world datasets.


# | Algorithm       | Best Case   | Worst Case  | Space Complexity | Stable | Use Case                                                                                   |
# |------------------|-------------|-------------|-------------------|--------|-------------------------------------------------------------------------------------------|
# | Quick Sort       | O(n log n)  | O(n^2)      | O(log n)          | No     | Most commonly used for general-purpose sorting. Tests divide-and-conquer strategies.      |
# | Merge Sort       | O(n log n)  | O(n log n)  | O(n)              | Yes    | Used for large datasets requiring stability. Tests recursion and merge logic.             |
# | Heap Sort        | O(n log n)  | O(n log n)  | O(1)              | No     | Space-efficient sorting or priority queue problems. Tests finding top K elements.         |
# | Counting Sort    | O(n + k)    | O(n + k)    | O(k)              | Yes    | Used for integer sorting in a limited range. Efficient for categorical data like scores.  |
# | Radix Sort       | O(nk)       | O(nk)       | O(n + k)          | Yes    | Used to sort large integers or strings with fixed digit lengths.                          |
# | Insertion Sort   | O(n)        | O(n^2)      | O(1)              | Yes    | Often tested for small or nearly sorted datasets. Simple and easy to optimize.            |
# | Tim Sort         | O(n)        | O(n log n)  | O(n)              | Yes    | Default in Python and Java. Efficient for real-world datasets with mixed patterns.         |
# | Bucket Sort      | O(n + k)    | O(n^2)      | O(n + k)          | Yes    | Suitable for uniformly distributed datasets, like sorting floating-point numbers.         |
# | Bubble Sort      | O(n)        | O(n^2)      | O(1)              | Yes    | Rarely use

# Here’s a comprehensive guide to implementing Singly-Linked List, Doubly-Linked List, Hash
# Table, Depth First Search (DFS), and Breadth First Search (BFS) in Python. Each includes:
#
# Textual explanation of the data structure/algorithm.
# Supported operations and use cases.
# Python class implementation with detailed docstrings.
# Examples of how to use the class and execute operations.



#Here’s a comprehensive guide to implementing Singly-Linked List, Doubly-Linked List, Hash Table,
# Depth First Search (DFS), and Breadth First Search (BFS) in Python. Each includes:
#
# Textual explanation of the data structure/algorithm.
# Supported operations and use cases.
# Python class implementation with detailed docstrings.
# Examples of how to use the class and execute operations.
#
# 1. Singly-Linked List
# What is a Singly-Linked List?
# A singly-linked list is a data structure consisting of nodes, where each node contains:
# A value.
# A pointer/reference to the next node.
# It allows efficient insertions and deletions compared to arrays but lacks direct indexing.
# Supported Operations
# Insert: Add a node at the beginning, end, or a specific position.
# Delete: Remove a node by value or position.
# Search: Find a node by its value.
# Traverse: Iterate through all nodes in the list.
# Use Cases
# Used when frequent insertions and deletions are needed.
# Good for implementing stacks and queues.

# Class Implementation

class SinglyLinkedList:
    """
    A class to represent a Singly-Linked List.

    Operations:
        - append(value): Add a node to the end.
        - prepend(value): Add a node to the beginning.
        - delete(value): Remove the first node with the given value.
        - search(value): Find the first node with the given value.
        - traverse(): Print all the elements in the list.
    """

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Add a node to the end of the list.
        """
        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        """
        Add a node to the beginning of the list.
        """
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """
        Remove the first node with the given value.
        """
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def search(self, value):
        """
        Find the first node with the given value.
        Returns:
            Node or None
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def traverse(self):
        """
        Print all elements in the list.
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

#How to Use

# Create a singly-linked list
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.prepend(0)
sll.traverse()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Search for a node
node = sll.search(2)
print("Found:", node.value if node else "Not Found")  # Output: Found: 2

# Delete a node
sll.delete(2)
sll.traverse()  # Output: 0 -> 1 -> 3 -> None


# 2. Doubly-Linked List
# What is a Doubly-Linked List?
# A doubly-linked list is similar to a singly-linked list but each node has:
# A reference to the next node.
# A reference to the previous node.
# Allows traversal in both directions.
# Supported Operations
# Same as singly-linked list but includes efficient backward traversal.
# Use Cases
# Good for implementing navigation systems (e.g., browser back/forward history).
# Better than singly-linked lists when frequent backward traversals are needed.

# Class Implementation

class DoublyLinkedList:
    """
    A class to represent a Doubly-Linked List.

    Operations:
        - append(value): Add a node to the end.
        - prepend(value): Add a node to the beginning.
        - delete(value): Remove the first node with the given value.
        - traverse_forward(): Print all elements from head to tail.
        - traverse_backward(): Print all elements from tail to head.
    """

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Add a node to the end of the list.
        """
        new_node = self.Node(value)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, value):
        """
        Add a node to the beginning of the list.
        """
        new_node = self.Node(value)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, value):
        """
        Remove the first node with the given value.
        """
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        current = self.head
        while current and current.value != value:
            current = current.next
        if current:
            if current.next:
                current.next.prev = current.prev
            else:
                self.tail = current.prev
            if current.prev:
                current.prev.next = current.next

    def traverse_forward(self):
        """
        Print all elements from head to tail.
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """
        Print all elements from tail to head.
        """
        current = self.tail
        while current:
            print(current.value, end=" <- ")
            current = current.prev
        print("None")
#How to Use

# Create a doubly-linked list
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.traverse_forward()  # Output: 0 -> 1 -> 2 -> 3 -> None
dll.traverse_backward()  # Output: 3 <- 2 <- 1 <- 0 <- None

# Delete a node
dll.delete(2)
dll.traverse_forward()  # Output: 0 -> 1 -> 3 -> None

# Covering the implementations for Hash Table, Depth First Search (DFS),
# and Breadth First Search (BFS) in Python.

# 3. Hash Table
# What is a Hash Table?
# A hash table is a data structure that uses a hash function to map keys to indices in an array.
# It provides O(1) average-time complexity for insert, search, and delete operations.
# Supported Operations
# Insert: Add a key-value pair.
# Search: Find a value by its key.
# Delete: Remove a key-value pair.
# Update: Change the value for a given key.
# Use Cases
# Fast lookups for key-value pairs (e.g., dictionaries, caches, sets).

# Summary
# Hash Table: Efficiently stores and retrieves key-value pairs.
# DFS: Explores graph/tree depth-first, useful for finding paths and connected components.
# BFS: Explores graph/tree breadth-first, ideal for shortest-path problems.


#Class Implementation

class HashTable:
    """
    A class to represent a simple Hash Table.

    Operations:
        - insert(key, value): Add a key-value pair.
        - search(key): Retrieve the value associated with a key.
        - delete(key): Remove a key-value pair.
    """

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty buckets

    def _hash_function(self, key):
        """
        Generate a hash for the given key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        """
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        self.table[index].append((key, value))

    def search(self, key):
        """
        Search for a value by its key.
        """
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        """
        Delete a key-value pair by its key.
        """
        index = self._hash_function(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
# How to Use

# Create a hash table
ht = HashTable()

# Insert key-value pairs
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city", "New York")

# Search for a key
print("Name:", ht.search("name"))  # Output: Name: Alice

# Delete a key
ht.delete("age")
print("Age:", ht.search("age"))  # Output: Age: None

# 4. Depth First Search (DFS)
# What is DFS?
# DFS is an algorithm used to traverse or search through graphs or trees.
# It starts at a root node and explores as far along each branch as possible before backtracking.
# Supported Operations
# Traverses nodes in depth-first order.
# Can detect cycles and find connected components in graphs.
# Use Cases
# Finding paths in a maze.
# Topological sorting in directed graphs.

#Class Implementation

class GraphDFS:
    """
    A class to represent a graph and perform Depth First Search (DFS).

    Operations:
        - add_edge(u, v): Add an edge between two nodes.
        - dfs(start): Perform DFS starting from a given node.
    """
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """
        Add an edge between nodes u and v.
        """
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        """
        Perform Depth First Search starting from the given node.
        """
        visited = set()

        def _dfs_recursive(node):
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    _dfs_recursive(neighbor)

        _dfs_recursive(start)

# How to Use

# Create a graph
g = GraphDFS()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

# Perform DFS
print("DFS Traversal:")
g.dfs(0)  # Output: DFS Traversal: 0 1 3 4 2 5 6

# 5. Breadth First Search (BFS)

# What is BFS?
# BFS is an algorithm used to traverse or search through graphs or trees.
# It explores all nodes at the current depth level before moving to the next level.
# Supported Operations
# Traverses nodes in breadth-first order.
# Finds the shortest path in unweighted graphs.
# Use Cases
# Finding the shortest path in a maze.
# Social network analysis.

# Class Implementation

from collections import deque

class GraphBFS:
    """
    A class to represent a graph and perform Breadth First Search (BFS).

    Operations:
        - add_edge(u, v): Add an edge between two nodes.
        - bfs(start): Perform BFS starting from a given node.
    """
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """
        Add an edge between nodes u and v.
        """
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        """
        Perform Breadth First Search starting from the given node.
        """
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# How to Use

# Create a graph
g = GraphBFS()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

# Perform BFS
print("BFS Traversal:")
g.bfs(0)  # Output: BFS Traversal: 0 1 2 3 4 5 6


# Trie Overview
# What is a Trie?
# A trie (pronounced "try") is a tree-like data structure used for efficiently
# storing and searching strings, especially when working with prefixes. Each node in the trie represents a single character of a string.
#
# How Does a Trie Work?
# The root node is empty and acts as the starting point.
# Each edge represents a character.
# Each node may have multiple children, each corresponding to a character.
# A special marker (e.g., is_end) indicates the end of a word.
# For example, storing the words "cat", "cap", and "dog" in a trie looks like this:

  #
  #       [root]
  #       /   \
  #      c     d
  #     / \      \
  #    a   a      o
  #   /     \       \
  #  t       p       g
  # [end]  [end]    [end]



# When to Use a Trie?
# Auto-complete: Quickly find all words with a given prefix.
# Spell checking: Verify if a word exists in a dictionary.
# Word games: Efficiently search for valid words or prefixes in games like Scrabble.
# IP Routing: Use for longest prefix matching.
# Search Engines: Fast retrieval of strings based on prefixes.
# Key Operations
# Insert: Add a word to the trie.
# Search: Check if a word exists in the trie.
# StartsWith: Check if any word in the trie starts with a given prefix.

# Trie Class Implementation
# Here’s a Python implementation of a trie with the essential operations:


class TrieNode:
    """
    A class representing a single node in a Trie.
    """

    def __init__(self):
        self.children = {}  # Dictionary to hold children nodes
        self.is_end_of_word = False  # Marks the end of a complete word


class Trie:
    """
    A class to represent a Trie (Prefix Tree).

    Operations:
        - insert(word): Add a word to the Trie.
        - search(word): Check if a word exists in the Trie.
        - starts_with(prefix): Check if any word in the Trie starts with a given prefix.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.

        Args:
            word (str): The word to insert.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        """
        Search for a word in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists, False otherwise.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        """
        Check if there is any word in the Trie that starts with the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            bool: True if there is a word with the prefix, False otherwise.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def collect_all_words(self):
        """
        Collect all words stored in the Trie.

        Returns:
            list: A list of all words in the Trie.
        """
        result = []

        def dfs(node, prefix):
            if node.is_end_of_word:
                result.append(prefix)
            for char, child_node in node.children.items():
                dfs(child_node, prefix + char)

        dfs(self.root, "")
        return result

# How to Use

# Create a Trie instance
trie = Trie()

# Insert words into the Trie
trie.insert("cat")
trie.insert("cap")
trie.insert("dog")

# Search for words
print("Search 'cat':", trie.search("cat"))  # Output: True
print("Search 'can':", trie.search("can"))  # Output: False

# Check prefixes
print("Starts with 'ca':", trie.starts_with("ca"))  # Output: True
print("Starts with 'do':", trie.starts_with("do"))  # Output: True
print("Starts with 'de':", trie.starts_with("de"))  # Output: False

# Collect all words
print("All words in Trie:", trie.collect_all_words())
# Output: ['cat', 'cap', 'dog']


# Explanation of Operations
# Insert (insert(word)):
#
# Traverse the trie, creating nodes for each character if they don’t already exist.
# Mark the last node of the word as is_end_of_word.
# Search (search(word)):
#
# Traverse the trie following the characters of the word.
# Return True if all characters are found, and the last character is marked as is_end_of_word.
# Starts With (starts_with(prefix)):
#
# Traverse the trie following the prefix.
# Return True if all characters of the prefix exist in the trie.
# Collect All Words (collect_all_words()):
#
# Use Depth-First Search (DFS) to traverse all paths in the trie and collect complete words.

# Use Cases in Action
# Auto-complete Example

# Insert words
trie.insert("hello")
trie.insert("help")
trie.insert("helicopter")
trie.insert("hero")

# Find all words with prefix "hel"
words_with_hel = [word for word in trie.collect_all_words() if word.startswith("hel")]
print("Words with 'hel':", words_with_hel)
# Output: ['hello', 'help', 'helicopter']

# Spell Checking Example

# Create a dictionary using the Trie
dictionary = Trie()
dictionary.insert("apple")
dictionary.insert("banana")
dictionary.insert("grape")

# Check for valid words
print("Is 'apple' a valid word?:", dictionary.search("apple"))  # Output: True
print("Is 'orange' a valid word?:", dictionary.search("orange"))  # Output: False


# Advantages of a Trie
# Fast prefix-based searches (𝑂(𝐿) O(L), where 𝐿 L is the length of the word or prefix).
# Space-efficient for large sets of words with shared prefixes.
# Can handle a variety of applications like auto-complete, dictionary searches, and routing.
# Limitations
# Higher memory usage compared to hash tables for small datasets.
# Not ideal for cases with non-overlapping keys (use a hash table instead).
