public class DoublyLinkedList {
    private class Node {
        public String data;
        public Node prev;
        public Node next;

        public Node(String data) {
            this.data = data;
        }

        public Node(String data, Node prev, Node next) {
            this(data);
            this.prev = prev;
            this.next = next;
        }
    }

    public Node head;
    public Node tail;
    public int size;

    public void addFirst(String data) {
        Node newNode = new Node(data, null, head);

        if (head != null) {
            head.prev = newNode;
        }

        head = newNode;

        if (tail == null) {
            tail = head;
        }

        size++;
    }

    public void addLast(String data) {
        Node newNode = new Node(data, tail, null);

        if (tail != null) {
            tail.next = newNode;
        }

        tail = newNode;

        if (head == null) {
            head = tail;
        }

        size++;
    }

    public void printList() {
        System.out.println("-----");
        for (DoublyLinkedList.Node node = head; node != null; node = node.next) {
            System.out.print(node.data + " ");
        }
        System.out.println();
        System.out.println("-----");
    }

    // 값만 변경
    public void reverse() {
        Node front = head;
        Node end = tail;

        for (int i = 0; i < size / 2; i++) {
            String temp = front.data;
            front.data = end.data;
            end.data = temp;

            front = front.next;
            end = end.prev;
        }
    }

    public static void main(String[] args) {

        DoublyLinkedList list = new DoublyLinkedList();
        list.addLast("1");
        list.addFirst("2");
        list.addFirst("3");
        list.addLast("4");
        list.addLast("5");
        list.printList();

        list.reverse();
        list.printList();

    }
}
