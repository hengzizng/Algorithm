import java.io.*;
import java.util.*;

public class BJ4256 {
    public static class Node {
        int value;
        Node left, right;

        public Node(int value) {
            this.value = value;
        }
    }

    public static int n, rootIndex;
    public static int[] preOrder, inOrder;
    public static StringBuilder sb;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder(); // 정답 출력을 위해 사용

        ////// test
        String input1 = "2\n" + "4\n" + "3 2 1 4\n" + "2 3 4 1\n" + "8\n" + "3 6 5 4 8 7 1 2\n" + "5 6 8 4 3 1 2 7";
        String input2 = "1\n" + "8\n" + "3 6 5 4 8 7 1 2\n" + "5 6 8 4 3 1 2 7";
        in = new BufferedReader(new StringReader(input1));
        ////// test

        int T = Integer.parseInt(in.readLine()); // 테스트케이스 개수

        for (int t = 0; t < T; t++) {
            n = Integer.parseInt(in.readLine()); // 노드 개수

            StringTokenizer st1 = new StringTokenizer(in.readLine(), " ");
            StringTokenizer st2 = new StringTokenizer(in.readLine(), " ");
            preOrder = new int[n]; // 전위순회 결과
            inOrder = new int[n]; // 중위순회 결과
            for (int i = 0; i < n; i++) {
                preOrder[i] = Integer.parseInt(st1.nextToken());
                inOrder[i] = Integer.parseInt(st2.nextToken());
            }

            rootIndex = 0; // 전위순회의 첫 번째 원소가 루트
            Node tree = makeTree(0, n - 1);

            postOrder(tree);

            sb.setLength(sb.length() - 1);
            sb.append("\n");
        }

        System.out.println(sb.toString());
    }

    // rootIndex: preOrder index (이번 트리의 root값을 나타냄)
    // left, middle, right: inOrder index (이번 트리의 왼쪽 오른쪽 부분 트리를 나타냄)
    // 왼쪽 부분 트리는 left ~ middle-1 , 오른쪽 부분 트리는 middle+1 ~ right
    public static Node makeTree(int left, int right) {
        if (left == right) {
            return new Node(preOrder[rootIndex]);
        }

        Node node = null;
        for (int i = left; i <= right; i++) {
            // 중위순회에서 이번 트리의 루트를 찾고 트리를 만든다.
            if (inOrder[i] == preOrder[rootIndex]) {
                node = new Node(inOrder[i]);

                // 왼쪽 부분 트리
                if (i > left) {
                    rootIndex++;
                    node.left = makeTree(left, i - 1);
                }

                // 오른쪽 부분 트리
                if (i < right) {
                    rootIndex++;
                    node.right = makeTree(i + 1, right);
                }

                break;
            }
        }

        return node;
    }

    // 후위순회
    public static void postOrder(Node node) {
        if (node.left != null) {
            postOrder(node.left);
        }
        if (node.right != null) {
            postOrder(node.right);
        }
        sb.append(node.value).append(" ");
    }
}
