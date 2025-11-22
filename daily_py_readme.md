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
