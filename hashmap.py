"""
Hash Table (HashMap) Implementation
=================================

Core Operations and Their Time Complexity:
1. Insert: O(1) average, O(n) worst case
2. Search: O(1) average, O(n) worst case
3. Delete: O(1) average, O(n) worst case
4. Resize: O(n) when load factor is exceeded
5. Collision Handling: Using chaining (linked lists)

How Hash Table Works:
--------------------
1. Hash Function:
   - Takes a key and converts it to an index
   - Example: hash("name") % table_size = index
   - Same key always gives same index
   - Different keys might give same index (collision)

2. Buckets and Chaining:
   - Each index has a bucket (list)
   - When collision occurs, items are chained in the bucket
   - Example: Index 1 -> [("name", "John"), ("age", 30)]

3. Load Factor:
   - Ratio of items to table size
   - When load factor > threshold (0.75), table resizes
   - Resizing doubles the table size

Detailed Visualization Examples:
------------------------------
1. Basic Insertion:
   Input: ("name", "John")
   Hash Function: hash("name") % 4 = 1
   Output:
   Index 0: []
   Index 1: [("name", "John")]
   Index 2: []
   Index 3: []

2. Collision Example:
   Input 1: ("name", "John") -> hash("name") % 4 = 1
   Input 2: ("age", 30) -> hash("age") % 4 = 1
   Output:
   Index 0: []
   Index 1: [("name", "John") -> ("age", 30)]
   Index 2: []
   Index 3: []

3. Delete Operation:
   Before:
   Index 0: []
   Index 1: [("name", "John") -> ("age", 30)]
   Index 2: []
   Index 3: []
   
   Input: Delete "age"
   Output:
   Index 0: []
   Index 1: [("name", "John")]
   Index 2: []
   Index 3: []

4. Resize Operation:
   Before (Size = 4):
   Index 0: [("key1", "value1")]
   Index 1: [("key2", "value2")]
   Index 2: [("key3", "value3")]
   Index 3: []
   Load Factor: 3/4 = 0.75 (triggers resize)
   
   After (Size = 8):
   Index 0: [("key1", "value1")]
   Index 1: [("key2", "value2")]
   Index 2: [("key3", "value3")]
   Index 3: []
   Index 4: []
   Index 5: []
   Index 6: []
   Index 7: []
   Load Factor: 3/8 = 0.375

5. Search Operation:
   Input: Search for "name"
   Hash Function: hash("name") % 4 = 1
   Process:
   1. Go to Index 1
   2. Search through chain: [("name", "John") -> ("age", 30)]
   3. Find "name" at first position
   Output: "John"

6. Load Factor Example:
   Table Size = 4
   Items = [("a", 1), ("b", 2), ("c", 3)]
   Load Factor = 3/4 = 0.75
   Action: Add ("d", 4)
   Result: Table resizes to size 8
   New Load Factor = 4/8 = 0.5

7. Hash Distribution Example:
   Input Data:
   [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
   
   Hash Values:
   hash("a") % 4 = 1
   hash("b") % 4 = 2
   hash("c") % 4 = 3
   hash("d") % 4 = 0
   hash("e") % 4 = 1
   
   Final Distribution:
   Index 0: [("d", 4)]
   Index 1: [("a", 1) -> ("e", 5)]
   Index 2: [("b", 2)]
   Index 3: [("c", 3)]
   
   Collision Rate: 1/5 = 20%
"""

