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
