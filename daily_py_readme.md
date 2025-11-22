# Unified Table – Python Data Types (Methods + Patterns + Loops)

## 📌 Method Calling Pattern
All types follow:


---

## 📌 Unified Table

| Data Type | Method | Call Pattern | Example | What It Does | Exception | Loop Pattern |
|-----------|---------|---------------|----------|----------------|-------------|----------------|
| **str** | `upper` | `s.upper()` | `"hi".upper()` | Uppercase string | — | `for ch in s:` |
| str | `lower` | `s.lower()` | `"HI".lower()` | Lowercase string | — | `for ch in s:` |
| str | `strip` | `s.strip()` | `" hi ".strip()` | Trim whitespace | — | `for ch in s:` |
| str | `split` | `s.split(",")` | `"a,b".split(",")` | Split into list | `TypeError` if bad sep | `for ch in s:` |
| str | `join` | `sep.join(list)` | `",".join(["a","b"])` | Join list into string | `TypeError` if non-string inside list | `for ch in s:` |
| str | `replace` | `s.replace(a,b)` | `"a-b".replace("-", "_")` | Replace substring | — | `for ch in s:` |
| str | `find` | `s.find(x)` | `"hi".find("i")` | Index or -1 | — | `for ch in s:` |
| str | `index` | `s.index(x)` | `"hi".index("i")` | Index or error | `ValueError` | `for ch in s:` |
| str | `count` | `s.count(x)` | `"hello".count("l")` | Count occurrences | — | `for ch in s:` |
| **list** | `append` | `lst.append(x)` | `[1,2].append(3)` | Add to end | — | `for x in lst:` |
| list | `extend` | `lst.extend(it)` | `lst.extend([4,5])` | Add all items | — | `for x in lst:` |
| list | `insert` | `lst.insert(i,x)` | `lst.insert(0,99)` | Insert at index | — | `for x in lst:` |
| list | `remove` | `lst.remove(x)` | `lst.remove(3)` | Remove first x | `ValueError` | `for x in lst:` |
| list | `pop` | `lst.pop()` | `lst.pop()` | Remove & return | `IndexError` | `for x in lst:` |
| list | `sort` | `lst.sort()` | `lst.sort()` | Sort in-place | `TypeError` | `for x in lst:` |
| list | `reverse` | `lst.reverse()` | `lst.reverse()` | Reverse list | — | `for x in lst:` |
| **dict** | `get` | `d.get(k)` | `d.get("age")` | Safe key access | — | `for k in d:` |
| dict | `keys` | `d.keys()` | `d.keys()` | All keys | — | `for k in d:` |
| dict | `values` | `d.values()` | `d.values()` | All values | — | `for v in d.values():` |
| dict | `items` | `d.items()` | `d.items()` | Key/value pairs | — | `for k,v in d.items():` |
| dict | `update` | `d.update(x)` | `d.update({})` | Merge dicts | `TypeError` | `for k,v in d.items():` |
| dict | `pop` | `d.pop(k)` | `d.pop("age")` | Remove key | `KeyError` | `for k in d:` |
| dict | `popitem` | `d.popitem()` | `d.popitem()` | Remove last pair | `KeyError` | `for k,v in d.items():` |
| **tuple** | `count` | `t.count(x)` | `(1,2,2).count(2)` | Count value | — | `for x in t:` |
| tuple | `index` | `t.index(x)` | `(1,2,3).index(2)` | Find index | `ValueError` | `for x in t:` |

---

## 📌 Loop Patterns (Quick Copy)

```python
# String
for ch in s:
    ...

# List
for item in lst:
    ...
for i, item in enumerate(lst):
    ...

# Dictionary
for k in d:
    ...
for v in d.values():
    ...
for k, v in d.items():
    ...

# Tuple
for item in t:
    ...


# Python Type Hints Explained (List, String, Dict, Tuple)  
### And Explanation of the Function:  
### `def find_first(nums: List[int], target: int) -> int`

## 📌 What Does This Code Mean?

```python
from typing import List

def find_first(nums: List[int], target: int) -> int:
```

This code defines a Python function using type hints.
Let’s break it down in simple English.

---

# 1. `from typing import List`

Python has a module called `typing` that provides type hints.

`List` is one such type hint.

This line means:

“Import the `List` type so we can show that a variable should be a list.”

Type hints do not change how the program runs —  
they only help humans understand the code better.

---

# 2. Understanding the Function Definition

```python
def find_first(nums: List[int], target: int) -> int:
```

## 🔹 `def find_first(...)`

This defines a function named `find_first`.

## 🔹 `nums: List[int]`

`nums` → parameter name  
`List[int]` → a list where each element is an integer  

Example:

```python
nums = [1, 2, 3, 4]
```

English meaning:

"`nums` should be a list of integers."

## 🔹 `target: int`

`target` → parameter name  
`int` → should be an integer

Example:

```python
target = 3
```

English meaning:

"`target` should be a single integer."

## 🔹 `-> int`

Return type hint.

Meaning:  
“This function will return an integer.”

If `target` is not found, the function returns `-1`.

---

# ✔ Full Meaning in English

```python
def find_first(nums: List[int], target: int) -> int:
```

Means:

“Define a function named `find_first` that takes  
• a list of integers (`nums`)  
• an integer (`target`)  
and returns an integer representing the **first index** of the target.”

---

# ✔ Example

```python
find_first([5, 7, 7, 8, 8], 8)
```

Returns:

```
3
```

Because 8 first appears at index 3.

---

# 3. Type Hints for Other Data Types

## ✔ String (`str`)

```python
def greet(name: str) -> str:
    return "Hello " + name
```

## ✔ List (`List[type]`)

```python
from typing import List

def total(nums: List[int]) -> int:
    return sum(nums)
```

## ✔ Dictionary (`dict[key_type, value_type]`)

```python
def get_age(person: dict[str, int]) -> int:
    return person.get("age", 0)
```

## ✔ Tuple (`tuple[type, type, ...]`)

```python
def add_point(p: tuple[int, int]) -> int:
    return p[0] + p[1]
```

---

# 4. Combined Example Using All Types

```python
from typing import List

def process_data(name: str, scores: List[int], stats: dict[str, float], point: tuple[int, int]) -> str:
    return f"{name} scored {sum(scores)}, average={stats['avg']}, point={point}"
```

Uses:

- `str`
- `List[int]`
- `dict[str, float]`
- `tuple[int, int]`

---
