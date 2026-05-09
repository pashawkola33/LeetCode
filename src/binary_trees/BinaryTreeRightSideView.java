package binary_trees;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinaryTreeRightSideView {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        if (root == null) { // если корень пуст, выводим пустой список
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {

            int levelSize = queue.size();


            for (int i = 0; i < levelSize; i++) {
                TreeNode treeNode = queue.poll(); // получаем первого

                if (treeNode.left != null) { // записываем левого ребенка
                    queue.add(treeNode.left);
                }
                if (treeNode.right != null) { // записываем правого ребенка
                    queue.add(treeNode.right);
                }

                if(i == levelSize - 1){  // если наш i это последний элемент, тоесть левый мы его добавляем в результат
                    result.add(treeNode.val);
                }
            }
        }
        return result;
    }
}
