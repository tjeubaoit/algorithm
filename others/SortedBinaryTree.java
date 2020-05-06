import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class SortedBinaryTree<T extends Comparable<T>> {

    private static class Node<T> {
        T data;
        Node<T> left;
        Node<T> right;
        Node<T> next;
        Node<T> prev;

        Node(T data) {
            this.data = data;
        }
    }

    private Node<T> root;
    private Node<T> head;
    private Node<T> tail;

    public Node<T> add(T data) {
        if (this.root == null) {
            this.root = new Node<>(data);
            this.head = root;
            this.tail = root;
            return this.root;
        }
        Node<T> node = this.root;
        while (true) {
            if (data.compareTo(node.data) < 0) {
                if (node.left == null) {
                    Node<T> newNode = new Node<>(data);
                    node.left = newNode;
                    this.insertBefore(node, newNode);
                    return newNode;
                } else {
                    node = node.left;
                }
            } else {
                if (node.right == null) {
                    Node<T> newNode = new Node<>(data);
                    node.right = newNode;
                    this.insertAfter(node, newNode);
                    return newNode;
                } else {
                    node = node.right;
                }
            }
        }
    }

    private void insertAfter(Node<T> after, Node<T> node) {
        Node<T> tmp = after.next;
        after.next = node;
        node.prev = after;

        node.next = tmp;
        if (tmp != null) {
            tmp.prev = node;
        }

        if (tail == after) {
            tail = node;
        }
    }

    private void insertBefore(Node<T> before, Node<T> node) {
        Node<T> tmp = before.prev;
        before.prev = node;
        node.next = before;

        node.prev = tmp;
        if (tmp != null) {
            tmp.next = node;
        }

        if (head == before) {
            head = node;
        }
    }

    public Iterator<T> iterator() {
        return new Iterator<T>() {
            private Node<T> curr = head;
            @Override
            public boolean hasNext() {
                return this.curr != null;
            }

            @Override
            public T next() {
                T data = curr.data;
                curr = curr.next;
                return data;
            }
        };
    }

    public List<T> asList() {
        return inOrder(this.root);
    }

    public List<T> inOrder(Node<T> node) {
        List<T> list = new LinkedList<>();
        if (node != null) {
            if (node.left != null) {
                list.addAll(inOrder(node.left));
            }
            list.add(node.data);
            if (node.right != null) {
                list.addAll(inOrder(node.right));
            }
        }
        return list;
    }

    public static void main(String[] args) {
        SortedBinaryTree<Integer> bst = new SortedBinaryTree<>();
        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            bst.add(random.nextInt(100));
        }

        Iterator<Integer> it = bst.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }

        System.out.println(bst.asList());
    }
}
