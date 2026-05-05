package linked_lists;

public class ListNode {
    int val;        // Значение (данные)
    ListNode next;  // Ссылка на следующий узел

    // Пустой конструктор
    ListNode() {}

    // Конструктор только для значения
    ListNode(int val) {
        this.val = val;
    }

    // Конструктор для значения и ссылки на следующий узел
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}