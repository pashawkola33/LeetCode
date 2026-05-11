/**
 * @lc id=104
 * @lc title=Maximum Depth of Binary Tree
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(h)
 */
package binary_trees;

public class MaximumDepthofBinaryTree {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftHeight = maxDepth(root.left);
        int rightHeight = maxDepth(root.right);

        return Math.max(leftHeight, rightHeight) + 1;
    }
}
