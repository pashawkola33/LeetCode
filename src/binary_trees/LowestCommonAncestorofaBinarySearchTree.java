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
