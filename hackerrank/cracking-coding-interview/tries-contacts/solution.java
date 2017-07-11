import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    private static final int MAX_CHARS = 26;
    private static final Node root = new Node();

    private static class Node {
        char value;
        int count = 0;
        Node[] children = new Node[MAX_CHARS];
    }

    private static void add(String contact) {
        Node node = root;
        for (int i = 0; i < contact.length(); i++) {
            char c = contact.charAt(i);
            Node child = findNode(node.children, c);
            if (child != null) {
                child.count += 1;
            } else {
                child = new Node();
                child.count = 1;
                node.children[c - 'a'] = child;
            }
            node = child;
        }
    }

    private static int find(String contact) {
        Node node = root;
        for (int i = 0; i < contact.length(); i++) {
            char c = contact.charAt(i);
            Node child = findNode(node.children, c);
            if (child == null) return 0;
            node = child;
        }
        return node.count;
    }

    private static Node findNode(Node[] nodes, char value) {
        return nodes[value - 'a'];        
    }

    private static void doOperation(String op, String contact) {
        if ("add".equals(op)) {
            add(contact);
        } else if ("find".equals(op)) {
            System.out.println(find(contact));
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int a0 = 0; a0 < n; a0++){
            String op = in.next();
            String contact = in.next();
            doOperation(op, contact);
        }
    }
}