class HashTable:
    def __init__(self, initial_size=10, load_factor=0.75):
        self.size = initial_size
        self.load_factor = load_factor
        self.count = 0
        self.table = [[] for _ in range(initial_size)]

    def _hash(self, key):
        """Hash function using Python's built-in hash"""
        return hash(key) % self.size

    def _resize(self):
        """Resize the table when load factor is exceeded"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        # Rehash all elements
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        """Insert key-value pair into hash table"""
        if self.count / self.size >= self.load_factor:
            self._resize()

        index = self._hash(key)
        bucket = self.table[index]

        # Check if key exists and update value
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Add new key-value pair
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        """Get value for a given key"""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Delete key-value pair from hash table"""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def contains(self, key):
        """Check if key exists in hash table"""
        return self.get(key) is not None

    def keys(self):
        """Get all keys in hash table"""
        return [k for bucket in self.table for k, _ in bucket]

    def values(self):
        """Get all values in hash table"""
        return [v for bucket in self.table for _, v in bucket]

    def items(self):
        """Get all key-value pairs in hash table"""
        return [(k, v) for bucket in self.table for k, v in bucket]

    def print_table(self, show_empty=False):
        """Print hash table structure with visualization"""
        print("\nHash Table Structure:")
        print("=" * 50)
        print(f"Size: {self.size}, Count: {self.count}, Load Factor: {self.count/self.size:.2f}")
        print("-" * 50)
        
        for i, bucket in enumerate(self.table):
            if bucket or show_empty:
                print(f"Index {i}: ", end="")
                if bucket:
                    print(" -> ".join([f"({k}: {v})" for k, v in bucket]))
                else:
                    print("[]")
        print("=" * 50)

    def visualize_operation(self, operation, key=None, value=None):
        """Visualize a specific operation with before/after states"""
        print(f"\nVisualizing {operation} Operation:")
        if key:
            print(f"Key: {key}, Hash: {self._hash(key)}")
        if value:
            print(f"Value: {value}")
            
        print("\nBefore:")
        self.print_table()
        
        if operation == "insert" and key and value:
            self.insert(key, value)
        elif operation == "delete" and key:
            self.delete(key)
        elif operation == "get" and key:
            result = self.get(key)
            print(f"Result: {result}")
            return
        
        print("\nAfter:")
        self.print_table()

# Example usage with enhanced visualization
if __name__ == "__main__":
    # Create hash table
    ht = HashTable(initial_size=4)  # Small size to demonstrate collisions
    
    # 1. Basic Insertions with Hash Values
    print("\n1. Basic Insertions:")
    data = [
        ("name", "John"),
        ("age", 30),
        ("city", "New York"),
        ("country", "USA")
    ]
    
    for key, value in data:
        print(f"\nInserting: {key} -> {value}")
        print(f"Hash value: {ht._hash(key)}")
        ht.visualize_operation("insert", key, value)
    
    # 2. Collision Demonstration
    print("\n2. Collision Demonstration:")
    collision_data = [
        ("phone", "123-456-7890"),
        ("email", "john@example.com")
    ]
    
    for key, value in collision_data:
        print(f"\nHash of '{key}': {ht._hash(key)}")
        ht.visualize_operation("insert", key, value)
    
    # 3. Delete Operation
    print("\n3. Delete Operation:")
    ht.visualize_operation("delete", "age")
    
    # 4. Search Operation
    print("\n4. Search Operation:")
    search_keys = ["name", "age", "phone"]
    for key in search_keys:
        print(f"\nSearching for: {key}")
        print(f"Hash value: {ht._hash(key)}")
        ht.visualize_operation("get", key)
    
    # 5. Resize Demonstration
    print("\n5. Resize Demonstration:")
    print("Adding more items to trigger resize...")
    more_data = [
        ("address", "123 Main St"),
        ("zip", "10001"),
        ("occupation", "Engineer"),
        ("salary", 100000)
    ]
    
    for key, value in more_data:
        print(f"\nInserting: {key} -> {value}")
        print(f"Hash value: {ht._hash(key)}")
        ht.visualize_operation("insert", key, value)
    
    # 6. Final State
    print("\n6. Final State:")
    ht.print_table(show_empty=True)
    
    # 7. Performance Metrics
    print("\n7. Performance Metrics:")
    print(f"Total items: {ht.count}")
    print(f"Table size: {ht.size}")
    print(f"Load factor: {ht.count/ht.size:.2f}")
    print(f"Collision rate: {sum(1 for bucket in ht.table if len(bucket) > 1)/ht.size:.2f}")
    
    # 8. Hash Distribution
    print("\n8. Hash Distribution:")
    distribution = {}
    for bucket in ht.table:
        length = len(bucket)
        distribution[length] = distribution.get(length, 0) + 1
    
    print("Bucket sizes distribution:")
    for size, count in sorted(distribution.items()):
        print(f"Buckets with {size} items: {count} ({count/ht.size*100:.2f}%)")
