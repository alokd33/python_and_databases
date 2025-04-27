"""
Complete Trie (Prefix Tree) Implementation with Examples
=====================================================

A Trie is a tree-like data structure that stores strings in a way that makes
prefix-based operations efficient. Each node represents a character in a string,
and paths from root to nodes form words. Common prefixes are shared between words.

Key Features:
1. O(L) time complexity for search, insert, and delete (L = length of word)
2. O(1) time complexity for checking if a prefix exists
3. Memory efficient for storing words with common prefixes
4. Perfect for autocomplete, spell checking, and prefix-based searches

Common Use Cases:
1. Autocomplete systems
2. Spell checkers
3. IP routing (longest prefix matching)
4. Word games (Boggle, Scrabble)
5. Search engines
6. Contact list search
"""
"""
Trie (Prefix Tree) Implementation
================================

// ... existing code ...

Detailed Visualization Examples with Step-by-Step Explanation:
-----------------------------------------------------------

1. Basic Trie Structure:
   --------------------
   Let's build a trie with words: "cat", "car", "cart", "dog"

   Step 1: Insert "cat"
   - Start at root
   - Add path: c -> a -> t
   - Mark 't' as end of word
   
   Structure:
        root
       /
      c
     /
    a
   /
  t (end)

   Step 2: Insert "car"
   - Start at root
   - Follow existing path: c -> a
   - Add new branch: r
   - Mark 'r' as end of word
   
   Structure:
        root
       /
      c
     /
    a
   / \
  t   r (end)

   Step 3: Insert "cart"
   - Start at root
   - Follow existing path: c -> a -> r
   - Add new node: t
   - Mark 't' as end of word
   
   Structure:
        root
       /
      c
     /
    a
   / \
  t   r
     /
    t (end)

   Step 4: Insert "dog"
   - Start at root
   - Add new path: d -> o -> g
   - Mark 'g' as end of word
   
   Final Structure:
        root
       /    \
      c      d
     /        \
    a          o
   / \          \
  t   r          g (end)
     /
    t (end)

2. Search Operation Example:
   -----------------------
   Searching for "car":
   1. Start at root
   2. Follow 'c' -> 'a' -> 'r'
   3. Check if 'r' is marked as end
   4. Found!

   Searching for "ca":
   1. Start at root
   2. Follow 'c' -> 'a'
   3. 'a' is not marked as end
   4. Not found (but prefix exists)

3. Prefix Search Example:
   ---------------------
   Finding words with prefix "ca":
   1. Start at root
   2. Follow 'c' -> 'a'
   3. From 'a', find all paths to end nodes:
      - a -> t (cat)
      - a -> r (car)
      - a -> r -> t (cart)
   4. Return: ["cat", "car", "cart"]

4. Delete Operation Example:
   -----------------------
   Deleting "car":
   1. Search for "car"
   2. Find path: c -> a -> r
   3. Unmark 'r' as end
   4. Keep structure (other words use same path)
   
   Result:
        root
       /    \
      c      d
     /        \
    a          o
   / \          \
  t   r          g (end)
     /
    t (end)

5. Real-World Example - Autocomplete:
   --------------------------------
   Dictionary: ["apple", "app", "application", "banana", "ball"]

   Structure:
        root
       /    \
      a      b
     /        \
    p          a
   / \          \
  p   p          l
 /     \          \
l       l          l
e       i          a
        c          n
        a          a
        t
        i
        o
        n

   User types "app":
   1. Follow path: a -> p -> p
   2. Find all words from this point:
      - app
      - apple
      - application
   3. Return suggestions: ["app", "apple", "application"]

6. Memory Optimization Example:
   --------------------------
   Storing similar words:
   Original words: ["hello", "hell", "help", "he"]
   
   Without Trie:
   - Store each word separately
   - Total characters: 4 + 4 + 4 + 2 = 14
   
   With Trie:
   - Share common prefix "he"
   - Additional characters: "llo", "l", "lp"
   - Total unique characters: 2 + 3 + 1 + 2 = 8
   - Memory saved: 6 characters

7. Performance Comparison Example:
   -----------------------------
   Operations on 10,000 words:
   
   Hash Table:
   - Insert: O(1) per word
   - Search: O(1) per word
   - Prefix Search: O(n) scan all words
   
   Trie:
   - Insert: O(L) per word (L = average word length)
   - Search: O(L) per word
   - Prefix Search: O(L) + O(k) (k = number of matches)
   
   Example with 5-letter words:
   Hash Table Prefix Search: ~10,000 comparisons
   Trie Prefix Search: ~5 steps + ~100 matches

8. Practical Use Case - Spell Checker:
   ---------------------------------
   Dictionary: ["cat", "car", "cart", "dog", "do", "done"]

   User types "carrt":
   1. Find closest matches:
      - Follow path: c -> a -> r
      - Possible corrections:
        * "car" (delete extra 'r')
        * "cart" (delete extra 'r')
   2. Return suggestions: ["car", "cart"]

// ... rest of the existing code ...
"""


