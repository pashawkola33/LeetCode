/**
 * @lc id=235
 * @lc title=Lowest Common Ancestor of a BST
 * @lc difficulty=Medium
 * @lc time=O(h)
 * @lc space=O(1)
 */
package binary_trees;

public class LowestCommonAncestorofaBinarySearchTree {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (root != null) {
            if (p.val < root.val && q.val < root.val) { // both are less? go to the left!
                root = root.left;
            }
            else if (p.val > root.val && q.val > root.val) { // both are bigger? go to the right!
                root = root.right;
            } else {
//             ((p.val > root.val && q.val < root.val) || (p.val < root.val && q.val > root.val))tree {
                return root;
            }
        }
        return null;
    }
}
