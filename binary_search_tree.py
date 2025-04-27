"""
Binary Search Tree Implementation
================================

Core Operations:
1. Insert
2. Search
3. Delete
4. Traversal (In-order, Pre-order, Post-order)
5. Find Min/Max
6. Height
7. Size

Visualization Examples:
----------------------
1. Basic BST Structure:
       5
      / \
     3   7
    / \ / \
   2  4 6  8

2. Insert Operation:
   Insert 1:
       5
      / \
     3   7
    / \ / \
   2  4 6  8
  /
 1

3. Delete Operation:
   Delete 3:
       5
      / \
     4   7
    /   / \
   2   6   8
  /
 1

4. Traversal Examples:
   In-order: [2, 3, 4, 5, 6, 7, 8]
   Pre-order: [5, 3, 2, 4, 7, 6, 8]
   Post-order: [2, 4, 3, 6, 8, 7, 5]

5. Min/Max Examples:
   Min: 2 (leftmost node)
   Max: 8 (rightmost node)

6. Height Example:
   Height: 3 (longest path from root to leaf)
       5
      / \
     3   7
    / \ / \
   2  4 6  8
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a value into BST
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = TreeNode(value)
                    return
                current = current.left
            elif value > current.value:
                if not current.right:
                    current.right = TreeNode(value)
                    return
                current = current.right
            else:
                return  # Value already exists

    # Search for a value in BST
    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    # Delete a value from BST
    def delete(self, value):
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def delete_helper(node, value):
            if not node:
                return None
            
            if value < node.value:
                node.left = delete_helper(node.left, value)
            elif value > node.value:
                node.right = delete_helper(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                temp = find_min(node.right)
                node.value = temp.value
                node.right = delete_helper(node.right, temp.value)
            
            return node

        self.root = delete_helper(self.root, value)

    # In-order traversal
    def inorder(self):
        result = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
        traverse(self.root)
        return result

    # Pre-order traversal
    def preorder(self):
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)
        traverse(self.root)
        return result

    # Post-order traversal
    def postorder(self):
        result = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
        traverse(self.root)
        return result

    # Find minimum value
    def find_min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    # Find maximum value
    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

    # Calculate height
    def height(self):
        def height_helper(node):
            if not node:
                return 0
            return 1 + max(height_helper(node.left), height_helper(node.right))
        return height_helper(self.root)

    # Count number of nodes
    def size(self):
        def size_helper(node):
            if not node:
                return 0
            return 1 + size_helper(node.left) + size_helper(node.right)
        return size_helper(self.root)

    # Print tree structure
    def print_tree(self):
        def print_helper(node, level=0, prefix="Root: "):
            if not node:
                return
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left or node.right:
                print_helper(node.left, level + 1, "L--- ")
                print_helper(node.right, level + 1, "R--- ")
        
        print("\nTree Structure:")
        print_helper(self.root)

    # Check if tree is balanced
    def is_balanced(self):
        def check_balance(node):
            if not node:
                return True, 0
            
            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)
            
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            
            return balanced, height
        
        balanced, _ = check_balance(self.root)
        return balanced

    # Build balanced BST from sorted list
    def build_balanced(self, values):
        def build_helper(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            node = TreeNode(values[mid])
            node.left = build_helper(start, mid - 1)
            node.right = build_helper(mid + 1, end)
            return node
        
        values.sort()
        self.root = build_helper(0, len(values) - 1)

# Example usage with visualization
if __name__ == "__main__":
    # Create BST
    bst = BST()
    
    # Insert values
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        bst.insert(value)
    
    # Print initial tree structure
    print("1. Initial BST Structure:")
    bst.print_tree()
    
    # Test search operations
    print("\n2. Search Operations:")
    print(f"Search 5: {bst.search(5)}")  # True
    print(f"Search 9: {bst.search(9)}")  # False
    
    # Test traversal operations
    print("\n3. Traversal Operations:")
    print(f"In-order: {bst.inorder()}")    # [2, 3, 4, 5, 6, 7, 8]
    print(f"Pre-order: {bst.preorder()}")  # [5, 3, 2, 4, 7, 6, 8]
    print(f"Post-order: {bst.postorder()}") # [2, 4, 3, 6, 8, 7, 5]
    
    # Test min/max operations
    print("\n4. Min/Max Operations:")
    print(f"Minimum value: {bst.find_min()}")  # 2
    print(f"Maximum value: {bst.find_max()}")  # 8
    
    # Test tree properties
    print("\n5. Tree Properties:")
    print(f"Height: {bst.height()}")  # 3
    print(f"Size: {bst.size()}")      # 7
    print(f"Is balanced: {bst.is_balanced()}")  # True
    
    # Test delete operation
    print("\n6. Delete Operation:")
    print("Before deletion:")
    bst.print_tree()
    bst.delete(3)
    print("\nAfter deleting 3:")
    bst.print_tree()
    
    # Insert new value
    print("\n7. Insert Operation:")
    bst.insert(1)
    print("After inserting 1:")
    bst.print_tree()
    
    # Build balanced BST from list
    print("\n8. Building Balanced BST:")
    balanced_bst = BST()
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    balanced_bst.build_balanced(values)
    print("Balanced BST structure:")
    balanced_bst.print_tree()
    print(f"Is balanced: {balanced_bst.is_balanced()}")  # True
    
    # Print final tree properties
    print("\n9. Final Tree Properties:")
    print(f"Height: {bst.height()}")
    print(f"Size: {bst.size()}")
    print(f"In-order traversal: {bst.inorder()}")
    print(f"Is balanced: {bst.is_balanced()}")
