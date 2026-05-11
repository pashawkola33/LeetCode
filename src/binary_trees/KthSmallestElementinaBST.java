/**
 * @lc id=230
 * @lc title=Kth Smallest Element in a BST
 * @lc difficulty=Medium
 * @lc time=O(h + k)
 * @lc space=O(h)
 */
package binary_trees;


import java.util.Stack;

public class KthSmallestElementinaBST {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();

        if(root == null){
            return 0;
        }
        while(true){
            while(root != null){
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();

            k--;
            if(k ==0){
                return root.val;
            }
            root = root.right;
        }
    }
}
