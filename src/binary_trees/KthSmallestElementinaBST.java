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
