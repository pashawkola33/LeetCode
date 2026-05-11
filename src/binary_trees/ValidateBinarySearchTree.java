/**
 * @lc id=98
 * @lc title=Validate Binary Search Tree
 * @lc difficulty=Medium
 * @lc time=O(n)
 * @lc space=O(h)
 */
package binary_trees;

import java.util.Stack;

public class ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MAX_VALUE, Long.MIN_VALUE);
    }

    public boolean validate(TreeNode node, long max, long min) {

        if (node == null) {
            return true;
        }

        if (node.val <= min || node.val >= max) {
            return false;
        }

        return validate(node.left, node.val, min) &&
                validate(node.right, max, node.val);
    }
}
