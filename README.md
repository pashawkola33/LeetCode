# 🚀 LeetCode Mastery

This repository tracks my journey through algorithmic challenges, focusing on achieving optimal time and space complexity. Each solution is implemented in Java with a focus on clean code and performance.

Each solution file is expected to start with an `@lc` metadata header. The README sections below are generated automatically from those headers.

<!-- GENERATED:ROOT:START -->
## 📊 Problem Tracking

- **Total solved:** 18
- **Difficulty breakdown:** Easy 12, Medium 6, Hard 0
- **Topics covered:** `arrays_hashing` 4, `binary_search` 1, `binary_trees` 7, `linked_lists` 3, `sliding_window` 1, `stacks` 1, `two_pointers` 1

| # | Problem | Difficulty | Topic | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Two Sum | Easy | `arrays_hashing` | $O(n)$ | $O(n)$ |
| 3 | Longest Substring Without Repeating Characters | Medium | `sliding_window` | $O(n)$ | $O(k)$ |
| 20 | Valid Parentheses | Easy | `stacks` | $O(n)$ | $O(n)$ |
| 21 | Merge Two Sorted Lists | Easy | `linked_lists` | $O(n + m)$ | $O(1)$ |
| 98 | Validate Binary Search Tree | Medium | `binary_trees` | $O(n)$ | $O(h)$ |
| 102 | Binary Tree Level Order Traversal | Medium | `binary_trees` | $O(n)$ | $O(n)$ |
| 104 | Maximum Depth of Binary Tree | Easy | `binary_trees` | $O(n)$ | $O(h)$ |
| 121 | Best Time to Buy and Sell Stock | Easy | `arrays_hashing` | $O(n)$ | $O(1)$ |
| 125 | Valid Palindrome | Easy | `two_pointers` | $O(n)$ | $O(1)$ |
| 141 | Linked List Cycle | Easy | `linked_lists` | $O(n)$ | $O(1)$ |
| 199 | Binary Tree Right Side View | Medium | `binary_trees` | $O(n)$ | $O(n)$ |
| 206 | Reverse Linked List | Easy | `linked_lists` | $O(n)$ | $O(1)$ |
| 217 | Contains Duplicate | Easy | `arrays_hashing` | $O(n)$ | $O(n)$ |
| 226 | Invert Binary Tree | Easy | `binary_trees` | $O(n)$ | $O(h)$ |
| 230 | Kth Smallest Element in a BST | Medium | `binary_trees` | $O(h + k)$ | $O(h)$ |
| 235 | Lowest Common Ancestor of a BST | Medium | `binary_trees` | $O(h)$ | $O(1)$ |
| 242 | Valid Anagram | Easy | `arrays_hashing` | $O(n)$ | $O(1)$ |
| 704 | Binary Search | Easy | `binary_search` | $O(log n)$ | $O(1)$ |
<!-- GENERATED:ROOT:END -->

## 📈 Roadmap

- [x] Arrays & Hashing Basics
- [x] Two Pointers & Sliding Window
- [x] Stacks & Linked Lists
- [x] Trees (Current)
- [ ] Graphs
- [ ] Dynamic Programming

---

### 📝 Key Patterns Learned

#### Linked Lists
* **Pointer Manipulation:** Used the three-pointer technique to reverse list directions in-place.
* **Fast and Slow Pointers:** Applied Floyd's Cycle-Finding Algorithm to detect loops.

#### Trees (DFS & BFS)
* **Depth-First Search (Recursive):** Leveraged the call stack to solve bottom-up problems.
* **Breadth-First Search (Iterative):** Used a Queue and levelSize snapshots to process trees layer by layer.

#### Binary Search Tree (BST) Specifics
* **Inorder Traversal Logic:** Applied the property that Inorder traversal ($Left \to Root \to Right$) visits nodes in non-decreasing order.
* **Iterative Search with Stack:** Used an explicit Stack to implement early exit during search, optimizing time when only the $k$-th smallest element is needed.
* **Range Validation:** Used dynamic boundaries to ensure global BST properties.