class TrieNode:
    """Node class for Trie implementation"""
    def __init__(self):
        self.children = {}  # Maps character to child node
        self.is_end = False  # Marks end of a word
        self.count = 0  # Count of words with this prefix
        self.frequency = 0  # Frequency of word (useful for autocomplete)

class Trie:
    """Trie implementation with visualization and examples"""
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0

    def insert(self, word: str, frequency: int = 1) -> None:
        """Insert a word into the trie with optional frequency"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True
        node.frequency = frequency
        self.total_words += 1

    def search(self, word: str) -> bool:
        """Check if word exists in trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Check if any word in trie starts with prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def get_words_with_prefix(self, prefix: str, limit: int = None) -> list:
        """Get all words that start with prefix, optionally limited by count"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        self._dfs(node, prefix, words, limit)
        return words

    def _dfs(self, node: TrieNode, current_word: str, words: list, limit: int = None) -> None:
        """Depth-first search to collect words with frequency sorting"""
        if node.is_end:
            words.append((current_word, node.frequency))
        
        # Sort children by frequency for better autocomplete
        sorted_children = sorted(node.children.items(), 
                               key=lambda x: x[1].frequency, 
                               reverse=True)
        
        for char, child in sorted_children:
            if limit and len(words) >= limit:
                break
            self._dfs(child, current_word + char, words, limit)

    def delete(self, word: str) -> bool:
        """Delete a word from trie"""
        if not self.search(word):
            return False
            
        node = self.root
        for char in word:
            node = node.children[char]
            node.count -= 1
        node.is_end = False
        self.total_words -= 1
        return True

    def get_prefix_count(self, prefix: str) -> int:
        """Get count of words with given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

    def print_trie(self, node=None, prefix="", is_last=True):
        """Print trie structure visually with frequencies"""
        if node is None:
            node = self.root
            
        # Print current node
        node_info = []
        if node.is_end:
            node_info.append("(end)")
        if node.frequency > 0:
            node_info.append(f"[freq: {node.frequency}]")
        if node.count > 0:
            node_info.append(f"[count: {node.count}]")
            
        print(prefix + ("└── " if is_last else "├── ") + 
              " ".join(node_info))
        
        # Print children
        prefix += "    " if is_last else "│   "
        children = list(node.children.items())
        for i, (char, child) in enumerate(children):
            is_last_child = i == len(children) - 1
            print(prefix + ("└── " if is_last_child else "├── ") + char)
            self.print_trie(child, prefix, is_last_child)

    def visualize_operation(self, operation: str, word: str = None, 
                          frequency: int = None, prefix: str = None):
        """Visualize a specific operation with before/after states"""
        print(f"\nVisualizing {operation} Operation:")
        if word:
            print(f"Word: {word}")
        if frequency:
            print(f"Frequency: {frequency}")
        if prefix:
            print(f"Prefix: {prefix}")
            
        print("\nBefore:")
        self.print_trie()
        
        if operation == "insert" and word:
            self.insert(word, frequency or 1)
        elif operation == "delete" and word:
            self.delete(word)
        elif operation == "search" and word:
            result = self.search(word)
            print(f"Result: {'Found' if result else 'Not found'}")
            return
        elif operation == "prefix" and prefix:
            words = self.get_words_with_prefix(prefix)
            print(f"Words with prefix '{prefix}': {words}")
            return
        
        print("\nAfter:")
        self.print_trie()

