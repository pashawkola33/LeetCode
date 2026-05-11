/**
 * @lc id=226
 * @lc title=Invert Binary Tree
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(h)
 */
package binary_trees;


public class InvertBinaryTree {
    public TreeNode invertTree(TreeNode root) {
        TreeNode temp = new TreeNode();

        if (root == null) {
            return null;
        }

        temp = root.left; // stored left
        root.left = root.right; //left = right;
        root.right = temp;


        invertTree(root.right);
        invertTree(root.left);

        return root;
    }
}
