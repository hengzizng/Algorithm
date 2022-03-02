public class SinglyLinkedList {
    private class Node {
        public String data;
        public Node next;

        public Node(String data) {
            this.data = data;
        }

        public Node(String data, Node next) {
            this(data);
            this.next = next;
        }
    }

    public Node head;

    public void addFirst(String data) {
        Node newNode = new Node(data, head);
        head = newNode;
    }

    public void addLast(String data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
        } else {
            getLastNode().next = newNode;
        }
    }

    public Node getLastNode() {
        Node node = head;

        while (node.next != null) {
            node = node.next;
        }

        return node;
    }

    public void printList() {
        System.out.println("-----");
        for (Node node = head; node != null; node = node.next) {
            System.out.print(node.data + " ");
        }
        System.out.println();
    }

    // 연결 자체를 변경
    public void reverse() {
        Node node = null;
        while (head != null) {
            Node temp = head;
            head = head.next;
            temp.next = node;
            node = temp;
        }
        head = node;
    }

    public static void main(String[] args) {

        SinglyLinkedList list = new SinglyLinkedList();
        list.addFirst("1");
        list.addFirst("2");
        list.addFirst("3");
        list.addLast("4");
        list.addLast("5");
        list.printList();

        list.reverse();
        list.printList();

    }
}
