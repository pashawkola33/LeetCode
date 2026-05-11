# 🚀 LeetCode Mastery

This repository tracks my journey through algorithmic challenges, focusing on achieving optimal time and space complexity. Each solution is implemented in Java with a focus on clean code and performance.

## 📊 Problem Tracking

| # | Problem | Difficulty | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| 217 | Contains Duplicate | Easy | $O(n)$ | $O(n)$ |
| 1 | Two Sum | Easy | $O(n)$ | $O(n)$ |
| 242 | Valid Anagram | Easy | $O(n)$ | $O(1)$ |
| 121 | Best Time to Buy and Sell Stock | Easy | $O(n)$ | $O(1)$ |
| 704 | Binary Search | Easy | $O(\log n)$ | $O(1)$ |
| 125 | Valid Palindrome | Easy | $O(n)$ | $O(1)$ |
| 20 | Valid Parentheses | Easy | $O(n)$ | $O(n)$ |
| 3 | Longest Substring Without Repeating Characters | Medium | $O(n)$ | $O(k)$ |
| 206 | Reverse Linked List | Easy | $O(n)$ | $O(1)$ |
| 141 | Linked List Cycle | Easy | $O(n)$ | $O(1)$ |
| 21 | Merge Two Sorted Lists | Easy | $O(n + m)$ | $O(1)$ |
| 226 | Invert Binary Tree | Easy | $O(n)$ | $O(h)$ |
| 104 | Maximum Depth of Binary Tree | Easy | $O(n)$ | $O(h)$ |
| 102 | Binary Tree Level Order Traversal | Medium | $O(n)$ | $O(n)$ |
| 199 | Binary Tree Right Side View | Medium | $O(n)$ | $O(n)$ |
| 98 | Validate Binary Search Tree | Medium | $O(n)$ | $O(h)$ |
| 235 | Lowest Common Ancestor of a BST | Medium | $O(h)$ | $O(1)$ |

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
* **Range Validation:** Implemented recursive DFS with dynamic "min/max" boundaries to ensure all nodes satisfy BST properties.
* **BST Search Logic:** Utilized the "Left < Root < Right" property to find the Lowest Common Ancestor without traversing the entire tree, achieving $O(h)$ time.