# Example usage with detailed explanations
if __name__ == "__main__":
    # Create trie
    trie = Trie()
    
    print("=== Basic Trie Operations ===")
    
    # 1. Insert words with frequencies
    print("\n1. Inserting words with frequencies:")
    words_with_freq = [
        ("cat", 5),
        ("car", 3),
        ("cart", 2),
        ("dog", 4),
        ("do", 1),
        ("done", 2)
    ]
    
    for word, freq in words_with_freq:
        print(f"\nInserting: {word} (frequency: {freq})")
        trie.visualize_operation("insert", word, freq)
    
    # 2. Search operations
    print("\n2. Search operations:")
    test_words = ["cat", "car", "cart", "dog", "do", "done", "ca", "d"]
    for word in test_words:
        print(f"\nSearching for: {word}")
        trie.visualize_operation("search", word)
    
    # 3. Prefix operations
    print("\n3. Prefix operations:")
    prefixes = ["ca", "do", "car", "d"]
    for prefix in prefixes:
        print(f"\nFinding words with prefix: {prefix}")
        trie.visualize_operation("prefix", prefix=prefix)
    
    # 4. Delete operations
    print("\n4. Delete operations:")
    words_to_delete = ["car", "do"]
    for word in words_to_delete:
        print(f"\nDeleting: {word}")
        trie.visualize_operation("delete", word)
    
    print("\n=== Advanced Use Cases ===")
    
    # 5. Autocomplete example
    print("\n5. Autocomplete example:")
    autocomplete_trie = Trie()
    autocomplete_words = [
        ("apple", 10),
        ("app", 5),
        ("application", 3),
        ("banana", 8),
        ("ball", 6)
    ]
    
    for word, freq in autocomplete_words:
        autocomplete_trie.insert(word, freq)
    
    print("\nTrie structure for autocomplete:")
    autocomplete_trie.print_trie()
    
    user_input = "app"
    print(f"\nAutocomplete suggestions for '{user_input}':")
    suggestions = autocomplete_trie.get_words_with_prefix(user_input)
    print(f"Suggestions: {suggestions}")
    
    # 6. Spell checker example
    print("\n6. Spell checker example:")
    spell_check_trie = Trie()
    dictionary = ["cat", "car", "cart", "dog", "do", "done"]
    
    for word in dictionary:
        spell_check_trie.insert(word)
    
    misspelled_word = "carrt"
    print(f"\nChecking misspelled word: {misspelled_word}")
    
    # Find closest matches
    prefix = misspelled_word[:3]  # First 3 characters
    suggestions = spell_check_trie.get_words_with_prefix(prefix)
    print(f"Possible corrections: {suggestions}")
    
    # 7. Performance comparison
    print("\n7. Performance comparison:")
    import time
    import random
    import string
    
    def generate_random_word(length):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    # Test data
    test_size = 10000
    words = [generate_random_word(5) for _ in range(test_size)]
    prefixes = [word[:3] for word in words[:1000]]
    
    # Trie performance
    performance_trie = Trie()
    start_time = time.time()
    for word in words:
        performance_trie.insert(word)
    trie_insert_time = time.time() - start_time
    
    start_time = time.time()
    for prefix in prefixes:
        performance_trie.get_words_with_prefix(prefix)
    trie_search_time = time.time() - start_time
    
    # Hash table performance
    hash_table = set()
    start_time = time.time()
    for word in words:
        hash_table.add(word)
    hash_insert_time = time.time() - start_time
    
    start_time = time.time()
    for prefix in prefixes:
        [word for word in hash_table if word.startswith(prefix)]
    hash_search_time = time.time() - start_time
    
    print(f"Trie Insert {test_size} words: {trie_insert_time:.4f} seconds")
    print(f"Trie Search 1000 prefixes: {trie_search_time:.4f} seconds")
    print(f"Hash Insert {test_size} words: {hash_insert_time:.4f} seconds")
    print(f"Hash Search 1000 prefixes: {hash_search_time:.4f} seconds")
    
    # 8. Memory usage
    print("\n8. Memory usage:")
    import sys
    trie_memory = sys.getsizeof(performance_trie) + sum(
        sys.getsizeof(node) for node in performance_trie.root.children.values()
    )
    hash_memory = sys.getsizeof(hash_table) + sum(
        sys.getsizeof(word) for word in hash_table
    )
    print(f"Trie Memory: {trie_memory/1024:.2f} KB")
    print(f"Hash Memory: {hash_memory/1024:.2f} KB")
    
    # 9. Real-world example - Contact Search
    print("\n9. Contact Search Example:")
    contact_trie = Trie()
    contacts = [
        ("John Doe", 5),
        ("Jane Smith", 3),
        ("John Smith", 4),
        ("Alice Johnson", 2),
        ("Bob Wilson", 1)
    ]
    
    for name, freq in contacts:
        contact_trie.insert(name.lower(), freq)
    
    search_prefix = "john"
    print(f"\nSearching contacts with prefix: {search_prefix}")
    results = contact_trie.get_words_with_prefix(search_prefix)
    print(f"Found contacts: {results}")
